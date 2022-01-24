import pyspark
from pyspark.sql import SparkSession
#Here I instantiate the spark session
spark = SparkSession.builder.appName('Analyzing').getOrCreate()
print(spark)