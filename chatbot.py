def get_response(user_input):
    """Return a predefined reply based on user input."""
    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hi! 👋 How can I help you today?"

    elif "how are you" in user_input or "how r you" in user_input:
        return "I'm fine, thanks! 😊 How about you?"

    elif "good" in user_input or "fine" in user_input or "great" in user_input:
        return "That's wonderful to hear! 😄"

    elif "bad" in user_input or "sad" in user_input or "not good" in user_input:
        return "Oh no, I'm sorry to hear that. 😔 I hope things get better!"

    elif "your name" in user_input or "who are you" in user_input:
        return "I'm ChatBot 🤖, your simple rule-based assistant!"

    elif "what can you do" in user_input or "help" in user_input:
        return ("I can chat with you! Try saying:\n"
                "  - hello / hi\n"
                "  - how are you\n"
                "  - what is your name\n"
                "  - joke\n"
                "  - time\n"
                "  - bye")

    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? 🌙\nBecause light attracts bugs! 🐛😄"

    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰"

    elif "bye" in user_input or "goodbye" in user_input or "exit" in user_input:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Hmm, I didn't understand that. 🤔 Type 'help' to see what I can do."


def chatbot():
    """Main chatbot loop."""
    print("=" * 40)
    print("       Welcome to ChatBot 🤖")
    print("=" * 40)
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("ChatBot: Please say something!\n")
            continue

        response = get_response(user_input)
        print(f"ChatBot: {response}\n")

        # Exit if user says bye
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit"]):
            break


if __name__ == "__main__":
    chatbot()
