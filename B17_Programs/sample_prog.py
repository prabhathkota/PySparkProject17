import sys
print(sys.version)
print(__name__)
from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
import time

if __name__ == "__main__":
    print("hello Spark")

    spark = SparkSession.builder.appName("RDD to DF").master("local").getOrCreate()
    sc = spark.sparkContext
    names = sc.parallelize(["test1", "test2"])
    #print(names.collect())
    spark.sparkContext.setLogLevel("Error")
    list_data_sample = [("Midhun","IT","CTS"),
                        ("Kiran","IT","HCL"),
                        ("Kishore","HR","TCS")]

    df_creation = spark.createDataFrame(list_data_sample).toDF("Name","Stream","Company")
    df_creation.show()
    df_creation.count()
    #time.sleep(1)
    #df_creation.createOrReplaceTempView('test1')
    #print("SQL -------------------------")
    #spark.sql("select * from test1").show()
    #spark.sql("select count(*) from test1").show()
    time.sleep(100)
