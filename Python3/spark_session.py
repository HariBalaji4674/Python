from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Hari") \
    .config("spark.hadoop.native.lib", "false") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")  # Suppress warnings
