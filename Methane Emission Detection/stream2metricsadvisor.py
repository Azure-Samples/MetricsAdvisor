# -------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# Licensed under Microsoft Incubation License Agreement:
#
# -------------------------------------------------------------

import argparse
import os
from datetime import datetime
import time

import pandas as pd
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient




def main(args):
    """This function is called when the script is run from the command line.
    This script is used to loop over a csv file containing sensor data, process
    the data with new timestamps, and format the data in the metrics advisor format,
    then continuosly upload the data to blob storage at a regular interval.

    Args:
        args (argparse.ArgumentParser): Command line arguments.
    """
    df = pd.read_csv(args.csv_file)

    assert os.getenv(
        "BLOB_CONNECTION_STRING"
    ), "No blob connection string found in .env file"

    print("******* CONNECTING TO AZURE BLOB STORAGE *******")
    blob_service_client = BlobServiceClient.from_connection_string(
        os.getenv("BLOB_CONNECTION_STRING")
    )

    print("******* CREATING THE AZURE BLOB CONTAINER *******")
    try:
        blob_service_client.create_container(args.container_name)
    except ResourceExistsError:
        print("Container: %s already exists", args.container_name)

    print("******* PROCESSING THE DATA FRAME *******")

    df = df[
        [
            "timestamp",
            "device",
            "methane",
            "wind_speed_resultant",
            "wind_direction",
            "temperature",
        ]
    ]

    print("Number of devices: " + str(len(df[["device"]].drop_duplicates())))

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    dft = df.set_index(["device", "timestamp"])

    print(f"        Dataframe length before resampling: {len(dft.index.unique())}")
    print(f"        Resampling the dataframe to {str(args.minute_resample)} minutes")

    idx = pd.to_datetime(dft.index.get_level_values(1)).ceil(
        f"{args.minute_resample}min"
    )
    dft = dft.groupby(["device", idx]).agg("mean").dropna(how="all")
    dft = dft.swaplevel(0, 1, 0).sort_index(0)
    dft = dft.reset_index(level=1)
    print(f"        Dataframe length after resampling: {len(dft.index.unique())}")

    # Format the timestamp column to ISO 8601:
    dft.index = dft.index.map(
        lambda x: datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S+00:00").isoformat() + "Z"
    )

    print("******* ENTERING THE MAIN LOOP *******")
    idx = 0
    starttime = time.time()
    timestamps = dft.index.unique()
    run_interval = args.minute_resample * 60.0  # seconds

    while True:
        print(str(datetime.now().replace(microsecond=0)) + " -- Index: ", idx)
        timestamp = timestamps[idx % len(timestamps)]
        row = dft.loc[timestamp]
        row = row.reset_index(drop=False)
        # get a new timestamp:
        now = datetime.now().replace(microsecond=0, second=0)
        # round the minutes down to the closest minute that matches the minute_resample rate
        now = now.replace(
            minute=args.minute_resample * (now.minute // args.minute_resample)
        )
        # use the new timestamp:
        row["timestamp"] = now.isoformat() + "Z"
        # Format the data and upload to blob:
        path = now.strftime("%Y/%m/%d/%Y-%m-%d-%H-%M.json")
        data = row.to_json(
            index=True,
            date_format="iso",
            date_unit="s",
            orient="records",
        )
        # Note the Metrics Advisor blob template used: %Y/%m/%d/%Y-%m-%d-%h-%M.json
        blob_client = blob_service_client.get_blob_client(
            container=args.container_name, blob=path
        )
        blob_client.upload_blob(data)

        idx += 1
        # sleep for the remainder of the interval
        time.sleep(run_interval - ((time.time() - starttime) % run_interval))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="arguments")
    parser.add_argument("--csv_file", type=str, help="Path to the csv file")
    parser.add_argument(
        "--container_name",
        type=str,
        help="Container name where the files will be stored",
    )
    parser.add_argument(
        "--minute_resample",
        type=int,
        help="Number of minutes to resample the data to",
    )
    args = parser.parse_args()
    main(args)
