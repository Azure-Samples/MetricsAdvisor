# Metrics Advisor
[Azure Metrics Advisor](https://azure.microsoft.com/en-us/services/metrics-advisor/#overview) is a time series monitoring platform that provides a set of APIs and a web-based workspace for ingesting time-series data, anomaly detection, sending alerts through multiple channels and diagnosing anomalous incidents without the need-to-know machine learning or write any code. For more information, please visit the [Azure Metrics Advisor technical documentation](https://docs.microsoft.com/en-us/azure/applied-ai-services/metrics-advisor/).

Metrics Advisor is designed for streaming data scenarios. **This code allows you to simulate a streaming data source and ingest its data into a Metrics Advisor workspace to test its capabilities and functionality in real-time.** 

The [stream2metricsadvisor.py](stream2metricsadvisor.py) script helps simulate streaming data into Azure Blob Storage (and therefore, Azure Metrics Advisor as well) in the absense of real sensor data streaming into your data store. This script accepts a CSV file and continuously loops over the data, processing the data from each timestamp at regular intervals, and pushes this data to blob storage. Once the data is in blob storage, you can use the [Azure Metrics Advisor web UI](https://metricsadvisor.azurewebsites.net) to create a data feed to ingest this streaming data and perform anomaly detection.

Please refer to the docstring inside the script for more details. You can use your own data instead of the sample CSV that we provide, but please modify the script if your data schema doesn't match the one we use.


## Getting Started


### Step 1 - Create a Metrics Advisor workspace
To get started, you need to create a Metrics Advisor resource in your Azure resource group. To set up Metrics Advisor resource, 


### Step 2 - Create a Blob Storage account

### Step 3 - Creating the virtual environment and installing the dependencies

Open a terminal, and run the following command to create and activate a new conda virtual environment and install the dependencies:
```bash
y | conda create --name metrics-advisor python=3.7
source activate metrics-advisor
pip install -r requirements.txt
```
Next, enter the following line in your terminal, replacing `<your-blob-connection-string>` with the blob connection string for your Azure blob storage account. You can find your connection string by navigating to your storage account in the Azure portal, and copying the `Connection string` from the "Access keys" section of the resource details.
```bash
export BLOB_CONNECTION_STRING="<your-blob-connection-string>"
```
### Step 4 - Run the script 

To run this script, use the following command:
```bash
nohup python stream2metricsadvisor.py --csv_file=<path_to .csv> --container_name=<container_name> --minute_resample=5 > nohup.out 2>&1 &
```

To monitor the progress of the script, use the following command:
$ tail -f nohup.out
To kill the script, use the following command:
$ kill <pid>
"""

### Step 5 -- Create a data feed in Metrics Advisor

<!-- screenshots + add the data schema -->

### Step 6 - Set up your Metrics Advisor workspace

Now, you can use Azure Metrics Advisor to perform anomaly detection on your data. You can refer to the Azure Metrics Advisor [quickstart page](https://docs.microsoft.com/en-us/azure/applied-ai-services/metrics-advisor/quickstarts/web-portal) page for more information on how to get started.


## Bringing your own data
explain data schema here.. 