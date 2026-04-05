
"""
# PySpark is the Python API for Apache Spark, an open-source distributed computing system. It allows you to perform 
# big data processing and analytics using Python. PySpark provides a high-level API for working with Spark's core features, 
# such as RDDs (Resilient Distributed Datasets), DataFrames, and SQL.

PySpark provides a powerful and flexible way to work with large datasets, enabling you to perform complex data transformations, 
machine learning, and graph processing. It is widely used in data science and big data applications for its scalability and ease of use.

"""
import os
import sys
import pyspark
from pyspark.sql import SparkSession

# Set PySpark to use the current Python executable
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Create a SparkSession
spark = SparkSession.builder.appName("PySpark Example").getOrCreate()

spark.version

