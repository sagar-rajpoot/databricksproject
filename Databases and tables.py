# Databricks notebook source
print("Module 2 - DB lakeHouse Platform- DataBases & Tables ")

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe extended employee

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema my_new_DB

# COMMAND ----------

# MAGIC %sql
# MAGIC describe database extended my_new_DB

# COMMAND ----------

# MAGIC %sql
# MAGIC use my_new_db;
# MAGIC CREATE TABLE managed_my_new_db
# MAGIC   (width INT, length INT, height INT)

# COMMAND ----------


