from doctest import master
from pyspark.sql import SparkSession
import logging, sys

def get_spark_session(env='DEV', app_name=''):
    if env == 'DEV':
        master_var = 'local'
    else:
        master_var = 'yarn'
    spark = SparkSession. \
        builder. \
        master(master_var). \
        appName(app_name). \
        getOrCreate()
    return spark

def create_dataframe(spark, schema, data):
    """
    Creates a PySpark DataFrame.

    :param spark: SparkSession object
    :param schema: Schema for the DataFrame (StructType)
    :param data: List of tuples representing rows of data
    :return: PySpark DataFrame
    """
    return spark.createDataFrame(data=data, schema=schema)

def set_logging():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    logger = logging.getLogger("PySparkApp")
    return logger