from system_777.numbers import (
    calculate_gematria,
    find_words,
    find_phrases,
    GematriaSystem,
)


class MetaphysicalShowcase:
    def __init__(self):
        self.target_value = 777
        self.system = GematriaSystem.ENGLISH

    def demonstrate_gematria_calculation(self, name: str):
        value = calculate_gematria(name, self.system)
        print(
            f"The Gematria value of '{name}' in {self.system.value} system is: {value}"
        )

    def demonstrate_matching_words(self):
        words = find_words(self.target_value, system=self.system)
        print(
            f"Words with Gematria value {self.target_value} in {self.system.value} system: {words}"
        )

    def demonstrate_matching_phrases(self):
        phrases = list(find_phrases(self.target_value, system=self.system))
        print(
            f"Phrases with Gematria value {self.target_value} in {self.system.value} system: {phrases}"
        )

    def set_target_value(self, value: int):
        self.target_value = value
        print(f"Target value set to: {self.target_value}")

    def set_system(self, system: GematriaSystem):
        self.system = system
        print(f"Gematria system set to: {self.system.value}")

    def analyze_personal_name(self, name: str):
        print(f"Analyzing the name '{name}'")
        for system in GematriaSystem:
            value = calculate_gematria(name, system)
            print(
                f"The Gematria value of '{name}' in {system.value} system is: {value}"
            )

    def suggest_similar_names(self, name: str):
        original_value = calculate_gematria(name, self.system)
        print(
            f"Suggesting names with Gematria value {original_value} in {self.system.value} system:"
        )
        similar_names = find_words(original_value, system=self.system)
        print(similar_names)

    def generate_inspirational_phrases(self):
        print(
            f"Generating phrases with Gematria value {self.target_value} in {self.system.value} system:"
        )
        inspirational_phrases = list(
            find_phrases(self.target_value, system=self.system)
        )
        for phrase in inspirational_phrases:
            print(f"- {phrase}")


if __name__ == "__main__":
    showcase = MetaphysicalShowcase()

    # Demonstrate changing target value and system
    showcase.set_target_value(777)
    showcase.set_system(GematriaSystem.HEBREW)

    # Demonstrate Gematria calculation for a specific name
    showcase.demonstrate_gematria_calculation("Metatron")

    # Demonstrate finding matching words
    # showcase.demonstrate_matching_words()

    # Demonstrate finding matching phrases
    # showcase.demonstrate_matching_phrases()

    # Analyze a personal name
    showcase.analyze_personal_name("Kenneth")

    # Suggest similar names
    showcase.suggest_similar_names("KENNETH ROBERT REITZ")

    # Generate inspirational phrases
    # showcase.generate_inspirational_phrases()
