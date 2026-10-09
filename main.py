"""CodeAlpha Task 4: Basic Rule-Based Chatbot"""


def get_reply(message: str) -> str:
    """Return a response based on simple keyword/rule matching."""
    text = message.strip().lower()

    if text in {"hello", "hi", "hey", "hello there"}:
        return "Hi! Nice to meet you. How can I help?"
    if "how are you" in text:
        return "I'm fine, thanks! How are you?"
    if "your name" in text or "who are you" in text:
        return "I'm CodeAlpha Bot, a simple rule-based chatbot."
    if "help" in text:
        return "You can greet me, ask how I am, ask my name, or say bye."
    if text in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Have a great day!"
    if "thank" in text:
        return "You're welcome!"
    if "time" in text:
        from datetime import datetime
        return f"The current system time is {datetime.now().strftime('%I:%M %p')}."
    return "I'm not sure how to respond to that yet. Type 'help' to see what I understand."


def main() -> None:
    print("=" * 46)
    print("       CODEALPHA RULE-BASED CHATBOT")
    print("=" * 46)
    print("Bot: Hello! Type 'help' for ideas or 'bye' to exit.")

    while True:
        try:
            user_message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        reply = get_reply(user_message)
        print(f"Bot: {reply}")

        if user_message.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
