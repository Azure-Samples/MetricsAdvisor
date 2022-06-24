# Metrics Advisor
[Azure Metrics Advisor](https://azure.microsoft.com/en-us/services/metrics-advisor/#overview) is a time series monitoring platform that provides a set of APIs and a web-based workspace for ingesting time-series data, anomaly detection, sending alerts through multiple channels and diagnosing anomalous incidents without the need-to-know machine learning or write any code. For more information, please visit the [Azure Metrics Advisor technical documentation](https://docs.microsoft.com/en-us/azure/applied-ai-services/metrics-advisor/).

Metrics Advisor is designed for streaming data scenarios. This tutorial will help you create a Metrics Advisor resource and continuously stream the sample data into it via Azure blob storage. We will also show you how to set up the anomaly detection setting pipeline in Metrics Advisor step by step. Let's go! 

## Getting Started

### Step 1 - Create a Metrics Advisor resource
To get started, you need to create an Azure Metrics Advisor resource in your Azure resource group. To set up Metrics Advisor resource, navigate to your resource group in the [Azure portal](https://ms.portal.azure.com/), click `Create` to add a new resource, then select `Metrics Advisor`. Make sure the details are accurate, then create the resource. You can move to the next step while the resource is being created.

### Step 2 - Create a Blob Storage account

Next, you will need to add a storage account in your resource group to store the incoming messages. Within your resource group in the Azure portal, click `Create` and type `Storage account`. Make sure that the storage account is in the same region as your Metrics Advisor resource, and then click on `Review and create`. Next, navigate to your new storage account, click on the containers link on the left, and create a new storage container by clicking the `+ Container` and give it a name, and then click `Create`.

### Step 3 - Creating the virtual environment and installing the dependencies

Open a terminal, clone this repo to your local machine, then run the following commands to create and activate a new conda virtual environment and install the dependencies:
```bash
y | conda create --name metrics-advisor python=3.7
source activate metrics-advisor
pip install -r requirements.txt
```
Next, enter the following line in your terminal, replacing `<your-blob-connection-string>` with the blob connection string for your Azure blob storage account that you just created. You can find your connection string by navigating to your storage account in the Azure portal, and copying the `Connection string` from the "Access keys" section of the resource details.
```bash
export BLOB_CONNECTION_STRING="<your-blob-connection-string>"
```

### Step 4 - Run the script to stream data into Azure blob storage

The [stream2metricsadvisor.py](stream2metricsadvisor.py) script helps simulate streaming data into Azure Blob Storage (and therefore, Azure Metrics Advisor as well) in the absense of real sensor data streaming into your data store. This script accepts a CSV file and continuously loops over the data, processing the data from each timestamp at regular intervals, and pushes this data to blob storage. Once the data is in blob storage, you can use the [Azure Metrics Advisor web UI](https://metricsadvisor.azurewebsites.net) to create a data feed to ingest this streaming data and perform anomaly detection.

Please refer to the docstring inside the script for more details. You can use your own data instead of the sample CSV that we provide, but please modify the script if your data schema doesn't match the one we use.

To run this script, use the following command:
```bash
nohup python stream2metricsadvisor.py --csv_file=<path_to .csv> --container_name=<container_name> --minute_resample=5 > nohup.out 2>&1 &
```
Where `<path_to .csv>` points to your CSV file, and `<container_name>` is the name of the storage container in your storage account where all the messages will be uploaded.

After you run the script, you can monitor its progress using the following command:
```bash
tail -f nohup.out
```
If you like to stop this script after you are finished with this tutorial, you can kill the process by running `kill <pid>`, where `<pid>` is the process id of the Python script. 

### Step 5 - Create a data feed in Metrics Advisor

 go to [Metrics Advisor landing page](https://metricsadvisor.azurewebsites.net) to choose the workspace you just created and click **Get started** to login. 

Choose **Add data feed** and start to onboard the data to Metrics Advisor, choose the settings and write down your own connection string and query.

![onboard_data](/media/methane_create_datafeed.png)

After you click **Load data**, you should choose the data schema same as below.

![choose_schema](/media/data_onboarding_configuration.png)

### Step 6 - Configure your anomaly detection and alerting settings

After you onboard the data, wait for some time of data ingestion into Metrics Advisor, it's wise to take a cup of coffee.☕

During that time, you could go to the **Hooks** in Metrics Advisor to set up an alert which could go to your teams, email, webhook, etc. based on your preference.

![setup_hooks](/media/methane_hook_setup.png)

Now, you could go to one of the metrics like *methane concentration* to see the detection results. You could also set some different detection method in the **Metric-level configuration** on the left.

![detect anomalies](/media/methane-anomaly-detection.png)

### Step 7 - Check the detected anomalies in Incident Hub

For the anomalies that have been detected, you could check the details behind this anomaly through the **incident** in your metric page.

![incident](/media/methane_incident.png)

When you click one of the incident, you'll be led to **Incident Hub**, which is a place that allows you to see an overview of all the latest detected anomalies in real-time and see their severity scores. It also allows you to diagnose and analyze the root cause of each incident.

![incident_hub](/media/methane_incident_hub.png)

If you click one incident in the **Incident list** down below, you could see the more detail of a specific incident.

![incident_detail](/media/methane_incident_details.png)



## Additional resources

📰 Read our blog post on [Detecting Methane Leaks using Azure Metrics Advisor](https://techcommunity.microsoft.com/t5/ai-cognitive-services-blog/detecting-methane-leaks-using-azure-metrics-advisor/ba-p/3254005)

👉 Join our community: [https://aka.ms/AnomalyDetector/Advisors](https://aka.ms/AnomalyDetector/Advisors)

🔗 Metrics Advisor Workspace: [https://metricsadvisor.azurewebsites.net/](https://metricsadvisor.azurewebsites.net/)

📑 Metrics Advisor documentation: [https://aka.ms/madoc](https://metricsadvisor.azurewebsites.net/)