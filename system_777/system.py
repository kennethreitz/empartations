from pydantic import BaseModel, Field
from typing import List

from .models import DivineBeing
from .database import angels, demons, goddesses


class System777(BaseModel):
    goddesses: List[DivineBeing] = Field(default_factory=list)
    angels: List[DivineBeing] = Field(default_factory=list)
    demons: List[DivineBeing] = Field(default_factory=list)

    @property
    def all_beings(self) -> List[DivineBeing]:
        return self.goddesses + self.angels + self.demons

    def add_demon(self, demon: DivineBeing):
        self.demons.append(demon)

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

    def find(self, s: str):
        s_lower = s.lower()
        results = []

        for being in self.all_beings:
            if s_lower in being.name.lower():
                results.append(being)
            elif s_lower in being.sephirah.lower():
                results.append(being)
            elif s_lower in [q.lower() for q in being.qualities]:
                results.append(being)

        return results

    def find_being_by_sephirah(self, sephirah: str) -> str:
        for being in self.all_beings:
            if being.sephirah == sephirah:
                return being

        return "No being associated with this sephirah."

    def find_being_by_name(self, name: str) -> str:
        name_lower = name.lower()

        for being in self.all_beings:
            if being.name.lower() == name_lower:
                return being.invoke()

    def find_being_by_quality(self, quality: str) -> str:
        quality_lower = quality.lower()
        results = []

        for being in self.all_beings:
            if quality_lower in [q.lower() for q in being.qualities]:
                results.append(being)

        return results


# Initialize the system
system_777 = System777(goddesses=goddesses, angels=angels, demons=demons)
