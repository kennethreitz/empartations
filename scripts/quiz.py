def spiritual_quiz():
    questions = [
        "How often do you meditate or pray?",
        "Do you feel connected to a higher power?",
        "How do you handle stressful situations?",
        "What does spirituality mean to you?",
        "Do you practice any form of mindfulness?",
    ]

    answers = []

    for question in questions:
        print(question)
        answer = input("Your answer: ")
        answers.append(answer)

    print("\nThank you for completing the quiz! Here are your responses:")
    for i, answer in enumerate(answers):
        print(f"Q{i+1}: {questions[i]}\nA: {answer}\n")

    # Provide a simple analysis based on responses
    print(
        "Based on your responses, it seems you are on a meaningful spiritual journey. Keep exploring and nurturing your connection to the divine."
    )


# Run the quiz
spiritual_quiz()
