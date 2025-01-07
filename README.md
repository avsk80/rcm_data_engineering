# rcm_data_pipeline
This project is built to serve the Finance depratment of a Hospital to improve and optimize the Revenue Cycle Management (RCM). In this project I have followed the best industry practices like medallion architecture, cofigurations driven code to build a data pipeline that is generic, idompotent, and is able to handle large-scale data. The project flow is as follows:

1) Acquire the required data such as EMR, claims (from insurer), ICD, CPT, and NPI. Here EMR data is available in Azure SQL DB; claims, and CPT are available as flat files (csv format); and NPI, and ICD codes are extracted from API.

2) Once the data is available, store it in Azure services. Here, I stored the flat files in ADLS Gen2 account, and EMR data in SQL DB, and the API extract as parquet files in ADLS Gen2.

3) Moving on, the next phase will be to build data pipeline using Azure Data Factory. I have built a ADF pipeline as shown below in the picture.

Overall process is as follows - 
1) First lookup for the config file that holds information related to what tables need to be fetched from the SQL DB and stored to bronze layer. From the configs we can set properties like is_active flag, full load or incremental, if incremental, what is the watermark column to refer to etc.

2) If the data is already available for the date then move it to archival and ingest the data to bronze.

3) Now, ingest the flat files, from landing to bronze and api extract to bronze layer (a ADLS Gen2 container).

4) After the data is available, build the Databricks notebooks that implement the logic of ingesting data from bronze to silver. Here we handle nulls, add extra columns that help us govern the data better like insert_date, modified_date etc, identify dirty and clean data as is_quaritined flag, implement SCD2 logic for the required tables.

5) From silver layer, we ingest only clean data ie. is_active = true and is_quarintined = false.

6) Based on the business logic, implement the analytical queries on the gold layer tables.

Note: All the steps are combined together in ADF activities and executed as a pipeline.

**Tech Stack used:**

Coding - Python

Azure - Data Factory, SQL DB, Gen2 storage containers, Databricks

Version control - Git
