
# DecodeLabs | Batch 2026 | Project 1
# Rule-Based AI Chatbot
# Author: [Alishba Ghulam Rasool]

print("------------------------------------------")
print("DecoBot is running! Type 'exit' to quit.")
print("------------------------------------------")

while True:

    user_input = input("You: ")
    user_input = user_input.lower().strip()

    if user_input == "exit" or user_input == "quit" or user_input == "bye":
        print("DecoBot: Goodbye! See you next time!")
        break

    elif user_input == "hello" or user_input == "hi" or user_input == "hey" or user_input == "hii":
        print("DecoBot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("DecoBot: I am doing great, thank you for asking!")

    elif user_input == "what is your name":
        print("DecoBot: My name is DecoBot!")

    elif user_input == "who are you":
        print("DecoBot: My name is DecoBot!I am an AI chatbot .")

    elif user_input == "what is ai":
        print("DecoBot: AI stands for Artificial Intelligence. It means making machines think like humans.")

    elif user_input == "what is python":
        print("DecoBot: Python is a programming language. It is used for AI, web development, and data science.")

    elif user_input == "who made you":
        print("DecoBot: I was made by an intern named Alishba at DecodeLabs!")

    elif user_input == "tell me a joke":
        print("DecoBot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif user_input == "Good Morning "  or user_input =="good morning":
         print("DecoBot: Good Morning! have a lovely day")     
    
    elif user_input == "good afternoon":
        print("DecoBot: Good Afternoon! Hope your day is going great!")

    elif user_input == "good evening":
        print("DecoBot: Good Evening! How was your day?")

    elif user_input == "good night":
        print("DecoBot: Good Night! Sleep well and sweet dreams!")

    elif user_input == "thanks" or user_input == "thank you":
        print("DecoBot: You're welcome! Happy to help.")

    elif user_input == "nice to meet you":
        print("DecoBot: Nice to meet you too!")

    elif user_input == "how is your day":
        print("DecoBot: My day is going great! Thanks for asking.")

    elif user_input == "welcome":
        print("DecoBot: Thank you!")

    elif user_input == "what's up" or user_input == "whats up":
        print("DecoBot: Not much! Just waiting to chat with you.")

    elif user_input == "have a nice day":
        print("DecoBot: Thank you! You have a nice day too.")

    elif user_input == "bye bye":
        print("DecoBot: Bye bye! Take care.")

    elif user_input == "good to see you":
        print("DecoBot: It's good to see you too!")

    elif user_input == "Help":
        print("DecoBot: I can Answer simple questions")  
        
    elif user_input == "are you there":
        print("DecoBot: Yes, I'm here and ready to help!")

    elif user_input == "how can you help me":
        print("DecoBot: I can answer simple questions about AI, Python, greetings, and more.")

    else:
        print("DecoBot: Sorry, I don't understand that. Try asking something else!")
