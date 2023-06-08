import random
import spacy

# Load a pre-trained NLP model
nlp = spacy.load("en_core_web_sm")

# Define a list of possible responses to greetings
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Define a list of possible responses to farewell
farewell_responses = ["Goodbye!", "Farewell!", "See you later!", "Until next time!"]

# Define a function to generate a random response from a list of options
def generate_response(options_list):
    return random.choice(options_list)

# Define a function to handle chatbot responses based on user input
def chatbot_response(user_input):
    # Use the NLP model to analyze user input
    doc = nlp(user_input)
    
    # Check if user input contains a greeting
    if any(token.text.lower() in ["hello", "hi", "hey"] for token in doc):
        return generate_response(greeting_responses)
    # Check if user input contains a farewell
    elif any(token.text.lower() in ["goodbye", "bye", "see you"] for token in doc):
        return generate_response(farewell_responses)
    # Check if user input contains a question about fee payment
    elif any(token.text.lower() in ["fee", "payment", "pay"] for token in doc):
        # Ask for fee collection account number
        return "Please provide the fee collection account number to make payment."
    # Check if user input contains a fee collection account number
    elif any(token.text.lower() in ["acc", "account", "number"] for token in doc):
        # Ask for payment procedure
        return "Thank you. Would you like to make payment via bank account or mobile money?"
    # Check if user input contains a payment procedure
    elif any(token.text.lower() in ["bank", "account"] for token in doc):
        # Provide bank account number for payment
        return "Please make payment to account number XXXXXXXX at any branch of ABC Bank."
    elif any(token.text.lower() in ["mobile", "money"] for token in doc):
        # Provide mobile money account number for payment
        return "Please make payment to account number XXXXXXXX using your mobile money service provider."
    else:
        return "I'm sorry, I didn't understand that."

# Run the chatbot
print("Welcome! I'm the chatbot. How can I help you today?")
while True:
    user_input = input("You: ")
    chatbot_output = chatbot_response(user_input)
    print("Bot:", chatbot_output) 