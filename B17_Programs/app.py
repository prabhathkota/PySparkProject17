import os, sys
from util import get_spark_session
from read import from_files


def main1():
    #env = os.environ.get('ENVIRON')
    #src_dir = os.environ.get('SRC_DIR')
    #file_pattern = f"{os.environ.get('SRC_FILE_PATTERN')}-*"
    #src_file_format = os.environ.get('SRC_FILE_FORMAT')

    env = "DEV"
    src_dir = "s3://emr-prabhath/landing/ghactivity"
    file_pattern = "2021-01-13-*"
    src_file_format = "json"
    print('*'*100)
    print(env, src_dir, file_pattern, src_file_format)
    
    print('*' * 100)
    #return
    spark = get_spark_session(env, 'GitHub Activity - Reading Data')
    df = from_files(spark, src_dir, file_pattern, src_file_format)
    df.printSchema()
    df.count()
    df.select('repo.*').show()

def main():
    #env = 'DEV'
    env = os.environ.get('ENVIRON')
    spark = get_spark_session(env, 'GitHub Activity - Getting Started')
    print(spark)
    spark.sql('SELECT current_date').show()


if __name__ == '__main__':
    main()

"""
export ENVIRON=DEV
export SRC_DIR=s3://emr-prabhath/landing/ghactivity
export SRC_FILE_PATTERN=2021-01-13
export SRC_FILE_FORMAT=json
"""