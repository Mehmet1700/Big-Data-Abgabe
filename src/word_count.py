from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Read input data from the test file
text_file = spark.read.text("test.txt")

# Perform transformations and count words
word_counts = text_file.rdd.flatMap(lambda line: line[0].split(" ")) \
                         .map(lambda word: (word, 1)) \
                         .reduceByKey(lambda a, b: a + b)

# Save the word counts to an output file (optional)
word_counts.saveAsTextFile("word_counts_output")

# Print the word counts
print("Word Counts:")
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop the SparkSession
spark.stop()
