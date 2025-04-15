from flask import Flask, render_template, request, jsonify
from emotion_detector import EmotionDetector
from response_generator import ResponseGenerator
from conversation_manager import ConversationManager

app = Flask(__name__)

# Initialize components
emotion_detector = EmotionDetector()
response_generator = ResponseGenerator()
conversation_manager = ConversationManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    # Process the message
    conversation_id = request.json.get('conversation_id', 'default')
    conversation_manager.add_user_message(conversation_id, user_message)
    
    # Detect emotion
    emotion = emotion_detector.detect_emotion(user_message)
    
    # Generate response
    conversation_context = conversation_manager.get_conversation(conversation_id)
    bot_response = response_generator.generate_response(user_message, emotion, conversation_context)
    
    # Save bot response
    conversation_manager.add_bot_message(conversation_id, bot_response)
    
    return jsonify({
        'response': bot_response,
        'emotion': emotion,
        'conversation_id': conversation_id
    })

if __name__ == '__main__':
    # Download necessary NLTK data
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    
    app.run(debug=True)
