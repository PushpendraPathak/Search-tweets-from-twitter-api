What are the risks involved in building such a pipeline? 
Ans- 
-Since
twitter api is an open source api, we should constantly monitor it for
any deprecations that might lead to problems in our runs. 
-Scraping the
data from outside network requires a proper security network which
should be enabled to avoid any security leaks or penetrations. The data
should also be sanitized if needed. 
-Load should be monitored
continuosly to check the cluster. 
-Need to check if author_id is
encrypted so that it does not disclose PII data.

How would you roll out the pipeline going from proof-of-concept to a
production-ready solution? 
Ans- There are some important points to note
when going to a production ready solution- 
-First of all, we need to
figure out the right developer account and access roles that we need in
order to query the twitter api because with current access level,
production ready solution would not be possible. 
-Currently, I have done
trial and error approach to find out the correct window size to be used
to maximize output because of access limitations. If this persists, we
need to figure out other ways to efficiently fetch data. 
-There could be
high influx of data in future and our system should be prepared for it.
-We should use secured authentication services where credentials can be
stored and changed rather than hardcoding them in the code. 
-Frameworks
to use parallel and distributed computing need to be setup to manage and
process high amounts of data. 
-The data ingestion and storage could be
done using some better formats like parquet instead of csv. 
-Since we
would know the right column names needed for business needs, we can do
right indexing for it. 
-Building and developing a CI/CD pipeline ready
code is necessary for all 3 landscapes(development, QA, Production).

What would a production-ready solution entail that a POC wouldn't? 
Ans-
There would be quite a few things that a production-ready solution will
entail that a POC wouldn't like- 
-The security aspect would be a big
factor so that no company data or access is compromised. 
-There would be
other security features added for PR pull, code merge etc. 
-The
production ready solution will entail autoscale cluster with higher
configurations to deal with the massive data processing. 
-An advanced
monitoring layer would be added on top to keep everything in control and
monitor the changes that might affect the processing. 
-An AI landscape
based UI would be provided to take a look at the output and filter them
based on the columns or other factors.

What is the level of effort required to deliver each phase of the
solution? 
Ans- 
Infrastructure setup- First thing we need to do is
identify the right framework needed for upscaling and maintaining our
system for the business needs. We also need to check and verify if the
framework is working as required, maintaining the security aspects as
well. 
-Data fetching- We need to make efforts to identify and implement
the right methodologies that extract the data from twitter api in the
most efficient and continuos way. It would lead to usage of kafka like
platforms. Load testing is to be done as well to make sure the system
does not collapse under heavy load. 
-Data processing- In this phase, we
need to develop proper recipes for the right processing needed as per
the business requirements as well as explore outliers, think of edge
cases, make sure the PII information is encrypted and to keep in mind
about deduplication of data and load testing. 
-Data Ingestion- This
phase will likely require the usage and identification of right database
and file formats in order to carry out quicker queries in future for
easy and fast retrieval. 
-CI/CD pipeline- This is a very important step
needed to be easy deployment in all three landscapes and will require a
lot of careful effort and monitoring.

What is your estimated timeline for delivery for a production-ready
solution? 
Ans- The estimated timeline for delivery would be as follows-
-Infrastructure setup- 3 weeks 
-Data fetching- 3 weeks 
-Data processing-
3 weeks 
-Data ingestion- 2 weeks 
-QA landscape validation and testing- 2
weeks 
-Production landscape validation and testing- 2 weeks 
-Production
landscape user acceptance testing- 2 weeks 
-Final enhancements from uat-
2 weeks 
Note- This timeline estimation are based on my own current
understanding of the project. However there would definitely be more
requirements and business needs and so a thorough discussion would be
required to access the needs and update the timeline accordingly.
