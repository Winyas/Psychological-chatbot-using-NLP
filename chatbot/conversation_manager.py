from collections import defaultdict
import time

class ConversationManager:
    def __init__(self):
        # Dictionary to store conversations
        # Format: {conversation_id: [{'role': 'user'/'bot', 'message': '...', 'timestamp': ...}, ...]}
        self.conversations = defaultdict(list)
        
        # Maximum conversation history to maintain
        self.max_history = 10
    
    def add_user_message(self, conversation_id, message):
        """Add a user message to the conversation history"""
        self.conversations[conversation_id].append({
            'role': 'user',
            'message': message,
            'timestamp': time.time()
        })
        
        # Trim conversation if it exceeds max history
        if len(self.conversations[conversation_id]) > self.max_history * 2:  # *2 because we count both user and bot messages
            self.conversations[conversation_id] = self.conversations[conversation_id][-self.max_history * 2:]
    
    def add_bot_message(self, conversation_id, message):
        """Add a bot message to the conversation history"""
        self.conversations[conversation_id].append({
            'role': 'bot',
            'message': message,
            'timestamp': time.time()
        })
    
    def get_conversation(self, conversation_id):
        """Get the full conversation history for a given ID"""
        return self.conversations.get(conversation_id, [])
    
    def get_last_n_exchanges(self, conversation_id, n=3):
        """Get the last n exchanges (user-bot pairs) from the conversation"""
        conversation = self.conversations.get(conversation_id, [])
        # Return at most the last n*2 messages (n user-bot pairs)
        return conversation[-n*2:] if conversation else []
    
    def clear_conversation(self, conversation_id):
        """Clear the conversation history for a given ID"""
        if conversation_id in self.conversations:
            del self.conversations[conversation_id]
