def ai_response(question):
    responses = {
        "hello": "Hi there!",
        "how are you": "I'm an AI, I don't have feelings.",
        "bye": "Goodbye!"
    }
    return responses.get(question.lower(), "I don't understand.")

print(ai_response("hell"))