import random

class ResponseGenerator:
    def __init__(self):
        # Response templates based on emotions
        self.response_templates = {
            'joy': [
                "I'm glad to hear you're feeling happy! What's bringing you joy today?",
                "That's wonderful! It's great to embrace positive emotions.",
                "Your happiness is contagious! Would you like to share more about what's making you feel this way?",
                "It sounds like you're in a good place emotionally. How can we maintain this positive energy?",
                "I'm happy that you're feeling joyful! Positive emotions are worth celebrating."
            ],
            'sadness': [
                "I'm sorry to hear you're feeling down. Would you like to talk about what's troubling you?",
                "It's okay to feel sad sometimes. Remember that all emotions are valid and temporary.",
                "I'm here for you during this difficult time. What might help you feel a bit better right now?",
                "Sadness can be overwhelming, but you don't have to face it alone. Is there something specific that triggered these feelings?",
                "I notice you seem sad. Sometimes expressing our feelings can help us process them better. Would you like to share more?"
            ],
            'anger': [
                "I can sense that you're frustrated. Would it help to talk about what's bothering you?",
                "It's natural to feel angry sometimes. Taking deep breaths can help manage intense emotions.",
                "Your feelings are valid. Would you like to explore what might be triggering your anger?",
                "When we're angry, it can be helpful to step back and reflect. What do you think is at the root of these feelings?",
                "I understand you're feeling upset. Is there a specific situation that's causing these strong emotions?"
            ],
            'fear': [
                "It sounds like you're feeling anxious. Remember that you're not alone in this.",
                "Fear is a natural response to uncertainty. Would talking about your concerns help?",
                "I'm here to support you through this anxious time. What specifically are you worried about?",
                "It's okay to feel scared. Sometimes naming our fears can help reduce their power over us.",
                "Anxiety can be challenging to manage. Would you like to discuss some coping strategies?"
            ],
            'surprise': [
                "That does sound surprising! How are you processing this unexpected situation?",
                "Unexpected events can certainly catch us off guard. How are you feeling about this surprise?",
                "I can understand why you'd be surprised. Would you like to talk more about how this is affecting you?",
                "Sometimes surprises can be difficult to process. How are you adapting to this new information?",
                "That's quite unexpected! Are you feeling okay with this surprise, or is it causing you stress?"
            ],
            'disgust': [
                "It sounds like you're really put off by this situation. Would you like to talk about it?",
                "That does sound unpleasant. How are you coping with these feelings?",
                "I understand this is causing you discomfort. Is there anything that might help you feel better?",
                "It's natural to have aversions to certain things. Would you like to explore why this might be triggering such a strong reaction?",
                "I hear that you're really bothered by this. Would talking through it help process these feelings?"
            ],
            'neutral': [
                "How are you feeling today? I'm here to chat about whatever's on your mind.",
                "Is there something specific you'd like to talk about today?",
                "I'm here to support you. What's been on your mind recently?",
                "Sometimes it helps to explore our feelings a bit more. Is there anything you'd like to discuss?",
                "I'm listening and here to help. What would you like to focus on in our conversation?"
            ]
        }
        
        # General responses when no specific emotion is detected
        self.general_responses = [
            "I'm here to listen and support you. Would you like to share more?",
            "Thank you for sharing that with me. How else can I help you today?",
            "I appreciate you opening up. Is there anything specific you'd like to discuss?",
            "I'm here to chat about whatever's on your mind. What would you like to talk about?",
            "I'm listening. Please feel free to share whatever you're comfortable with."
        ]
        
        # Follow-up questions to encourage deeper conversation
        self.follow_up_questions = [
            "Could you tell me more about that?",
            "How did that make you feel?",
            "What thoughts come up for you when you experience this?",
            "Have you noticed any patterns related to when these feelings arise?",
            "What do you think might help in this situation?"
        ]
    
    def generate_response(self, user_message, emotion, conversation_context):
        # Check if this is a greeting
        greeting_keywords = ['hello', 'hi', 'hey', 'greetings', 'howdy']
        if any(greeting in user_message.lower() for greeting in greeting_keywords) and len(conversation_context) <= 2:
            return "Hello! I'm your psychological support chatbot. I'm here to listen and chat with you about how you're feeling. How are you doing today?"
        
        # Check if this is a farewell
        farewell_keywords = ['bye', 'goodbye', 'see you', 'talk to you later', 'farewell']
        if any(farewell in user_message.lower() for farewell in farewell_keywords):
            return "Thank you for chatting with me today. Remember to be kind to yourself, and I'm here whenever you need to talk. Take care!"
        
        # Generate response based on detected emotion
        if emotion in self.response_templates:
            responses = self.response_templates[emotion]
        else:
            responses = self.general_responses
        
        # Select a random response from the appropriate category
        response = random.choice(responses)
        
        # Add a follow-up question occasionally (30% chance)
        if random.random() < 0.3 and len(conversation_context) > 2:
            response += " " + random.choice(self.follow_up_questions)
        
        return response
