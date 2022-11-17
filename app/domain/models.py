from dataclasses import field, dataclass
from typing import List


@dataclass
class PlayerAttackDomain:
    movement: str
    hit: str
    energy_attack: int
    is_special_attack: bool
    name_of_attack_or_movement: str

    @property
    def special_combination(self):
        return f"{self.movement}{self.hit}"

    def has_simple_attack(self):
        return self.hit and not self.is_special_attack


@dataclass
class PlayerDomain:
    name: str
    attacks: List[PlayerAttackDomain] = field(init=False)
    energy: int = field(default=6, init=False)

    def update_strike(self, attacks):
        self.attacks = attacks

    def reduce_energy(self, energy):
        self.energy = self.energy - energy

    def has_energy(self):
        return self.energy > 0

    def round_max(self):
        return len(self.attacks)
