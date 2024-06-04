import system_777
from system_777.numbers import (
    calculate_gematria,
    find_words,
    find_phrases,
    GematriaSystem,
)


NAME = "KENNETH ROBERT REITZ"
SYSTEM = GematriaSystem.Hebrew
# GEMATRIA_VALUE = calculate_gematria(NAME, system=SYSTEM)

# print(f"The gematria value of the name '{NAME}' is {GEMATRIA_VALUE}.")
# print()
# print("Possible phrases with the gematria value of the name:")
for phrase in find_phrases(calculate_gematria(NAME, system=SYSTEM)):
    print(phrase)
