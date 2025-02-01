import logging
import os, sys
from utils import get_spark_session, set_logging


def main():
    spark = get_spark_session(env='DEV', app_name='read_orc')
    logger = set_logging()

    df = spark.read.format("orc").load("file:///D://workspace//data//part-00000-436f5fca-a760-4f77-a4b6-60e947c0f768-c000.snappy.orc")
    df.show()
    # | txnid | txndate | custid | amount | category | product | city | state | payment_type |
    # +-----+----------+-------+------+--------------------+--------------------+--------------+--------------+------------+
    # | 0 | 06 - 26 - 2011 | 4007024 | 40.33 | null | CardioMachineAc... | Clarksville | Tennessee | credit |

    df.printSchema()
    logger.info(f"Count ORC: {df.count()}")
    logger.info(df.dtypes)

if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""