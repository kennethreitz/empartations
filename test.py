import system_777
from system_777.numbers import (
    calculate_gematria,
    find_words,
    find_phrases,
    GematriaSystem,
)


NAME = "SHEKINAH"
SYSTEM = GematriaSystem.Hebrew
GEMATRIA_VALUE = calculate_gematria(NAME, system=SYSTEM)

print(f"The gematria value of the name '{NAME}' is {GEMATRIA_VALUE}.")

print("Possible words with the gematria value of the name:")
print(find_words(GEMATRIA_VALUE))
