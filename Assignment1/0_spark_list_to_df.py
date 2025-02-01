import os, sys
#import sys

from utils import get_spark_session, create_dataframe
from pyspark.sql import SparkSession

def main():
    spark = get_spark_session(env='DEV', app_name='list_to_df')
    print(spark)

    # List of tuples
    data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]

    # Create DataFrame without schema
    df = spark.createDataFrame(data, ["Name", "Age"])

    # Show the DataFrame
    df.show()

    # Using function
    df1 = create_dataframe(spark, data=data, schema=["Name", "Age"])

    df1.show()

if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""