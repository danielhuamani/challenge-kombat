from abc import ABC, abstractmethod
from dataclasses import field
from dataclassy import dataclass
from enum import Enum
from typing import Any, List


@dataclass
class PlayerFightDomain:
    movement: str
    hit: str
    is_combination_special: bool = field(init=False)
    combination_special: list = field(init=False, repr=False)

    @classmethod
    def get_message_movement(cls, name):
        return f"{name}"

    def __dataclass_post_init__(self, combination_special):
        self.is_combination_special = f"{self.movement}{self.hit}" in combination_special


@dataclass
class PlayerDomain:
    name: str
    combination_special: list
    movements: list
    hits: list
    strike: List[PlayerFightDomain] = field(init=False)
    life_energy: int = field(default=6, init=False)

    def __post_init__(self):
        print(self.movements)
        self.strike = [
            PlayerFightDomain(self.movements[x], self.hits[x], self.combination_special)
            for x in range(0, len(self.movements))
        ]

    # def __init__(self, movements, hits):
    #     self.movements = movements
    #     self.hits = hits


# class PlayerInterface():

#     def update():

#     def get():


class PlayerFightService:
    MOVEMENTS = {"W": "Arriba", "S": "Abajo", "A": "Izquierda", "D": "Derecha"}
    HITS = {"P": {"name": "Puño", "losing_energy": 1}, "K": {"name": "Patada", "losing_energy": 1}}
    HITS_SPECIAL = {}
    GAME_OVER_ENERGY = 0

    @classmethod
    def execute(cls, player: PlayerDomain):
        movement = player.movements.pop()
        hit = player.hits.pop()
        return player

    @classmethod
    def send_message(cls, movement, hit):
        ...


# class TonynFightService(PlayerFightInterface):
#     HITS_SPECIAL = {
#         "DSDP": {"name": "Taladoken", "losing_energy": 3},
#         "SDK": {"name": "Remuyuken", "losing_energy": 2},
#     }


# class ArnaldorPlayerService(PlayerFightInterface):
#     HITS_SPECIAL = {
#         "ASAP": {"name": "Taladoken", "losing_energy": 3},
#         "sak": {"name": "Remuyuken", "losing_energy": 2},
# }
class StartOfFightService:
    ...


def main(player_json):

    num_strike = len(player_json["player1"]["movimientos"])
    player_1_movements = player_json["player1"]["movimientos"]
    player_1_hits = player_json["player1"]["golpes"]
    player_2_movements = player_json["player2"]["movimientos"]
    player_2_hits = player_json["player2"]["golpes"]
    tonyn_player1 = PlayerDomain("Tonyn", ["DSDP", "SDK"], player_1_movements, player_2_hits)
    arnaldor_player2 = PlayerDomain("Arnaldor", ["SAK", "ASAP"], player_2_movements, player_2_hits)
    # for x in range(0, movements_len + 1):
    #     print()
    print(tonyn_player1, arnaldor_player2)


p = {
    "player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
    "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]},
}

main(p)
