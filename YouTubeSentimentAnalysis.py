#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:32:36 2024

@author: indiramallela
"""

import os
import googleapiclient.discovery
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Preload the VADER sentiment lexicon
nltk.download('vader_lexicon', quiet=True)

# API key and video ID
api_key = "AIzaSyD94bGpAplpOjnBgFoohuOt4fUlqOAO5qM"
video_id = "npfahtvaWOk"
# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Create the API service object
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyD94bGpAplpOjnBgFoohuOt4fUlqOAO5qM"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

# Request comments from YouTube API
request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    fields="items/snippet/topLevelComment/snippet/textDisplay",
    maxResults=100
)
response = request.execute()

# Store the sentiment scores for each comment
sentiment_scores = []

for comment in response["items"]:
    text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    sentiment_score = sia.polarity_scores(text)["compound"]
    sentiment_scores.append(sentiment_score)

# Calculate the average sentiment score
average_sentiment_score = sum(sentiment_scores) / len(sentiment_scores)

# Print the average sentiment score
print("Average Sentiment Score:", average_sentiment_score)
