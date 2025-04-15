import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import re

class EmotionDetector:
    def __init__(self):
        # Emotion keywords dictionary
        self.emotion_keywords = {
            'joy': ['happy', 'joy', 'delighted', 'glad', 'pleased', 'excited', 'thrilled', 'content', 'satisfied', 'cheerful', 'wonderful', 'great', 'good', 'love', 'enjoy'],
            'sadness': ['sad', 'unhappy', 'depressed', 'down', 'miserable', 'heartbroken', 'gloomy', 'disappointed', 'upset', 'grief', 'sorrow', 'crying', 'tear', 'lonely', 'alone'],
            'anger': ['angry', 'mad', 'furious', 'outraged', 'annoyed', 'irritated', 'frustrated', 'enraged', 'hate', 'hostile', 'bitter', 'infuriated', 'offended', 'resent'],
            'fear': ['afraid', 'scared', 'frightened', 'terrified', 'anxious', 'worried', 'nervous', 'panic', 'terror', 'horror', 'dread', 'alarmed', 'stressed', 'concerned'],
            'surprise': ['surprised', 'amazed', 'astonished', 'shocked', 'stunned', 'startled', 'unexpected', 'wonder', 'disbelief', 'speechless', 'wow', 'unbelievable'],
            'disgust': ['disgusted', 'revolted', 'nauseated', 'repulsed', 'sickened', 'loathing', 'hate', 'dislike', 'aversion', 'repelled', 'gross', 'yuck'],
            'neutral': ['okay', 'fine', 'neutral', 'indifferent', 'so-so', 'alright', 'average']
        }
        
        # Try to download NLTK resources if not already downloaded
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
    
    def preprocess_text(self, text):
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        
        return filtered_tokens
    
    def detect_emotion(self, text):
        # Get sentiment polarity from TextBlob
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        
        # Preprocess text
        tokens = self.preprocess_text(text)
        
        # Count emotion keywords
        emotion_counts = {emotion: 0 for emotion in self.emotion_keywords}
        
        for token in tokens:
            for emotion, keywords in self.emotion_keywords.items():
                if token in keywords:
                    emotion_counts[emotion] += 1
        
        # Determine primary emotion based on keyword counts
        max_count = max(emotion_counts.values())
        if max_count > 0:
            # If there are emotion keywords, use the most frequent one
            primary_emotions = [emotion for emotion, count in emotion_counts.items() if count == max_count]
            primary_emotion = primary_emotions[0]  # In case of tie, take the first one
        else:
            # If no emotion keywords, use sentiment analysis
            if sentiment_score > 0.2:
                primary_emotion = 'joy'
            elif sentiment_score < -0.2:
                primary_emotion = 'sadness'
            else:
                primary_emotion = 'neutral'
        
        return primary_emotion
