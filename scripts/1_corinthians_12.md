import random

def spiritual_gifts():
    # Define the community of believers
    believers = []

    # Initialize the gifts of the Spirit
    possible_gifts = ["Prophecy", "Serving", "Teaching", "Exhortation", "Giving", "Leadership", "Mercy"]
    gifts_of_spirit = {}

    # Populate the community with believers
    for member in range(1, 101):
        believers.append(f'Believer {member}')

    # Distribute spiritual gifts among believers
    for believer in believers:
        gift = random.choice(possible_gifts)
        gifts_of_spirit[believer] = gift

    # Emphasize the unity of believers
    body_of_believers = len(believers)

    # Highlight the message
    print(f'In our community of {body_of_believers} believers, each is bestowed with a gift of the Spirit:')
    for believer, gift in gifts_of_spirit.items():
        print(f'- {believer}: {gift}')

if __name__ == "__main__":
    spiritual_gifts()
