'''
Here we test the basic setup for spark.
If it succeeds, Hurray
'''


def runSpark():
    '''
    The Spark PI examplte to test the installation
    it is expected that it fails, with an exception
    :return:
    '''


    import sys
    from random import random
    from operator import add

    from pyspark.sql import SparkSession

    # Create a SparkSession
    spark = SparkSession \
        .builder \
        .appName("PythonPi") \
        .config("spark.driver.cores", 2) \
        .master("local[2]") \
        .getOrCreate()

    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * partitions


    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0


    count = spark.sparkContext.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))

    spark.stop()
