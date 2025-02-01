import os, sys
from utils import get_spark_session, create_dataframe


def main():
    spark = get_spark_session(env='DEV', app_name='dict_to_df')
    print(spark)

    # List of tuples
    data1 = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]

    # List of dictionaries
    data = [
        {"Name": "Alice", "Age": 25},
        {"Name": "Bob", "Age": 30},
        {"Name": "Cathy", "Age": 28}
    ]

    # Create DataFrame
    df = spark.createDataFrame(data)

    # Show the DataFrame
    df.show()

if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
"""