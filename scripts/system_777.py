from pydantic import BaseModel, Field
from typing import List


class DivineBeing(BaseModel):
    name: str
    sephirah: str
    qualities: List[str]
    domains: List[str]
    invocation_message: str
    lunar_essence: str
    celestial_body: str
    sphere_of_influence: str

    def invoke(self, custom_message: str = None) -> str:
        message = custom_message if custom_message else self.invocation_message
        return (
            f"Invoking {self.name}, of {', '.join(self.domains)}.\n"
            f"Sephirah: {self.sephirah}\n"
            f"Lunar Essence: {self.lunar_essence}\n"
            f"Celestial Body: {self.celestial_body} - Sphere of Influence: {self.sphere_of_influence}\n"
            f"{message}\n"
        )


class System777(BaseModel):
    goddesses: List[DivineBeing] = Field(default_factory=list)
    angels: List[DivineBeing] = Field(default_factory=list)

    def add_goddess(self, goddess: DivineBeing):
        self.goddesses.append(goddess)

    def add_angel(self, angel: DivineBeing):
        self.angels.append(angel)

    def invoke_all(self) -> str:
        invocations = ""
        for goddess in self.goddesses:
            invocations += goddess.invoke() + "\n"
        for angel in self.angels:
            invocations += angel.invoke() + "\n"
        return invocations

    def find_being_by_sephirah(self, sephirah: str) -> str:
        for goddess in self.goddesses:
            if goddess.sephirah == sephirah:
                return goddess.invoke()
        for angel in self.angels:
            if angel.sephirah == sephirah:
                return angel.invoke()
        return "No being associated with this sephirah."

    def find_being_by_name(self, name: str) -> str:
        name_lower = name.lower()
        for goddess in self.goddesses:
            if goddess.name.lower() == name_lower:
                return goddess.invoke()
        for angel in self.angels:
            if angel.name.lower() == name_lower:
                return angel.invoke()
        return "No being found with this name."

    def find_being_by_quality(self, quality: str) -> str:
        quality_lower = quality.lower()
        results = []
        for goddess in self.goddesses:
            if quality_lower in [q.lower() for q in goddess.qualities]:
                results.append(goddess.invoke())
        for angel in self.angels:
            if quality_lower in [q.lower() for q in angel.qualities]:
                results.append(angel.invoke())
        return "\n".join(results) if results else "No being found with this quality."


# Initialize the system
system_777 = System777()

# Add goddesses to the system
system_777.add_goddess(
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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
    DivineBeing(
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

# Add angels to the system
system_777.add_angel(
    DivineBeing(
        name="Metatron",
        sephirah="Kether",
        qualities=["divine light", "unity"],
        domains=["divine light", "unity"],
        invocation_message="Guide us with your divine light, illuminate our path with the unity of the cosmos.",
        lunar_essence="The blinding light of the cosmic moon",
        celestial_body="Sun",
        sphere_of_influence="Divine presence and cosmic order",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Raziel",
        sephirah="Chokmah",
        qualities=["wisdom", "creative force"],
        domains=["wisdom", "knowledge"],
        invocation_message="Guide us with your profound wisdom, illuminate our minds with your creative force.",
        lunar_essence="The radiant glow of the wise moon",
        celestial_body="Uranus",
        sphere_of_influence="Wisdom and secrets of the universe",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Tzaphkiel",
        sephirah="Binah",
        qualities=["understanding", "form"],
        domains=["understanding", "insight"],
        invocation_message="Guide us with your deep understanding, illuminate our lives with the clarity of your insight.",
        lunar_essence="The deep mystery of the new moon",
        celestial_body="Saturn",
        sphere_of_influence="Structure and understanding",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Tzadkiel",
        sephirah="Chesed",
        qualities=["mercy", "expansion"],
        domains=["mercy", "benevolence"],
        invocation_message="Guide us with your endless mercy, illuminate our paths with your benevolent light.",
        lunar_essence="The soft glow of the gibbous moon",
        celestial_body="Jupiter",
        sphere_of_influence="Expansion and benevolence",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Samael",
        sephirah="Geburah",
        qualities=["strength", "discipline"],
        domains=["strength", "justice"],
        invocation_message="Guide us with your fierce strength, illuminate our lives with the power of discipline.",
        lunar_essence="The intense power of the blood moon",
        celestial_body="Mars",
        sphere_of_influence="Strength and discipline",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Raphael",
        sephirah="Tiphereth",
        qualities=["beauty", "harmony"],
        domains=["healing", "beauty"],
        invocation_message="Guide us with your healing touch, illuminate our souls with the harmony of beauty.",
        lunar_essence="The warm glow of the harvest moon",
        celestial_body="Sun",
        sphere_of_influence="Healing and harmony",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Haniel",
        sephirah="Netzach",
        qualities=["victory", "endurance"],
        domains=["victory", "love"],
        invocation_message="Guide us with your victorious spirit, illuminate our hearts with your enduring love.",
        lunar_essence="The gentle radiance of the crescent moon",
        celestial_body="Venus",
        sphere_of_influence="Love and victory",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Michael",
        sephirah="Hod",
        qualities=["glory", "splendor"],
        domains=["protection", "glory"],
        invocation_message="Guide us with your protective presence, illuminate our paths with your glorious light.",
        lunar_essence="The shadowy luminescence of the dark moon",
        celestial_body="Mercury",
        sphere_of_influence="Protection and glory",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Gabriel",
        sephirah="Yesod",
        qualities=["foundation", "connection to the divine"],
        domains=["communication", "foundation"],
        invocation_message="Guide us with your divine communication, illuminate our spirits with your foundational strength.",
        lunar_essence="The ethereal glow of the full moon",
        celestial_body="Moon",
        sphere_of_influence="Divine connection and communication",
    )
)

system_777.add_angel(
    DivineBeing(
        name="Sandalphon",
        sephirah="Malkuth",
        qualities=["manifestation", "earthly presence"],
        domains=["manifestation", "earth"],
        invocation_message="Guide us with your grounded presence, illuminate our paths with the light of manifestation.",
        lunar_essence="The fertile glow of the earth's moon",
        celestial_body="Earth",
        sphere_of_influence="Manifestation and earthly presence",
    )
)

# Example usage
print(system_777.invoke_all())
print(system_777.find_being_by_sephirah("Chokmah"))
print(system_777.find_being_by_name("Isis"))
print(system_777.find_being_by_name("Metatron"))
print(system_777.find_being_by_quality("wisdom"))
