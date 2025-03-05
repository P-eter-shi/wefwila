import random
import re
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

class AIAssistant:
    def __init__(self, model_path=None):
        """
        Initialize the AI Assistant with optional pre-trained model
        
        :param model_path: Optional path to a pre-trained model
        """
        self.intents = self._load_intents()
        self.tokenizer = Tokenizer(oov_token="<OOV>")
        self.model = None
        
        if model_path:
            self.load_model(model_path)
        else:
            self._prepare_training_data()
            self._build_model()
    
    def _load_intents(self, file_path='intents.json'):
        """
        Load predefined conversation intents
        
        :param file_path: Path to intents JSON file
        :return: Parsed intents dictionary
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "greetings": {
                    "patterns": [
                        "hi", "hello", "hey", "greetings", 
                        "good morning", "good afternoon"
                    ],
                    "responses": [
                        "Hello! How can I help you today?", 
                        "Hi there! What can I do for you?",
                        "Greetings! I'm ready to assist you."
                    ]
                },
                "goodbye": {
                    "patterns": [
                        "bye", "goodbye", "see you later", 
                        "talk to you soon"
                    ],
                    "responses": [
                        "Goodbye! Have a great day!", 
                        "See you later!", 
                        "Take care!"
                    ]
                }
            }
    
    def _prepare_training_data(self):
        """
        Prepare training data from intents
        """
        patterns = []
        labels = []
        
        for intent, data in self.intents.items():
            for pattern in data['patterns']:
                patterns.append(pattern)
                labels.append(intent)
        
        self.tokenizer.fit_on_texts(patterns)
        sequences = self.tokenizer.texts_to_sequences(patterns)
        padded_sequences = pad_sequences(sequences, padding='post')
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            padded_sequences, 
            labels, 
            test_size=0.2, 
            random_state=42
        )
    
    def _build_model(self):
        """
        Build and compile neural network model
        """
        vocab_size = len(self.tokenizer.word_index) + 1
        
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(vocab_size, 16, input_length=self.X_train.shape[1]),
            tf.keras.layers.GlobalAveragePooling1D(),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(len(self.intents), activation='softmax')
        ])
        
        self.model.compile(
            optimizer='adam', 
            loss='sparse_categorical_crossentropy', 
            metrics=['accuracy']
        )
        
        # Convert labels to numerical format
        label_mapping = {label: idx for idx, label in enumerate(self.intents.keys())}
        y_train_numeric = np.array([label_mapping[label] for label in self.y_train])
        y_test_numeric = np.array([label_mapping[label] for label in self.y_test])
        
        # Train the model
        self.model.fit(
            self.X_train, 
            y_train_numeric, 
            epochs=50, 
            validation_data=(self.X_test, y_test_numeric),
            verbose=0
        )
    
    def predict_intent(self, text):
        """
        Predict the intent of a given text
        
        :param text: Input text to classify
        :return: Predicted intent
        """
        sequence = self.tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, padding='post', maxlen=self.X_train.shape[1])
        
        prediction = self.model.predict(padded_sequence)
        intent_idx = np.argmax(prediction)
        
        return list(self.intents.keys())[intent_idx]
    
    def get_response(self, text):
        """
        Generate a response based on input text
        
        :param text: Input text from user
        :return: Appropriate response
        """
        # Normalize input
        text = text.lower().strip()
        
        # Check for direct intent match
        for intent, data in self.intents.items():
            for pattern in data['patterns']:
                if re.search(pattern.lower(), text):
                    return random.choice(data['responses'])
        
        # Use neural network for more complex predictions
        predicted_intent = self.predict_intent(text)
        return random.choice(self.intents[predicted_intent]['responses'])
    
    def save_model(self, path='chatbot_model'):
        """
        Save the trained model
        
        :param path: Directory to save model
        """
        if self.model:
            self.model.save(path)
    
    def load_model(self, path):
        """
        Load a pre-trained model
        
        :param path: Path to saved model
        """
        self.model = tf.keras.models.load_model(path)

def main():
    chatbot = AIAssistant()
    
    print("AI Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("AI Chatbot: Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print("AI Chatbot:", response)

if __name__ == "__main__":
    main()