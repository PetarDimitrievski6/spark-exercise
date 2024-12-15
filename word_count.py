from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCount").getOrCreate()

text_file = spark.sparkContext.textFile("input.txt")

word_counts = (
    text_file.flatMap(lambda line: line.split(" "))
    .map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
)

for word, count in word_counts.collect():
    print(f"{word}: {count}")

spark.stop()