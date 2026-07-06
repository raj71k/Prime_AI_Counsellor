from chatbot.prompt_manager import PromptManager
from chatbot.conversation_engine import ConversationEngine

bot = ConversationEngine()

question = input("Student: ")

answer = bot.chat(question)

print("\nAI:\n")
print(answer)