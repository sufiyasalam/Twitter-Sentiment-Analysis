from pyspark.sql import SparkSession
from pyspark.sql.functions import col, size, split, count

# ✅ Initialize Spark Session
spark = SparkSession.builder.appName("TwitterSentimentAnalysis").getOrCreate()

# ✅ Load CSV from local storage
file_path = "tweets_with_sentiment_cleaned.csv"  
df_spark = spark.read.csv(file_path, header=True, inferSchema=True)

# ✅ Display basic stats
print("\n🔍 Dataset Summary:")
print(f"✅ Total Tweets: {df_spark.count()}")

# ✅ Count sentiment distribution
print("\n📊 Sentiment Distribution:")
df_spark.groupBy("Sentiment").count().show()

# ✅ Word count analysis
df_spark = df_spark.withColumn("word_count", size(split(col("cleaned_text"), " ")))

print("\n🔍 Average Word Count per Sentiment:")
df_spark.groupBy("Sentiment").agg({"word_count": "avg"}).show()
