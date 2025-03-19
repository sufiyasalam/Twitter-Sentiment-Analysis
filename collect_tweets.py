import tweepy
import json

# 🔹 Replace these values with your actual Twitter Developer credentials
BEARER_TOKEN = "your_bearer_token"
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# ✅ Method 1: Authenticate using Bearer Token (Recommended for API v2)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# ✅ Method 2: Authenticate using API Key, API Secret, Access Token, and Access Token Secret
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# 🔍 Define search query (fetch tweets about IBM Cloud)
query = "IBM Cloud -is:retweet lang:en"  # Excluding retweets

# 🔹 Fetch tweets (max 100)
tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["text"])

# Extract tweet texts
tweet_texts = [tweet.text for tweet in tweets.data] if tweets.data else []

# 💾 Save tweets to JSON file
with open("tweets.json", "w", encoding="utf-8") as f:
    json.dump(tweet_texts, f, indent=4, ensure_ascii=False)

print("✅ Tweets collected successfully!")
