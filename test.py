import system_777
from system_777.numbers import (
    calculate_gematria,
    find_words,
    find_phrases,
    GematriaSystem,
)


NAME = "I AM THAT I AM"
SYSTEM = GematriaSystem.HEBREW
# GEMATRIA_VALUE = calculate_gematria(NAME, system=SYSTEM)

# print(f"The gematria value of the name '{NAME}' is {GEMATRIA_VALUE}.")
# print()
# print("Possible phrases with the gematria value of the name:")
found_phrases = []
for phrase in find_words(calculate_gematria(NAME, system=SYSTEM)):
    if phrase not in found_phrases:
        found_phrases.append(phrase)

    print(phrase)
