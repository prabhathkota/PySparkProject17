from pyspark import SparkContext, SparkConf

if __name__ == '__main__':
    sc = SparkContext("local", "word count b17")

    #read text file and split each line into words
    #hadoop,1
    #pyspark,1
    #hadoop,1
    #D:\\BigData\\training\\input\\input.txt

    lines = sc.textFile("file:////D://BigData//training//input//wc_input.txt")
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

    words_count.saveAsTextFile("file:////D://BigData//training//output//wc_output")