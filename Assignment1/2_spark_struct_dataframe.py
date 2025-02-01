import os, sys
from utils import get_spark_session, create_dataframe
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
#from pyspark.sql.types import *

def main():
    spark = get_spark_session(env='DEV', app_name='df_struct_with_schema')
    #print(spark)
    #spark.sql('SELECT current_date').show()

    schema = StructType([
        StructField("Name", StringType(), True),
        StructField("Age", IntegerType(), True),
        StructField("City", StringType(), True)
    ])

    # Example data
    data = [
        ("Alice", 25, "New York"),
        ("Bob", 30, "San Francisco"),
        ("Cathy", 28, "Los Angeles")
    ]

    df_struct = create_dataframe(spark, schema, data)
    df_struct.show()

if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""