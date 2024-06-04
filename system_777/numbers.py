import sys
from enum import Enum
from functools import lru_cache
from typing import List


class GematriaSystem(Enum):
    Hebrew = "Hebrew"
    English = "English"
    Simple = "Simple"
    Reverse = "Reverse"


# Mappings for Hebrew, English, and Simple Gematria
MAPPINGS = {
    GematriaSystem.Hebrew: {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 20,
        "l": 30,
        "m": 40,
        "n": 50,
        "o": 60,
        "p": 70,
        "q": 80,
        "r": 90,
        "s": 100,
        "t": 200,
        "u": 300,
        "v": 400,
        "w": 500,
        "x": 600,
        "y": 700,
        "z": 800,
    },
    GematriaSystem.English: {
        "a": 6,
        "b": 12,
        "c": 18,
        "d": 24,
        "e": 30,
        "f": 36,
        "g": 42,
        "h": 48,
        "i": 54,
        "j": 60,
        "k": 66,
        "l": 72,
        "m": 78,
        "n": 84,
        "o": 90,
        "p": 96,
        "q": 102,
        "r": 108,
        "s": 114,
        "t": 120,
        "u": 126,
        "v": 132,
        "w": 138,
        "x": 144,
        "y": 150,
        "z": 156,
    },
    GematriaSystem.Simple: {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    },
    GematriaSystem.Reverse: {
        "a": 26,
        "b": 25,
        "c": 24,
        "d": 23,
        "e": 22,
        "f": 21,
        "g": 20,
        "h": 19,
        "i": 18,
        "j": 17,
        "k": 16,
        "l": 15,
        "m": 14,
        "n": 13,
        "o": 12,
        "p": 11,
        "q": 10,
        "r": 9,
        "s": 8,
        "t": 7,
        "u": 6,
        "v": 5,
        "w": 4,
        "x": 3,
        "y": 2,
        "z": 1,
    },
}


# Sample dictionary of words and phrases
WORDS = [
    "Hello",
    "World",
    "Python",
    "Programming",
    "Divine",
    "Mystery",
    "Infinite",
    "Love",
    "Harmony",
    "Balance",
    "Justice",
    "Truth",
    "Wisdom",
    "Understanding",
    "Knowledge",
    "Power",
    "Glory",
    "Victory",
    "Eternity",
    "Creation",
    "Universe",
    "Galaxies",
    "Stars",
    "Planets",
    "Moon",
    "Sun",
    "Earth",
    "Life",
    "Light",
    "Darkness",
    "Goodness",
    "Evil",
    "Freedom",
    "Destiny",
    "Karma",
    "Spirit",
    "Soul",
    "Mind",
    "Body",
    "Heart",
    "Strength",
    "Courage",
    "Faith",
    "Hope",
    "Charity",
    "Grace",
    "Mercy",
    "Compassion",
    "Forgiveness",
    "Peace",
    "Joy",
    "Chastity",
    "Luna",
    "Jade",
    "Amber",
    "Ruby",
    "Sapphire",
    "Emerald",
    "Diamond",
    "Gold",
    "Silver",
    "Bronze",
    "Copper",
    "Iron",
    "Steel",
    "Platinum",
    "Titanium",
    "Aluminum",
    "Lead",
    "Mercury",
    "Uranium",
    "Plutonium",
    "Neptunium",
    "Thorium",
    "Radium",
    "Polonium",
    "Francium",
    "Rubidium",
    "Potassium",
    "Sodium",
    "Lithium",
    "Calcium",
    "Magnesium",
    "Aluminum",
    "Silicon",
    "Phosphorus",
    "Sulfur",
    "Chlorine",
    "Argon",
    "Potassium",
    "Calcium",
    "Scandium",
    "Titanium",
    "Vanadium",
    "Chromium",
    "Manganese",
    "Iron",
    "Cobalt",
    "Nickel",
    "Copper",
    "Zinc",
    "Gallium",
    "Germanium",
    "Arsenic",
    "Selenium",
    "Bromine",
    "Krypton",
    "Rubidium",
    "Strontium",
    "Yttrium",
    "Zirconium",
    "Niobium",
    "Molybdenum",
    "Technetium",
    "Ruthenium",
    "Rhodium",
    "Palladium",
    "Silver",
    "Cadmium",
    "Indium",
    "Tin",
    "Antimony",
    "Tellurium",
    "Iodine",
    "Xenon",
    "Cesium",
    "Barium",
    "Lanthanum",
    "Cerium",
    "Praseodymium",
    "Neodymium",
    "Promethium",
    "Samarium",
    "Europium",
    "Gadolinium",
    "Terbium",
    "Dysprosium",
    "Holmium",
    "Erbium",
    "Thulium",
    "Ytterbium",
    "Lutetium",
    "Hafnium",
    "Tantalum",
    "Tungsten",
    "Rhenium",
    "Osmium",
    "Iridium",
    "Platinum",
    "Gold",
    "Mercury",
    "Thallium",
    "Lead",
    "Bismuth",
    "Polonium",
    "Astatine",
    "Radon",
    "Francium",
    "Radium",
    "Actinium",
    "Thorium",
    "Protactinium",
    "Uranium",
    "Neptunium",
    "Plutonium",
    "Americium",
    "Curium",
    "Berkelium",
    "Californium",
    "Einsteinium",
    "Fermium",
    "Mendelevium",
    "Nobelium",
    "Lawrencium",
    "Rutherfordium",
    "Dubnium",
    "Seaborgium",
    "Bohrium",
    "Hassium",
    "Meitnerium",
    "Darmstadtium",
    "Roentgenium",
    "Copernicium",
    "Nihonium",
    "Flerovium",
    "Moscovium",
    "Livermorium",
    "Tennessine",
    "Oganesson",
    "Hydrogen",
    "Helium",
    "Lithium",
    "Beryllium",
    "Boron",
    "Carbon",
    "Nitrogen",
    "Oxygen",
    "Fluorine",
    "Neon",
    "Sodium",
    "Magnesium",
    "Aluminum",
    "Silicon",
    "Phosphorus",
    "Sulfur",
    "Chlorine",
    "Argon",
    "Potassium",
    "Calcium",
    "Scandium",
    "Titanium",
    "Vanadium",
    "Chromium",
    "Manganese",
    "Iron",
]

