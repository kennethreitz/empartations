# The Seven Rays concept from the esoteric teachings of Alice A. Bailey can be described using Python code
# in a metaphorical way. The code will outline each Ray and its associated qualities.

# Define the Seven Rays as a dictionary
seven_rays = {
    "1st Ray": {
        "Name": "Ray of Will or Power",
        "Qualities": ["Power", "Will", "Purpose", "Leadership"],
        "Color": "Red"
    },
    "2nd Ray": {
        "Name": "Ray of Love-Wisdom",
        "Qualities": ["Love", "Wisdom", "Understanding", "Inclusivity"],
        "Color": "Blue"
    },
    "3rd Ray": {
        "Name": "Ray of Active Intelligence",
        "Qualities": ["Intelligence", "Creativity", "Adaptability", "Mental Agility"],
        "Color": "Yellow"
    },
    "4th Ray": {
        "Name": "Ray of Harmony through Conflict",
        "Qualities": ["Harmony", "Beauty", "Artistry", "Balance"],
        "Color": "Green"
    },
    "5th Ray": {
        "Name": "Ray of Concrete Knowledge or Science",
        "Qualities": ["Knowledge", "Science", "Detail-Oriented", "Analytical"],
        "Color": "Orange"
    },
    "6th Ray": {
        "Name": "Ray of Devotion or Abstract Idealism",
        "Qualities": ["Devotion", "Loyalty", "Idealism", "Faith"],
        "Color": "Indigo"
    },
    "7th Ray": {
        "Name": "Ray of Ceremonial Order or Magic",
        "Qualities": ["Order", "Ritual", "Magic", "Organizational Skills"],
        "Color": "Violet"
    }
}

# Display the information about each Ray
for ray, details in seven_rays.items():
    print(f"{ray}: {details['Name']}")
    print(f"Qualities: {', '.join(details['Qualities'])}")
    print(f"Color: {details['Color']}\n")
