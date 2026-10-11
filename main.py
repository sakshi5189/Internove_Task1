"""Run all demos:  python main.py"""
from src import spam_classifier, digit_neural_network, rule_based_chatbot

print("=== Demo 1: Rule-based AI (chatbot) ===")
for q in ["Hi", "What is AI?", "Tell me about deep learning", "What's the weather?"]:
    print(f"You: {q}\nBot: {rule_based_chatbot.reply(q)}")

print("\n=== Demo 2: Machine Learning (spam detector) ===")
spam_classifier.main()

print("\n=== Demo 3: Deep Learning (neural network) ===")
digit_neural_network.main()
