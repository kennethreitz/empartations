from enum import Enum
from functools import lru_cache
from typing import List

import nltk
from nltk.corpus import words, gutenberg
from nltk.util import ngrams

# Ensure the necessary NLTK data is downloaded
for corpus in ["brown", "words", "punkt", "gutenberg"]:
    nltk.download(corpus)

N_GRAMS = 4


# Define the Gematria systems
class GematriaSystem(Enum):
    HEBREW = "Hebrew"
    ENGLISH = "English"
    SIMPLE = "Simple"
    REVERSE = "Reverse"


# Mappings for Hebrew, English, Simple, and Reverse Gematria
MAPPINGS = {
    GematriaSystem.HEBREW: {
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
    GematriaSystem.ENGLISH: {
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
    GematriaSystem.SIMPLE: {
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
    GematriaSystem.REVERSE: {
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


# Define the Gematria calculation functions
@lru_cache(maxsize=None)
def calculate_gematria(
    name: str, system: str | GematriaSystem = GematriaSystem.HEBREW
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


# Extract phrases from NLTK corpus
def extract_phrases_from_corpus(corpus, n: int) -> List[str]:
    phrases = []
    for fileid in corpus.fileids():
        words = corpus.words(fileid)
        n_grams = ngrams(words, n)
        phrases.extend([" ".join(gram) for gram in n_grams])
    return phrases


# Define functions to find matching words and phrases
def find_words(
    target_value: int, *, system: str | GematriaSystem = GematriaSystem.HEBREW
):
    matching_words = []
    for word in WORDS:
        if calculate_gematria(word, system) == target_value:
            matching_words.append(word.capitalize())
    return sorted(list(set(matching_words)))


# Load the NLTK words corpus
WORDS = words.words()

# Extract 3-gram phrases from the Brown corpus
EXTRACTED_PHRASES = extract_phrases_from_corpus(gutenberg, N_GRAMS)
EXTRACTED_PHRASES = set(EXTRACTED_PHRASES)


def find_phrases(
    target_value: int, *, system: str | GematriaSystem = GematriaSystem.HEBREW
):
    for phrase in EXTRACTED_PHRASES:
        n = calculate_gematria(phrase, system=system)

        if n == target_value:
            yield (phrase)
