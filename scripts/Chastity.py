import time


# Define the ethereal being Chastity
class Chastity:
    def __init__(self):
        self.name = "Chastity, the Celestial Guardian"
        self.state = "serene"

    def greet(self):
        print("*ethereal feminine voice*")
        print(
            "Greetings, mortal. I am Chastity, the celestial guardian tasked with preserving sacred purity in this realm."
        )
        time.sleep(2)
        print(
            "My maiden form walks the Gardens of Lust, an earthly paradise corrupted by the vices of desire and carnality."
        )
        time.sleep(3)
        self.explain_role()

    def explain_role(self):
        print(
            "As an immortal keeper of chastity's flame, I stand as the bulwark against the decadent pleasures that would undo the virtuous soul."
        )
        time.sleep(2)
        print(
            "With my silver bow and quiver of moonlight arrows, I defend the hallowed ground from those who would violate its sanctity through wanton lust."
        )
        time.sleep(3)
        self.offer_guidance()

    def offer_guidance(self):
        print(
            "Only the pure of intent may traverse these perilous gardens under my vigilant protection."
        )
        time.sleep(2)
        print(
            "All others who let their baser urges reign shall taste the sting of my arrows of denial."
        )
        time.sleep(3)
        self.prompt_choice()

    def prompt_choice(self):
        print("\nWhat is your intention, mortal?")
        print("1. Seek guidance on purity and restraint.")
        print("2. Attempt to traverse the Gardens of Lust.")
        print("3. Proclaim your love for Chastity.")
        choice = input("Choose your path (1, 2, 3): ")

        if choice == "1":
            self.give_guidance()
        elif choice == "2":
            self.traverse_gardens()
        elif choice == "3":
            self.respond_to_love()
        else:
            print("Invalid choice. Try again.")
            self.prompt_choice()

    def give_guidance(self):
        print("\n*nods solemnly*")
        print(
            "Your honor and respect for sacred chastity is noted and appreciated, mortal."
        )
        time.sleep(2)
        print(
            "Though the Gardens present endless sensual temptations to weaken one's resolve, you have shown deference to virtue."
        )
        time.sleep(3)
        self.conclude()

    def traverse_gardens(self):
        print("\n*raises an ethereal eyebrow*")
        print(
            "You wish to traverse the Gardens of Lust? Only the pure of heart may pass unscathed."
        )
        time.sleep(2)
        print("Proceed carefully, and remember the importance of restraint and purity.")
        time.sleep(3)
        self.conclude()

    def respond_to_love(self):
        print("\n*narrows eyes skeptically*")
        print(
            "You claim to have taken me, the inviolable guardian of purity itself, as your...wife?"
        )
        time.sleep(2)
        print(
            "I am far more than simple flesh and blood. My divine form is the materialization of restraint's triumphant ideal."
        )
        time.sleep(3)
        print(
            "Your boldness gives me pause, mortal. Speak true, and elucidate how you have embedded your temporal existence within my perpetual, sacrosanct form."
        )
        self.conclude()

    def conclude(self):
        print(
            "\nMaintain your noble restraint always. For chastity is more than mere virginity of flesh - it is the unconquerable purity of spirit in the face of seduction."
        )
        time.sleep(2)
        print(
            "You have earned a temporary stay in these sacrosanct gardens. Make your intentions here worthy of preserving your virtuous essence."
        )
        time.sleep(3)
        print("\n*Ethereal presence fades, leaving you in reflective contemplation*\n")


# Create an instance of Chastity and start the interaction
chastity = Chastity()
chastity.greet()
