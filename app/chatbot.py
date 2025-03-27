# app/chatbot.py
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json
import os
import random

# Download necessary NLTK packages (run once)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

class ConstructionChatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.intents = self._load_intents()
        self.stop_words = set(stopwords.words('english'))
        
    def _load_intents(self):
        # Create intents file if it doesn't exist
        intents_file = os.path.join(os.path.dirname(__file__), 'data', 'construction_intents.json')
        
        # Create the data directory if it doesn't exist
        os.makedirs(os.path.dirname(intents_file), exist_ok=True)
        
        # Check if intents file exists, if not create it with default intents
        if not os.path.exists(intents_file):
            default_intents = {
                "intents": [
                    {
                        "tag": "greeting",
                        "patterns": ["Hi", "Hello", "Hey", "How are you", "Greetings"],
                        "responses": ["Hello! How can I help with your construction questions?", 
                                     "Hi there! Ask me anything about construction.", 
                                     "Hello! I'm your construction assistant."]
                    },
                    {
                        "tag": "goodbye",
                        "patterns": ["Bye", "See you", "Goodbye", "I'm done", "Thank you"],
                        "responses": ["Goodbye! Feel free to ask more construction questions later.",
                                     "Thanks for chatting. Have a great day!",
                                     "Goodbye! Come back if you have more construction queries."]
                    },
                    {
                        "tag": "materials",
                        "patterns": ["What materials do I need", "Best materials for", "Material recommendations", "Building materials"],
                        "responses": ["Common construction materials include concrete, steel, wood, and masonry. What specifically are you building?",
                                     "Material selection depends on your project. Could you specify what you're constructing?",
                                     "For most buildings, you'll need concrete for the foundation, steel for structural support, and various finishing materials."]
                    },
                    {
                        "tag": "cost_estimation",
                        "patterns": ["How much will it cost", "Price estimate", "Budget for construction", "Project cost"],
                        "responses": ["Construction costs vary widely based on location, materials, and project scope. I'd need more details to give an estimate.",
                                     "For accurate cost estimation, consider factors like square footage, materials, labor costs, and location.",
                                     "On average, residential construction costs range from $100-200 per square foot, but this can vary significantly."]
                    },
                    {
                        "tag": "timeline",
                        "patterns": ["How long will it take", "Construction timeline", "Project duration", "Schedule for building"],
                        "responses": ["Construction timelines depend on project size and complexity. Small renovations may take weeks, while large buildings take months or years.",
                                     "Typical home construction takes 6-9 months, but weather delays and permit issues can extend this.",
                                     "Your timeline should include planning, permitting, site preparation, construction, and finishing phases."]
                    },
                    {
                        "tag": "permits",
                        "patterns": ["What permits do I need", "Building permits", "Construction permits", "Legal requirements"],
                        "responses": ["Most construction projects require building permits. Contact your local building department for specific requirements.",
                                     "Common permits include building permits, electrical permits, plumbing permits, and mechanical permits.",
                                     "Permit requirements vary by location and project type. Always check local building codes before starting construction."]
                    },
                    {
                        "tag": "contractors",
                        "patterns": ["Finding a contractor", "How to hire builders", "Good construction company", "Reliable contractors"],
                        "responses": ["When hiring contractors, look for proper licensing, insurance, good reviews, and detailed contracts.",
                                     "Get multiple quotes from different contractors and check their references and previous work.",
                                     "A good contractor should provide a detailed timeline, cost breakdown, and have clear communication."]
                    },
                    {
                        "tag": "diy",
                        "patterns": ["Can I do it myself", "DIY construction", "Self-build", "Build without contractor"],
                        "responses": ["DIY construction is possible for smaller projects, but requires knowledge, tools, and time.",
                                     "Even for DIY projects, you'll need permits and must follow building codes.",
                                     "Consider your skill level and the complexity of the project. Some aspects like electrical and plumbing might be better left to professionals."]
                    },
                    {
                        "tag": "safety",
                        "patterns": ["Construction safety", "Safe building practices", "Safety requirements", "Hazards"],
                        "responses": ["Always wear proper personal protective equipment (PPE) including hard hats, gloves, and safety glasses.",
                                     "Follow all safety guidelines, secure permits, and schedule required inspections.",
                                     "Construction sites should have clear safety protocols, first aid kits, and fire extinguishers."]
                    },
                    {
                        "tag": "unknown",
                        "patterns": [],
                        "responses": ["I'm not sure I understand your construction question. Could you rephrase?",
                                     "I don't have information on that specific construction topic. Could you ask something else?",
                                     "I'm still learning about construction. Could you ask a different question?"]
                    }
                ]
            }
            
            with open(intents_file, 'w') as f:
                json.dump(default_intents, f, indent=4)
        
        # Load intents from file
        with open(intents_file, 'r') as f:
            return json.load(f)
    
    def _preprocess_text(self, text):
        # Tokenize and lemmatize the text
        tokens = word_tokenize(text.lower())
        # Remove stop words and punctuation
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens 
                 if word.isalnum() and word not in self.stop_words]
        return tokens
    
    def _get_response(self, user_input):
        processed_input = self._preprocess_text(user_input)
        
        # Find the matching intent
        matched_intent = None
        max_matched_words = 0
        
        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                pattern_tokens = self._preprocess_text(pattern)
                # Count how many words in the pattern match the user input
                matches = sum(1 for token in processed_input if token in pattern_tokens)
                if matches > max_matched_words:
                    max_matched_words = matches
                    matched_intent = intent
        
        # If we found a match with at least one word, or it's the unknown intent
        if matched_intent:
            return random.choice(matched_intent["responses"])
        else:
            # Return a response from the "unknown" category
            for intent in self.intents["intents"]:
                if intent["tag"] == "unknown":
                    return random.choice(intent["responses"])
    
    def get_response(self, user_input):
        if not user_input:
            return "Please type a message."
        
        return self._get_response(user_input)

# Create a singleton instance
chatbot = ConstructionChatbot()