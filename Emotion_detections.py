import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment intensity analyzer
analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    sentiment = analyzer.polarity_scores(text)
    
    if sentiment['compound'] >= 0.05:
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Test the emotion detection
text = "I am so happy right now!"
emotion = detect_emotion(text)
print(f"The emotion in the text is: {emotion}")
