import logging
import os, sys
from utils import get_spark_session, set_logging


def main():
    spark = get_spark_session(env='DEV', app_name='read_parquet')
    logger = set_logging()

    df = spark.read.load("file:///D://workspace//data//part-00000-a4267c6d-d25e-4a81-bc65-f3849d78b899-c000.snappy.parquet")
    #spark.read.parquet
    #spark.read.format('parquet').load
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