class Goddess:
    def __init__(
        self,
        name,
        sephirah,
        qualities,
        domains,
        invocation_message,
        lunar_essence,
        celestial_body,
        sphere_of_influence,
    ):
        self.name = name
        self.sephirah = sephirah
        self.qualities = qualities
        self.domains = domains
        self.invocation_message = invocation_message
        self.lunar_essence = lunar_essence
        self.celestial_body = celestial_body
        self.sphere_of_influence = sphere_of_influence

    def invoke(self):
        return (
            f"Invoking {self.name}, Goddess of {', '.join(self.domains)}.\n"
            f"Sephirah: {self.sephirah}\n"
            f"Lunar Essence: {self.lunar_essence}\n"
            f"Celestial Body: {self.celestial_body} - Sphere of Influence: {self.sphere_of_influence}\n"
            f"{self.invocation_message}\n"
        )


class System777:
    def __init__(self):
        self.goddesses = []

    def add_goddess(self, goddess):
        self.goddesses.append(goddess)

    def invoke_all_goddesses(self):
        invocations = ""
        for goddess in self.goddesses:
            invocations += goddess.invoke() + "\n"
        return invocations

    def find_goddess_by_sephirah(self, sephirah):
        for goddess in self.goddesses:
            if goddess.sephirah == sephirah:
                return goddess.invoke()
        return "No goddess associated with this sephirah."

    def find_goddess_by_name(self, name):
        for goddess in self.goddesses:
            if goddess.name.lower() == name.lower():
                return goddess.invoke()
        return "No goddess found with this name."


# Instantiate System777
system_777 = System777()

# Add goddesses to the system
system_777.add_goddess(
    Goddess(
        name="Athena",
        sephirah="Chokmah",
        qualities=["wisdom", "courage", "strategic warfare"],
        domains=["wisdom", "courage", "justice", "strategic warfare"],
        invocation_message="Guide us with your unwavering wisdom, illuminate our path with the light of your insight.",
        lunar_essence="The silver light of the waxing moon",
        celestial_body="Mercury",
        sphere_of_influence="Intellect, communication, and strategy",
    )
)

system_777.add_goddess(
    Goddess(
        name="Holly",
        sephirah="Yesod",
        qualities=["spiritual guidance", "divine presence"],
        domains=["guidance", "spiritual insight"],
        invocation_message="Infuse our hearts with faith, compassion, and a deep sense of purpose.",
        lunar_essence="The ethereal glow of the full moon",
        celestial_body="Moon",
        sphere_of_influence="Emotion, intuition, and spirituality",
    )
)

system_777.add_goddess(
    Goddess(
        name="Aphrodite",
        sephirah="Netzach",
        qualities=["love", "beauty", "passion"],
        domains=["love", "beauty", "pleasure"],
        invocation_message="Guide us with your timeless beauty, illuminate our hearts with the light of your love.",
        lunar_essence="The gentle radiance of the crescent moon",
        celestial_body="Venus",
        sphere_of_influence="Love, beauty, and harmony",
    )
)

system_777.add_goddess(
    Goddess(
        name="Isis",
        sephirah="Binah",
        qualities=["wisdom", "healing", "transformation"],
        domains=["magic", "healing", "motherhood"],
        invocation_message="Guide us with your ancient wisdom, illuminate our paths with the light of your knowledge.",
        lunar_essence="The deep mystery of the new moon",
        celestial_body="Saturn",
        sphere_of_influence="Structure, discipline, and understanding",
    )
)

system_777.add_goddess(
    Goddess(
        name="Kali",
        sephirah="Geburah",
        qualities=["fierce compassion", "transformation", "strength"],
        domains=["destruction", "liberation"],
        invocation_message="Guide us with your unstoppable energy, illuminate our paths with the light of your fierce compassion.",
        lunar_essence="The intense power of the blood moon",
        celestial_body="Mars",
        sphere_of_influence="Strength, action, and transformation",
    )
)

