import random

print("🤖 Welcome to my Rule-Based AI Chatbot!")
print("Type 'bye' or 'exit' to end the conversation.")

while True:
    message = input("You: ").lower().strip()

    if message in ["hi", "hello", "hey"]:
        responses = [
            "Hello! How can I help you?",
            "Hi there! Nice to meet you!",
            "Hey! What can I do for you?"
        ]
        print("Bot:", random.choice(responses))

    elif "what can you do" in message:
        print("Bot: I can answer simple questions using predefined rules.")

    elif "help" in message:
        print("Bot: You can say hello, ask what I can do, or say bye to exit.")

    elif message in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")