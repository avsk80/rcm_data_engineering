# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS rcm_catalog.audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS rcm_catalog.audit.load_logs (
# MAGIC   data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table rcm_catalog.audit.load_logs;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from rcm_catalog.audit.load_logs;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS rcm_catalog.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS rcm_catalog.gold;

# COMMAND ----------


