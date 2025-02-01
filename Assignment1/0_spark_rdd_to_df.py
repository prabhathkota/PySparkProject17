from utils import get_spark_session
from pyspark.sql.functions import col
from pyspark.sql import Row

def main():
    spark = get_spark_session(env='DEV', app_name='rdd_to_df')
    print(spark)

    # =============================================
    # List of tuples
    data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]

    # Create RDD
    rdd = spark.sparkContext.parallelize(data)

    df = rdd.toDF(["Name", "Age"])
    df.show()

    #=============================================
    data1 = list(range(1,11))
    print(data1)

    # rdd0 = spark.sparkContext.parallelize(data1)
    # df0 = rdd0.toDF(["Num"])
    # df0.show()

    rdd1 = spark.sparkContext.parallelize(data1)
    rdd11 = rdd1.map(lambda x: (x,))
    df1 = rdd11.toDF(["Num"])
    df1.show()

    # Show the DataFrame
    df1.filter(col("Num") > 5).show()

    # =============================================
    data2 = [Row(Name="Alice", Age=25), Row(Name="Bob", Age=30), Row(Name="Cathy", Age=28)]

    rdd2 = spark.sparkContext.parallelize(data2)
    df2 = rdd2.toDF()
    df2.show()



if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""