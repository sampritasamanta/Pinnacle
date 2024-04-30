from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('Customer Support Bot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english')

# Start the conversation loop
print("Welcome to Customer Support Bot. How can I assist you today?")
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)
