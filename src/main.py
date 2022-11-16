from abc import ABC, abstractmethod
from dataclasses import field, dataclass
from enum import IntEnum
from typing import Any, List


@dataclass
class PlayerFightDomain:
    movement: str
    hit: str
    energy_per_hit: int

    # def __dataclass_post_init__(self, combination_special):
    #     self.is_combination_special = f"{self.movement}{self.hit}" in combination_special


@dataclass
class PlayerDomain:
    name: str
    movements: list
    hits: list
    strikes: List[PlayerFightDomain] = field(init=False)
    energy: int = field(default=6, init=False)

    def update_strike(self, strikes):
        self.strikes = strikes

    def reduce_energy(self, energy):
        self.energy = self.energy - energy


class PlayerFightRepository:
    @classmethod
    def play_(cls, player: PlayerDomain):
        player

    @classmethod
    def send_message(cls, movement, hit, combination_special):
        ...


class Player1CombinationEnergy(IntEnum):
    DSDP = 3
    SDK = 2
    P = 1
    K = 1


class Player2CombinationEnergy(IntEnum):
    SAK = 3
    ASAP = 2
    P = 1
    K = 1


class PlayerCreateService:
    enum_combination_energy = None

    @classmethod
    def execute(cls, name, movements, hits):
        num_plays = len(movements)
        p = PlayerDomain(name, movements, hits)
        strikes = []
        for x in range(num_plays):
            energy_per_hit = cls.get_energy_per_hit(movements[x], hits[x])
            strikes.append(PlayerFightDomain(movements[x], hits[x], energy_per_hit))
        p.update_strike(strikes)
        return p

    @classmethod
    def get_energy_per_hit(cls, movement, hit):
        combination_special = f"{movement}{hit}"
        if combination_special in cls.enum_combination_energy.__members__:
            return cls.enum_combination_energy[combination_special].value
        elif hit in cls.enum_combination_energy.__members__:
            return cls.enum_combination_energy[hit].value
        else:
            return 0


class Player1CreateService(PlayerCreateService):
    enum_combination_energy = Player1CombinationEnergy


class Player2CreateService(PlayerCreateService):
    enum_combination_energy = Player2CombinationEnergy


class StartOfFightService:
    @classmethod
    def execute(cls, player1, player2, num_plays):
        players = [player1, player2]
        win_is = None
        if cls.order_by(player1, player2) == "player2":
            players.reverse()
        for x in range(num_plays):
            player_first = players[0]
            player_second = players[1]
            cls.reduce_energy(player_second, player_first.strikes[x].energy_per_hit)

            cls.reduce_energy(player_first, player_second.strikes[x].energy_per_hit)
            print(player_second.energy)

    @classmethod
    def reduce_energy(cls, player, energy):
        player.reduce_energy(energy)
        return player

    @classmethod
    def validate_energy(cls, player):
        return player.energy > 0

    @classmethod
    def order_by(cls, player1, player2):
        p1_len_movements = len(player1.movements)
        p1_len_hits = len(player1.hits)
        p2_len_movements = len(player2.movements)
        p2_len_hits = len(player2.hits)
        result_buttons = cls.order_by_len(p1_len_movements + p1_len_hits, p2_len_movements + p2_len_hits)
        result_movements = cls.order_by_len(p1_len_movements, p2_len_movements)
        result_hits = cls.order_by_len(p1_len_hits, p2_len_hits)
        if result_buttons is not None:
            return result_buttons
        elif result_movements is not None:
            return result_movements
        elif result_hits is not None:
            return result_hits
        return "player1"

    @classmethod
    def order_by_len(cls, player1_len, player2_len):
        if player1_len == player2_len:
            return None
        elif player1_len > player2_len:
            return "player1"
        else:
            return "player2"


def main(player_json):

    num_plays = len(player_json["player1"]["movimientos"])
    player_1_movements = player_json["player1"]["movimientos"]
    player_1_hits = player_json["player1"]["golpes"]
    player_2_movements = player_json["player2"]["movimientos"]
    player_2_hits = player_json["player2"]["golpes"]
    tonyn_player1 = Player1CreateService.execute("Tonyn", player_1_movements, player_1_hits)
    arnaldor_player2 = Player1CreateService.execute("Arnaldor", player_2_movements, player_2_hits)
    StartOfFightService.execute(tonyn_player1, arnaldor_player2, num_plays)

    print(tonyn_player1, arnaldor_player2)


p = {
    "player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
    "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]},
}

main(p)
