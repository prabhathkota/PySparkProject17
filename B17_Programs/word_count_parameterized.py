from pyspark import SparkContext, SparkConf
import sys

if __name__ == '__main__':
    sc = SparkContext("local", "word count b17")
    input_file_param = sys.argv[1]
    output_file_param = sys.argv[2]

    #read text file and split each line into words
    #hadoop,1
    #pyspark,1
    #hadoop,1
    #D:\\BigData\\training\\input\\input.txt
    input_file = f"file:////D://BigData//training//input//{input_file_param}"
    output_file = f"file:////D://BigData//training//outfile//{output_file_param}"
    print(input_file)
    print(output_file)

    #file: // // D: // BigData // training // input // wc_input.txt
    #file: // // D: // BigData // training // outfile // wc_output2

    #sys.exit()
    lines = sc.textFile(input_file)
    print(lines.collect())
    #['In today’s data-driven world, handling massive volumes of data efficiently is crucial. ',
    # 'PySpark, the Python library for Apache Spark,

    words_flat = lines.flatMap(lambda x: x.split(" "))
    print(words_flat.collect())
    #['In', 'today’s', 'data-driven', 'world,', 'handling', 'massive'

    words_map_tuple = words_flat.map(lambda x: (x,1))
    print(words_map_tuple.collect())
    #[('In', 1), ('today’s', 1), ('data-driven', 1), ('world,', 1),

    words_count = words_map_tuple.reduceByKey(lambda a,b: a+b)
    print(words_count.collect())
    #[('In', 1), ('today’s', 1), ('data-driven', 1), ('world,', 1), ('handling', 1),
    # ('massive', 1), ('volumes', 1), ('of', 3), ('data', 9),

    words_count.saveAsTextFile(output_file)
    print("File written successfully")