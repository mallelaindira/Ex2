# YouTube Comment Sentiment Analysis

## Introduction
This Python script retrieves comments from a YouTube video using the YouTube Data API v3 and performs sentiment analysis on the comments using the VADER sentiment lexicon from NLTK (Natural Language Toolkit). The average sentiment score of the comments is then calculated.

## Prerequisites
- You need to have a Google Cloud Platform (GCP) project with the YouTube Data API v3 enabled. Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).
- Ensure you have NLTK (Natural Language Toolkit) installed. You can install it using `pip install nltk`.

## Code Explanation https://www.youtube.com/watch?v=tRLbQU3TQdQ

### Imports
```python
import os
import googleapiclient.discovery
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk



