import json
import random
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import numpy as np

# Download punkt tokenizer if not already downloaded
nltk.download('punkt')

# Load intents
with open('intents.json') as f:
    data = json.load(f)

# Prepare corpus and tags for TF-IDF
corpus = []
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        tags.append(intent['tag'])

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
X = vectorizer.fit_transform(corpus)

# Function to get chatbot response + sentiment
def get_response(user_input):
    # Vectorize user input
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)
    idx = np.argmax(similarities)

    # If similarity is too low, return default message
    if similarities[0][idx] < 0.2:
        response = "Sorry, I don't understand the question. Can you rephrase?"
    else:
        tag = tags[idx]
        for intent in data['intents']:
            if intent['tag'] == tag:
                response = random.choice(intent['responses'])

    # Sentiment analysis
    sentiment = TextBlob(user_input).sentiment.polarity
    if sentiment > 0.1:
        sentiment_response = " 😊 I'm glad to hear that!"
    elif sentiment < -0.1:
        sentiment_response = " 😔 I'm sorry to hear that."
    else:
        sentiment_response = ""

    return response + sentiment_response