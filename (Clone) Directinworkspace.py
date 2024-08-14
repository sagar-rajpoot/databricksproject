# Databricks notebook source
print("hello I am Here")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "hello from sql!"

# COMMAND ----------

# MAGIC %md
# MAGIC # text1
# MAGIC ## text2

# COMMAND ----------

# MAGIC %fs ls 'databricks-datasets'

# COMMAND ----------

dbutils.help() 

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('databricks-datasets')
display(files)

# COMMAND ----------


