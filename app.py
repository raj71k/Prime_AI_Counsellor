from chatbot.conversation_engine import ConversationEngine

bot = ConversationEngine()

while True:

    question = input("\nStudent: ")

    if question.lower() == "exit":
        break

    answer = bot.chat(question)

    print("\nAI:")
    print(answer)