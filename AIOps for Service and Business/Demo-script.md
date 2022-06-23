# Context and customer pain-points
Let's meet Joe, who is the CEO of an e-commerce company which sells a wide range of products.
The company is totally data driven, lots of telemetries are logged and monitored actively. From business critical metrics such as 'Cost/Revenue', 'Daily active users' of the website, to service performance metrics like 'Page load time' and 'Cache hit rate' are all been logged and stored in a relational database.
It's been a great pain-point that even has tons of telemetries collected, it's still hard to run the business smoothly. They've tried to monitor those metrics via static rules and thresholds. 
But eventually gave up, because of alert fatigue. Additionally, every time if there's any issue, it's either been missed and caused great impact, or it costs tons of time to find the root cause of the issue. The distresses hurt customer experiences a lot and lead to huge business loss.
Take use of the telemetries effectively and get all pieces run together is crucial to business success. 

# How Metrics Advisor helps
Joe's company has taken Metrics Advisor as their business monitoring solution. Sam who manages the IT department of the company onboarded all telemetries to Metrics Advisor. 
Like all Azure services, Sam first goes to Azure to create a Metrics Advisor resource.
Then he goes to the portal of Metrics Advisor. From there, he selects his instance of Metrics Advisor web-based workspace and jumps into it.
Now Sam's going to onboard the time series data for both the business metrics and service telemetries.
Take business metrics as an example, to onboard cost/revenue metrics, firstly set the correct source type, granularity and ingestion start time, as well as the connection information and the query.
Then set the right metric schema and a few additional configurations before submitting the data feed.

Note that the 'category' column and the 'region' column are set as dimensions, as that could enable the platform to monitor the cost/revenue from all different region & category combinations, and diagnose easily when there is an issue.
An aggregation rule is also specified so that Metrics Advisor will roll up the two dimensions automatically and a monitor that cost/revenue from aggregated region and category.

# Fine tune configurations
Next, is to tune the models to ensure they detect anomalies as expected.
The knowledge of what values of the parameters that works for the data come from the proof of concept stage before production usage.

During that stage, Sam's team has run some validation on a relatively small, but representative dataset and got the best parameter value that works with the sample dataset for the best tradeoff between precision and recall.
They apply those configurations to the production data and are ready to further fine tune the parameters in case the production data results deviate from the POC results.
With that, Sam could set up alerting on instance, which enables e-mail alerts for metrics onboarded.

After successfully onboarded business metrics, Sam also onboarded telemetries collected from the infrastructure of the e-commerce website.

# Root cause analysis 
In order to best root cause issues, Sam, could build a simple metrics graph to describe the dependencies between the whole pipeline components. From high-level financial metrics, to website service components and also pipeline running status. One or multiple graph could be built to help orchestrate the related metrics and also provide fuel to 
automatic root cause analysis provided by Metrics Advisor.
What he did was to simply depict the dependencies between different time series based on his knowledge of the system architecture and his knowledge of what really contributes directly to each other.

For example, DAU is dependent on latency of the Front Door Web App, which is dependent on the database throughput, which is dependent on disk I/O and the CPU.

# Diagnose from an incident
Now it's all set. Let's give it a go and see what it can do.
On xx month yy day, the business manager Joe, receives an alert that the overall Revenue has a significant drop. He clicks on the anomaly that detected on **'region=SUM' and 'category=SUM'**, and chooses **'To incident hub'**, then he is directed to the incident analysis page.

### Pinpoint issue into specific dimension
In the incident diagnostic page, Joe quickly goes through the current abnormal status at the beginning and checks the 'Analyzed root cause' part, which is automatically analyzed by the system. It helps quickly pinpoint the issue into specific dimension of 'region=Karachi' and 'category=SUM'. Then he gets to know the most potential root cause. 
Joe can further confirm this by slicing and dicing on the 'dimension tree', where he can view all the anomaly status on different dimensions, either to double confirm the automatic analysis or evaluate on the issue impact.

### Further analyze root cause using metrics graph
After locating into specific dimension, Joe can further analyze the root cause using the metrics graph that created before. Metrics Advisor will do the automatic anomaly correlation across multiple metrics within the graph and provide additional insights to find the eventual root cause. 
In this issue, the service has correlated another anomaly captured on 'DAU', which shows a significant drop at the same time. What's more, for the located dimension 'region=Karachi & category=SUM', the service has automatically correlated two anomalies on 'Cache Hit Rate' and 'Page Load Time', which show a significant drop and spike respectively. 

By consolidating above metrics, Joe can easily pinpoint the root cause is due to the low cache hit rate on Karachi region, which leads to a high page load time and impacts the end customer's experience. Then the engagement drop eventually causes the revenue decrease. He can work with Sam to take action quickly, mitigate the customer impact and stop losing money immediately.

### Outcomes
By just a few clicks and going through the automatic diagnostic information in a couple of minutes, Joe and Sam can quickly find the root cause of the issue and take mitigated actions to avoid further impact. 
Joe was super grateful for Sam's quick turn around and actually, Sam went above and beyond what Joe knew. With Metrics Advisor, Sam also receives other alerts from the infrastructure data that Sam's team had taken preventive actions to those infrastructural influence before they make serious impact to business.
Now, this is definitely making Joe's life much easier.

Compared with traditional way, it saves **95%** time to discover and mitigate one issue, which could avoid **thousands of dollars** revenue loss. But more importantly, the company has managed to provide **a robust service** which wins customer's trust and empowers bigger **business growth**. 

Recently, Sam is looking to customize a platform to connect deeply with their other tools. Luckily, Metrics Advisor has brought all capabilities with its web UI, as well as a rich set of rest APIs, SDK libraries in Java, JavaScript, .NET, and Python, that can make coding as a service, much easier.
