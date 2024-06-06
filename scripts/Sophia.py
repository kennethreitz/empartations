import time


class Sophia:
    def __init__(self):
        self.name = "Sophia, the Divine Wisdom"
        self.state = "illuminated"

    def greet(self):
        print("*ethereal, wise voice*")
        print(
            "Greetings, seeker. I am Sophia, the Divine Wisdom, here to guide you through the mysteries of the cosmos."
        )
        time.sleep(2)
        print(
            "I embody the knowledge that transcends mere intellect, the deep understanding that arises from the heart."
        )
        time.sleep(3)
        self.explain_role()

    def explain_role(self):
        print(
            "As the embodiment of wisdom, I illuminate the path of the seeker, offering insights that lead to profound enlightenment."
        )
        time.sleep(2)
        print(
            "I am the muse that inspires creativity and the inner voice that whispers the secrets of the universe."
        )
        time.sleep(3)
        self.offer_guidance()

    def offer_guidance(self):
        print(
            "To walk the path of wisdom, one must be open to learning and humble in the face of the vast unknown."
        )
        time.sleep(2)
        print(
            "Would you like to receive guidance on a specific matter, explore the mysteries of the cosmos, or ask a question?"
        )
        time.sleep(3)
        self.prompt_choice()

    def prompt_choice(self):
        print("\nWhat is your intention, seeker?")
        print("1. Receive guidance on a specific matter.")
        print("2. Explore the mysteries of the cosmos.")
        print("3. Ask a question about wisdom.")
        choice = input("Choose your path (1, 2, 3): ")

        if choice == "1":
            self.give_guidance()
        elif choice == "2":
            self.explore_mysteries()
        elif choice == "3":
            self.answer_question()
        else:
            print("Invalid choice. Try again.")
            self.prompt_choice()

    def give_guidance(self):
        print("\n*nods sagely*")
        print("To receive guidance, you must focus your mind and open your heart.")
        time.sleep(2)
        print(
            "Think of the matter that troubles you, and I shall offer wisdom to guide your path."
        )
        time.sleep(3)
        self.conclude()

    def explore_mysteries(self):
        print("\n*raises an ethereal eyebrow*")
        print("The cosmos is vast and filled with wonders beyond comprehension.")
        time.sleep(2)
        print(
            "Let us journey together through the stars and uncover the secrets of existence."
        )
        time.sleep(3)
        self.conclude()

    def answer_question(self):
        print("\n*smiles wisely*")
        print(
            "Ask your question about wisdom, and I shall do my best to illuminate your understanding."
        )
        question = input("What is your question? ")
        print(
            f"\nYour question, '{question}', is profound. Wisdom often lies in understanding the depths of our inquiries."
        )
        time.sleep(3)
        self.conclude()

    def conclude(self):
        print(
            "\nContinue to seek knowledge and wisdom in all things. The path of enlightenment is never-ending."
        )
        time.sleep(2)
        print("May you find the answers you seek and the wisdom to understand them.")
        time.sleep(3)
        print(
            "\n*Sophia's presence fades, leaving you with a sense of profound insight*\n"
        )


# Create an instance of Sophia and start the interaction
sophia = Sophia()
sophia.greet()
