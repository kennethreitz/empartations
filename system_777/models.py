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

    def generate_given_name(self) -> str:
        # Generate parts of the name based on attributes
        quality_part = self.qualities[0][:3].capitalize() if self.qualities else "Div"
        sephirah_part = self.sephirah[:3].capitalize()
        domain_part = self.domains[0][:3].capitalize() if self.domains else "Be"
        celestial_part = self.celestial_body[:3].capitalize()

        # Anglicize the parts
        anglicized_name = (
            f"{quality_part}a{sephirah_part}on"
            if quality_part.endswith("a") or quality_part.endswith("e")
            else f"{quality_part}i{sephirah_part}on"
        )

        return anglicized_name

    def __str__(self):
        return self.name