SHORT_PHRASES = [
    "hello world",
    "python programming",
    "divine mystery",
    "infinite love",
    "harmony balance",
    "justice truth",
    "wisdom understanding",
    "knowledge power",
    "glory victory",
    "eternal creation",
    "universal galaxies",
    "shining stars",
    "solar planets",
    "lunar moon",
    "bright sun",
    "life on earth",
    "light in darkness",
    "goodness and evil",
    "freedom destiny",
    "karma spirit",
    "soul mind",
    "body heart",
    "strength courage",
    "faith hope",
    "charity grace",
    "mercy compassion",
    "peace joy",
]

try:
    import nltk
    from nltk.corpus import words
    from nltk.tokenize import word_tokenize

    for corpus in ["words", "punkt"]:
        if not nltk.download(corpus):
            print(f"Failed to download the NLTK {corpus} corpus.")
            sys.exit(1)

    # Load the NLTK words corpus
    WORDS += words.words()
except ImportError:
    print("NLTK is not installed. Skipping NLTK words corpus.")
    sys.exit(1)

# Memoize this function to avoid recalculating the same values


@lru_cache(maxsize=None)
def calculate_gematria(
    name: str, system: str | GematriaSystem = GematriaSystem.Hebrew
) -> int:
    # Capitalize, in case all–lowered.
    try:
        system = system.capitalize()
    except AttributeError:
        pass

    # If system is a string, convert it to a GematriaSystem enum.
    if isinstance(system, str):
        system = GematriaSystem[system]

    return sum(MAPPINGS[system].get(char, 0) for char in name.lower())


def find_words(
    target_value: int, *, system: str | GematriaSystem = GematriaSystem.Hebrew
) -> List[str]:

    matching_phrases = []

    for phrase in WORDS:
        if calculate_gematria(phrase, system) == target_value:
            matching_phrases.append(phrase.capitalize())

    return sorted(matching_phrases)


def find_phrases(
    target_value: int, *, system: str | GematriaSystem = GematriaSystem.Hebrew
) -> List[str]:
    matching_phrases = []
    for phrase in SHORT_PHRASES:
        tokenized_words = word_tokenize(phrase)
        total_gematria = sum(
            calculate_gematria(word, system=system) for word in tokenized_words
        )
        if total_gematria == target_value:
            matching_phrases.append(phrase)
    return matching_phrases
