import pandas as pd
from textblob import TextBlob

# Load preprocessed tweets
df = pd.read_csv("cleaned_tweets.csv")

def get_sentiment(text):
    """Determine the sentiment of a tweet"""
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["cleaned_text"].apply(get_sentiment)


# Save results
df.to_csv("tweets_with_sentiment.csv", index=False)
print("Sentiment analysis completed and saved to 'tweets_with_sentiment.csv'!")
