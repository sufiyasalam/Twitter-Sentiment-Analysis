import json
import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords
nltk.download("stopwords")
nltk.download("punkt")

# Load tweets from JSON file
with open("tweets.json", "r", encoding="utf-8") as f:
    tweets = json.load(f)

# Define stopwords
stop_words = set(stopwords.words("english"))

# Function to clean text
def clean_tweet(tweet):
    tweet = tweet.lower()  # Convert to lowercase
