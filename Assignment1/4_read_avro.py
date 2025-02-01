import logging
import os, sys

from pyspark.sql import SparkSession
from utils import get_spark_session, set_logging


def main():
    spark = get_spark_session(env='DEV', app_name='read_avro')
    #https://mvnrepository.com/artifact/com.databricks/spark-avro_2.11/4.0.0
    logger = set_logging()

    # spark = SparkSession.builder \
    #     .appName("AvroExample") \
    #     .config("spark.jars.packages", "org.apache.spark:spark-avro_2.11:4.0.0") \
    #     .getOrCreate()

    df = spark.read.format('avro').load("file:///D://workspace//data//part-00000-12a6a823-993e-417f-a13a-b6afc6d8c0ce-c000.avro")
    df.show()
    # | empid | emp_name | designation | skills_date |
    # | 101 | SaiMidhun | Spark_Developer | Hadoop |

    df.printSchema()
    logger.info(f"Count: {df.count()}")
    logger.info(df.dtypes)

if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""