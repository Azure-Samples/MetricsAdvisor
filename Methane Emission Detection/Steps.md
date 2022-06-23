# Introduction
This tutorial will help you create a Metrics Advisor resource and use the sample data to set up anomaly detection pipeline in Metrics Advisor step by step. Let's go!

# 0. Resources

👉 Join our community: https://aka.ms/AnomalyDetector/Advisors

🔗 Metrics Advisor Workspace: https://metricsadvisor.azurewebsites.net/

📑 Metrics Advisor documentation: https://aka.ms/madoc

# 1. Create a Metrics Advisor resource
Create a Azure Metrics Advisor resource in [Azure portal](https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesMetricsAdvisor). It may take about 20mins to create the resource successfully. 

During this period, you can get back to this repository and move to step 2 to prepare the sample data. 

# 2. Prepare sample data
Download the sample data [here](/Methane%20Emission%20Detection/MASample_Methane.csv). This sample data contains 2 variables, *methane concentration* and *temperature*, which are from *device A* and *device B*. After the CSV file is downloaded, you should ingest the data into a database. Here we use Azure Data Explorer as an example.

Go to Azure Data Explorer(ADX) and select **Data** to the left to upload the CSV file.

![data_ingestion](/media/adx_data_ingestion.png)

💡Note: You'd better shift the timestamp to a recent time period to have a better real-time experience in Metrics Advisor. For now, the time period in sample data is from 2022-6-6 to 2022-7-26, as time goes by, you should probably change the time period start from a future date.

# 3. Create data feeds
After resource is created and sample data has been ingested to the database, go to [Metrics Advisor landing page](https://metricsadvisor.azurewebsites.net) to choose the workspace you just created and click **Get started** to login. 

Choose **Add data feed** and start to onboard the data to Metrics Advisor, choose the settings and write down your own connection string and query.

![onboard_data](/media/methane_create_datafeed.png)

After you click **Load data**, you should choose the data schema same as below.

![choose_schema](/media/data_onboarding_configuration.png)

# 4. Check the detection process and results

After you onboard the data, wait for some time of data ingestion into Metrics Advisor, it's wise to take a cup of coffee.☕

During that time, you could go to the **Hooks** in Metrics Advisor to set up an alert which could go to your teams, email, webhook, etc. based on your preference.

![setup_hooks](/media/methane_hook_setup.png)

Now, you could go to one of the metrics like *methane concentration* to see the detection results. You could also set some different detection method in the **Metric-level configuration** on the left.

![detect anomalies](/media/methane-anomaly-detection.png)

# 5. Check the incidents

For the anomalies that have been detected, you could check the details behind this anomaly through the **incident** in your metric page.

![incident](/media/methane_incident.png)

When you click one of the incident, you'll be led to **Incident Hub**, which is a place that allows you to see an overview of all the latest detected anomalies in real-time and see their severity scores. It also allows you to diagnose and analyze the root cause of each incident.

![incident_hub](/media/methane_incident_hub.png)

If you click one incident in the **Incident list** down below, you could see the more detail of a specific incident.

![incident_detail](/media/methane_incident_details.png)

# 6. View demo script and present the demo
The [demo script](/Methane%20Emission%20Detection/Demo-script.md) is published in the repository as well, please go through that first and get familiar with the demo story. After checking all the metrics data is onboard and having the latest detection results, you're ready to go!