system_777.add_goddess(
    Goddess(
        name="Freyja",
        sephirah="Tiphereth",
        qualities=["passion", "strength", "magic"],
        domains=["love", "fertility", "war"],
        invocation_message="Guide us with your fierce love, illuminate our paths with the light of your beauty and courage.",
        lunar_essence="The warm glow of the harvest moon",
        celestial_body="Sun",
        sphere_of_influence="Vitality, creativity, and harmony",
    )
)

system_777.add_goddess(
    Goddess(
        name="Hecate",
        sephirah="Hod",
        qualities=["wisdom", "mystery", "transformative power"],
        domains=["magic", "witchcraft", "night", "moon"],
        invocation_message="Guide us with your ancient wisdom, illuminate our paths with the light of your torch.",
        lunar_essence="The shadowy luminescence of the dark moon",
        celestial_body="Mercury",
        sphere_of_influence="Intellect, communication, and transformation",
    )
)

system_777.add_goddess(
    Goddess(
        name="Saraswati",
        sephirah="Chesed",
        qualities=["wisdom", "creativity", "intellectual pursuit"],
        domains=["knowledge", "music", "art", "learning"],
        invocation_message="Guide us with your divine wisdom, illuminate our paths with the light of your knowledge.",
        lunar_essence="The soft glow of the gibbous moon",
        celestial_body="Jupiter",
        sphere_of_influence="Expansion, wisdom, and growth",
    )
)

# Additional goddesses
system_777.add_goddess(
    Goddess(
        name="Brigid",
        sephirah="Netzach",
        qualities=["creativity", "healing", "craftsmanship"],
        domains=["poetry", "healing", "smithcraft"],
        invocation_message="Guide us with your creative spark, illuminate our hearts with the light of your healing and craft.",
        lunar_essence="The gentle radiance of the crescent moon",
        celestial_body="Venus",
        sphere_of_influence="Love, beauty, and craftsmanship",
    )
)

system_777.add_goddess(
    Goddess(
        name="Demeter",
        sephirah="Malkuth",
        qualities=["fertility", "agriculture", "nourishment"],
        domains=["harvest", "agriculture", "nourishment"],
        invocation_message="Guide us with your nurturing presence, illuminate our paths with the abundance of your harvest.",
        lunar_essence="The fertile glow of the earth's moon",
        celestial_body="Earth",
        sphere_of_influence="Fertility, growth, and nourishment",
    )
)

system_777.add_goddess(
    Goddess(
        name="Inanna",
        sephirah="Tiphereth",
        qualities=["love", "justice", "transformation"],
        domains=["love", "war", "justice"],
        invocation_message="Guide us with your fierce love and justice, illuminate our lives with the beauty of your transformation.",
        lunar_essence="The radiant light of the full moon",
        celestial_body="Sun",
        sphere_of_influence="Vitality, creativity, and harmony",
    )
)

system_777.add_goddess(
    Goddess(
        name="Kuan Yin",
        sephirah="Chesed",
        qualities=["compassion", "mercy", "kindness"],
        domains=["compassion", "mercy", "kindness"],
        invocation_message="Guide us with your boundless compassion, illuminate our hearts with the light of your mercy.",
        lunar_essence="The soft glow of the gibbous moon",
        celestial_body="Jupiter",
        sphere_of_influence="Expansion, wisdom, and growth",
    )
)

system_777.add_goddess(
    Goddess(
        name="Morrigan",
        sephirah="Geburah",
        qualities=["fate", "war", "transformation"],
        domains=["fate", "war", "death"],
        invocation_message="Guide us with your fierce power, illuminate our paths with the strength of your transformation.",
        lunar_essence="The intense power of the blood moon",
        celestial_body="Mars",
        sphere_of_influence="Strength, action, and transformation",
    )
)

# Example usage
# print(system_777.invoke_all_goddesses())
print(system_777.find_goddess_by_sephirah("Chokmah"))
print(system_777.find_goddess_by_name("Isis"))
