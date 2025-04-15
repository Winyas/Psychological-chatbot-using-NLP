# Psychological Support Chatbot

A chatbot that uses Natural Language Processing (NLP) to detect emotions in user messages and provide appropriate psychological support responses.

## Features

- **Emotion Detection**: Analyzes user input to identify emotions such as joy, sadness, anger, fear, surprise, and disgust.
- **Contextual Responses**: Generates responses tailored to the detected emotion.
- **Conversation Management**: Maintains conversation history to provide more coherent interactions.
- **Web Interface**: Simple and intuitive user interface for chatting with the bot.

## Technologies Used

- **Python**: Core programming language
- **Flask**: Web framework for the application
- **NLTK**: Natural Language Toolkit for text processing
- **TextBlob**: Library for sentiment analysis
- **HTML/CSS/JavaScript**: Frontend web interface

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd chatbot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## How It Works

1. **Emotion Detection**: The chatbot analyzes the user's message using a combination of keyword matching and sentiment analysis to identify the underlying emotion.

2. **Response Generation**: Based on the detected emotion, the chatbot selects an appropriate response from its template library, designed to provide psychological support.

3. **Conversation Flow**: The chatbot maintains context by storing the conversation history, allowing for more coherent and meaningful interactions.

## Project Structure

- `app.py`: Main application file with Flask web server
- `emotion_detector.py`: Module for detecting emotions in text
- `response_generator.py`: Module for generating appropriate responses
- `conversation_manager.py`: Module for managing conversation flow
- `templates/index.html`: HTML template for the web interface
- `static/css/style.css`: CSS for styling the web interface
- `static/js/script.js`: JavaScript for handling client-side interactions

## Limitations

- The emotion detection is based on simple keyword matching and basic sentiment analysis, which may not always accurately capture the nuances of human emotions.
- The chatbot is not a replacement for professional psychological help. It is designed as a supportive tool only.
- The responses are template-based and may sometimes feel generic.

## Future Improvements

- Implement more sophisticated NLP techniques for better emotion detection
- Add machine learning models to improve response generation
- Incorporate more psychological frameworks into the response templates
- Add user authentication for personalized experiences
- Implement conversation analytics to track emotional patterns over time

## License

[MIT License](LICENSE)

## Disclaimer

This chatbot is not a substitute for professional psychological or psychiatric help. If you or someone you know is experiencing a mental health crisis, please contact a mental health professional or a crisis helpline immediately.
