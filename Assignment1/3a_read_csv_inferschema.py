import os, sys
from utils import get_spark_session, create_dataframe
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, Row


def main():
    spark = get_spark_session(env='DEV', app_name='read_csv_wo_header')

    #custid,fname,lname,age,city,state
    #1,Richard,Hernandez,45,Brownsville,TX
    df = spark.read.csv("file:///D:\\workspace\\data\\customer_records_with_schema.csv",
                          header=True,
                          inferSchema=True)
    df.show()
    df.printSchema()
    print(f"Count: {df.count()}")
    print(df.dtypes)

if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""