from pyspark.sql import SparkSession


def get_spark_session(env, app_name):
    if env == 'DEV':
        spark = SparkSession. \
            builder. \
            config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4").\
            master('local'). \
            appName(app_name). \
            getOrCreate()
        return spark
    return