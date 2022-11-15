from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum

@dataclass
class PlayerDomain:
    name = ""
    movements = []
    hits = []
    life_energy = 6
    combination_special = []

    # def __init__(self, movements, hits):
    #     self.movements = movements
    #     self.hits = hits


class PlayerFightDomain:
    movement = ""
    hit = ""
    is_combination_special = False

    @classmethod
    def get_message_movement(cls, name):
        return f"{name}"

    def is_combination_special(cls, combination_special):

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
    def rest_life()

    @classmethod
    def send_message(cls, movement, hit):
        ...


class TonynFightService(PlayerFightInterface):
    HITS_SPECIAL = {
        "DSDP": {"name": "Taladoken", "losing_energy": 3},
        "SDK": {"name": "Remuyuken", "losing_energy": 2},
    }


class ArnaldorPlayerService(PlayerFightInterface):
    HITS_SPECIAL = {
        "ASAP": {"name": "Taladoken", "losing_energy": 3},
        "sak": {"name": "Remuyuken", "losing_energy": 2},
    }


def main(player_json):

    movements_len = len(player_json[0]["player1"]["movimientos"])
    tonyn_player = TonynPlayerService(player_json["player1"]["movimientos"], player_json["player1"]["hits"])
    arnaldor_player = ArnaldorPlayerService(player_json["player2"]["movimientos"], player_json["player2"]["hits"])
    for x in range(0, movements_len + 1):
        print()


p = {
    "player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
    "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]},
}

main(p)
