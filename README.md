# AI Basics Demo

A small Python project that shows the three layers from my report *"Introduction to Artificial Intelligence"*:
**AI -> Machine Learning -> Deep Learning**.

| Demo | File | Idea |
|------|------|------|
| 1. Rule-based AI | `src/rule_based_chatbot.py` | A chatbot where a human writes every rule. No learning. |
| 2. Machine Learning | `src/spam_classifier.py` | A spam detector that learns from example messages (Naive Bayes). |
| 3. Deep Learning | `src/digit_neural_network.py` | A neural network that reads handwritten digits (0-9). |

All three are examples of **Narrow AI (ANI)**: each is good at exactly one job.

## How to run

```bash
git clone https://github.com/<your-username>/ai-basics-demo.git
cd ai-basics-demo
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py                   # runs all three demos
python src/rule_based_chatbot.py # chat with the bot yourself
```

## Sample output

```
Test accuracy on unseen messages: 83%
'Free prize waiting, click now'  ->  SPAM
'Can we study for the exam tomorrow?'  ->  NOT SPAM
Neural network accuracy on unseen digits: 98.0%
```

The digit demo also saves `outputs/digit_predictions.png`.

## What I learned

- Rule-based AI is predictable but can't handle anything its author didn't think of.
- Machine learning replaces hand-written rules with patterns learned from data.
- Deep learning (neural networks) handles complex input like images, but needs more data and computing power.
- The spam dataset is tiny, so its accuracy is only for demonstration. Real systems use thousands of messages.

## Tech used

Python 3, scikit-learn, matplotlib.
