import os, sys
from utils import get_spark_session, create_dataframe
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, Row


def main():
    spark = get_spark_session(env='DEV', app_name='read_csv_wo_header')

    #custid,fname,lname,age,city,state
    #1,Richard,Hernandez,45,Brownsville,TX
    schema = StructType([
        StructField("custid", IntegerType(), True),
        StructField("fname", StringType(), True),
        StructField("lname", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("city", StringType(), True),
        StructField("state", StringType(), True)
    ])

    sc = spark.sparkContext
    rdd = sc.textFile("file:///D:\\workspace\\data\\customer_records_UPD.csv")
    rdd1 = rdd.map(lambda x: x.split(','))
    rdd2 = rdd1.map(lambda x: Row(int(x[0]), x[1], x[2], int(x[3]), x[4], x[5]))

    df = spark.createDataFrame(rdd2, schema)
    df.show()

if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""