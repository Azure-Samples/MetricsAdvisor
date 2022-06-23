# Context and customer pain points
Methane (CH4) is a potent greenhouse gas that is much more effective at absorbing infrared radiation than CO2, and therefore, has a severe global warming impact. The Global Warming Potential (GWP) of a greenhouse gas is its ability to trap extra heat in the atmosphere over time relative to CO2. The Intergovernmental Panel on Climate Change (IPCC) estimates the 20-year GWP of methane to be more than 80 times that of CO2, indicating its potency as a greenhouse gas. This underscores the importance of detection and remediation of methane leaks into the atmosphere.  

Let's meet Bob, who is an 👨‍💻engineer from an energy company. He plans to work on the methane emission detection in the natural gas transmission pipeline, since this methane leak will not only exacerbate the greenhouse effect, but could lead to potential explosion in the production and processing pipeline.

# How Metrics Advisor helps
Bob's company has taken Metrics Advisor as their methane concentration detection solution, and Bob uploaded all telemetries to Metrics Advisor. Azure Metrics Advisor provides a powerful time-series monitoring platform that offers a set of APIs and a web-based workspace for ingesting time-series data, performing univariate and multivariate anomaly detection, sending alerts through multiple channels, and diagnosing the root cause of anomalous incidents. Azure Metrics Advisor works great in streaming scenarios, such as methane leak detection, where detecting anomalies in real-time is critical.  It allows the detection of spikes, dips, deviations from cyclic patterns, and trend changes through both univariate and multivariate anomaly detection APIs.

# Data ingestion and processing
The first step is to deploy methane sensors oil and gas facilities such as pipelines, storage tanks, and compressors, in addition to sensors that measure other atmospheric variables such as wind speed, wind direction, temperature, and relative humidity (in this demo, Bob only uses **methane concentration** and **temperature**). These sensors can be placed optimally, using a machine learning framework developed by Microsoft, that aims to maximize detection of possible methane leaks with a limited sensor budget. Once the sensors are deployed, Azure IoT Hub can be used to regularly communicate with the sensors and ingest the data into a data store on Azure such as Azure SQL database, Azure Data Explorer (ADX), or Azure CosmosDB. An example architecture diagram is shown below.

![methane architecture](/media/methane-architecture.png)

# Data onboarding to Metrics Advisor

Like all Azure services, Bob first goes to Azure to create a Metrics Advisor resource.
Then he goes to the portal of Metrics Advisor. From there, he selects his instance of Metrics Advisor web-based workspace and jumps into it.

Once the data is flowing to the data store, a data feed can be set up in   to onboard the data into Metrics Advisor and unlock many of the powerful capabilities the Azure Metrics Advisor provides. Azure Metrics Advisor can authenticate and pull data from a variety of data sources such as Azure Blob Storage, Azure CosmosDB, Azure SQL database, and PostgreSQL.

Now Bob's going to onboard the time series data for both the **methane concentration** and **temperature**, which are from 2 devices.

To onboard the data, Bob selected the `source type` as Azure Data Explorer(Kusto), set the `granularity` and `Ingest data since` based on his data.
![onboard data](/media/onboard-data.png)

Then Bob sets the right metric schema and a few additional configurations before submitting the data feed. The **methane concentration** and **temperature** are two essential metrics that need to be monitored on, so they are selected as *measure*, while the device is a categorical variable, so it's selected as *dimension*.

![onboarding configuration](/media/data_onboarding_configuration.png)


# Fine tune configuration
Next, is to tune the models to ensure they detect anomalies as expected.
The knowledge of what values of the parameters that works for the data come from the proof of concept stage before production usage.

During that stage, Bob's team has run some validation on a relatively small, but representative dataset and got the best parameter value that works with the sample dataset for the best tradeoff between precision and recall.
They apply those configurations to the production data and are ready to further fine tune the parameters in case the production data results deviate from the POC results.

![set_configuration](/media/methane-anomaly-detection.png)

With that, Bob could set up alerting on instance, which enables Teams alerts for metrics onboard.

![setup_hooks](/media/methane_hook_setup.png)

# Diagnose from an incident

For the anomalies that have been detected, Bob checks the details behind this anomaly through the **incident** in the metric page.

![incident](/media/methane_incident.png)

In **Incident Hub**, which is a place that allows Bob to see an overview of all the latest detected anomalies in real-time and see their severity scores, also to diagnose and analyze the root cause of each incident. Bob now finds that there are 3 alerts from the methane concentration metric and he could easily know the timestamp when these happened.

![incident_hub](/media/methane_incident_hub.png)

Bob clicks one incident in the **Incident list** down below to see the more detail of a specific incident.

![incident_detail](/media/methane_incident_details.png)

### Outcome
By just a few clicks and going through the automatic diagnostic information in a couple of minutes, Bob can quickly find the anomaly and take mitigated actions to avoid further impact. 
With Metrics Advisor, Bob also receives other alerts from Metrics Advisor in Teams, and he'll no longer miss the severe methane emission case anymore.
Now, this is definitely making Bob's life much easier.

Compared with traditional way, it saves **95%** time to discover and mitigate one issue, which could avoid **thousands of dollars** revenue loss, most important, this will save lives. At the same time, the company has managed to provide **a robust service** which wins customer's trust and empowers bigger impact. 

Recently, Bob is also looking to customize a platform to connect deeply with their other tools. Luckily, Metrics Advisor has brought all capabilities with its web UI, as well as a rich set of rest APIs, SDK libraries in Java, JavaScript, .NET, and Python, that can make coding as a service, much easier.