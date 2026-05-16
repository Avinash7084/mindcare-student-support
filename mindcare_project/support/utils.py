import nltk
import random
from nltk.tokenize import word_tokenize

# Simple Rule-Based NLP for the Chatbot
def get_chat_response(message):
    message = message.lower()

    # Define groups of keywords
    greetings = ["hi", "hello", "hey", "good morning"]
    
    # 1. Handle Greetings
    if any(word in message for word in greetings):
        return random.choice([
            "Hello! I'm your MindCare assistant. How are you feeling today?",
            "Hi there! How can I support you right now?",
            "Hey! I'm here to listen if something is on your mind.",
            "Good Morning, How are you today"
        ])
    
    # Intent mapping
    intents = {
        "exam": [
        "Don't panic about your exams. Break your syllabus into small parts.",
        "Exams are tough! Remember to stay hydrated and take short breaks.",
        "You've got this! Start with the easiest topics to build your confidence."
    ],
        "stress": [
        "I'm sorry you're feeling stressed. Try the 4-7-8 breathing technique.",
        "Take a deep breath. Stress is a sign you care, but don't let it overwhelm you.",
        "When things get heavy, try taking a 10-minute walk outside."
    ],
        "sleep": "Good sleep is vital! Try to avoid screens an hour before bed and keep a consistent wake-up time.",
        "sad": "It's okay to feel down sometimes. Have you tried talking to a friend or writing your thoughts in a journal?",
    }

    # Basic keyword matching (can be upgraded to spaCy/Scikit-learn later)
    for key in intents:
        if key in message:
            return intents[key]
    
    return "I'm not sure I fully understand, but I'm here. Could you tell me more about what's bothering you?"

# Assessment Scoring Logic
def calculate_mental_health_metrics(answers):
    """
    Expects a list of integers (0-3 scale).
    Calculates percentage based on category.
    """
    try:
        # Assuming 15 questions (0-4: Stress, 5-9: Anxiety, 10-14: Depression)
        stress_score = sum(answers[0:5])
        anxiety_score = sum(answers[5:10])
        depression_score = sum(answers[10:15])

        # Convert to percentage (max score per section is 15)
        return {
            "stress": int((stress_score / 15) * 100),
            "anxiety": int((anxiety_score / 15) * 100),
            "depression": int((depression_score / 15) * 100),
        }
    except Exception:
        return {"stress": 0, "anxiety": 0, "depression": 0}