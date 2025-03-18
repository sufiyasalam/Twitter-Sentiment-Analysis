# Twitter-Sentiment-Analysis

## Overview
This project analyzes Twitter sentiment using IBM Watson NLP and Apache Spark. It classifies tweets into Positive, Neutral, and Negative sentiments.

## Features
- Extract tweets using the Twitter API.
- Perform sentiment analysis with IBM Watson NLP.
- Process data using Apache Spark.
- Visualize results with word clouds and statistical graphs.

## Prerequisites
- Python 3.x
- IBM Watson NLP SDK
- Apache Spark
- Twitter Developer Account & API Keys

## Setup Instructions
1. Clone the repository:
git clone https://github.com/sufiyasalam/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis

2. Install dependencies:
pip install -r requirements.txt

3. Configure Twitter API keys in a `.env` file:
- API_KEY=your_api_key
- API_SECRET=your_api_secret
- ACCESS_TOKEN=your_access_token
- ACCESS_SECRET=your_access_secret
- BEARER_TOKEN=your_bearer_token

4. Run the sentiment analysis: python analyze_sentiments.py

## Results
- Generates sentiment-based word clouds.
- Provides insights into tweet sentiment distribution.

## License
This project is open-source and licensed under the MIT License.

   
