# Databricks notebook source
print("Module2 - Setup Delta Tables")

# COMMAND ----------

# MAGIC %sql
# MAGIC create table employeeCTAS AS select * from employee

# COMMAND ----------

# MAGIC %sql SHOW TABLES

# COMMAND ----------

# MAGIC %sql describe detail employeectas

# COMMAND ----------

# MAGIC %sql
# MAGIC create view view_normal as select * from employee;
# MAGIC create temporary view view_temp as select * from employee;
# MAGIC create global temporary view view_globaltemp as select * from employee;

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from view_temp

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from global_temp.view_globaltemp

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in global_temp

# COMMAND ----------


