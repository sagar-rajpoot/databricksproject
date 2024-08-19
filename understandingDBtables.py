# Databricks notebook source
# MAGIC %sql
# MAGIC create table employee
# MAGIC (
# MAGIC   id int,
# MAGIC   name string,
# MAGIC   salary double
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO employee (id, name, salary)
# MAGIC VALUES (1, 'sagar', 150.20)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into employee values 
# MAGIC (2, 'sandeep',120.20),
# MAGIC (3, 'Nita' , 100.35),
# MAGIC (4, 'shilpi', 85.40)

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE Detail employee

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history employee

# COMMAND ----------

# MAGIC %sql
# MAGIC update employee
# MAGIC set salary = salary + 50
# MAGIC where name = 'Nita' 

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history employee

# COMMAND ----------

# MAGIC %sql
# MAGIC Describe detail employee

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history employee

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from employee version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from employee

# COMMAND ----------

# MAGIC %sql 
# MAGIC describe history employee

# COMMAND ----------

# MAGIC %sql
# MAGIC restore table employee to version as of 4

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from employee

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history employee

# COMMAND ----------


