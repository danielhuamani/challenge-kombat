from domain.models import PlayerDomain, PlayerAttackDomain
from domain.constants import (
    PlayerBaseEnergyByAttack,
    Player1CombinationEnergyByAttack,
    Player2CombinationEnergyByAttack,
    Player1CombinationNameByAttack,
    Player2CombinationNameByAttack,
    MovementsNameEnum,
    HitsNameEnum,
)
from functools import reduce


class PlayerCreateService:
    enum_combination_basic_energy = PlayerBaseEnergyByAttack
    enum_hits_name = HitsNameEnum
    enum_movements_name = MovementsNameEnum
    enum_special_attack_name = None
    enum_special_combination_energy_by_attack = None

    @classmethod
    def execute(cls, name, movements, hits):
        num_rounds = len(movements)
        p = PlayerDomain(name)
        attacks = []
        for x in range(num_rounds):
            is_special_attack = cls.get_is_special_attack(movements[x], hits[x])
            attack_or_movement_name = cls.get_name_of_attack_or_movement(
                p.name, movements[x], hits[x], is_special_attack
            )
            energy_attack = cls.get_energy_by_attack(movements[x], hits[x], is_special_attack)
            attacks.append(
                PlayerAttackDomain(movements[x], hits[x], energy_attack, is_special_attack, attack_or_movement_name)
            )
        p.update_strike(attacks)
        return p

    @classmethod
    def get_is_special_attack(cls, movement, hit):
        special_combination = f"{movement}{hit}"
        is_special_attack = False
        for strike in cls.enum_special_combination_energy_by_attack:
            if strike.name in special_combination and len(special_combination) >= len(strike.name):
                is_special_attack = True
                break
        return is_special_attack

    @classmethod
    def get_energy_by_special_attack(cls, movement, hit):
        special_combination = f"{movement}{hit}"
        energy = 0
        for strike in cls.enum_special_combination_energy_by_attack:
            if strike.name in special_combination:
                energy = strike.value
                break
        return energy

    @classmethod
    def get_energy_by_hit(cls, hit):
        if hit in cls.enum_combination_basic_energy.__members__:
            return cls.enum_combination_basic_energy[hit].value
        return None

    @classmethod
    def get_special_attack_name(cls, special_combination):
        name = None
        for strike in cls.enum_special_attack_name:
            if strike.name in special_combination and len(special_combination) >= len(strike.name):
                name = strike.value
                break
        return name

    @classmethod
    def get_movements_name(cls, movement, has_hit):
        movements_name = []
        len_movement = len(movement)
        if len_movement == 1:
            return cls.enum_movements_name[movement].value
        for index, mov in enumerate(movement, 1):
            movements_name.append(cls.enum_movements_name[mov].value)
            if not has_hit and index == len_movement - 1:
                movements_name.append(" y ")
            elif index != len_movement:
                movements_name.append(", ")
        return "".join(movements_name)

    @classmethod
    def get_hit_name(cls, hit):
        return cls.enum_hits_name[hit].value

    @classmethod
    def get_name_of_attack_or_movement(cls, name, movement, hit, is_special_attack):
        message = "no hace nada"
        special_combination = f"{movement}{hit}"
        if is_special_attack:
            attack_name = cls.get_special_attack_name(special_combination)
            message = f"{name} {attack_name}"
        else:
            movements_name = cls.get_movements_name(movement, bool(hit))
            if hit:
                hit_name = cls.get_hit_name(hit)
                message = f"{name} {movements_name} y {hit_name}"
            else:
                message = f"{name} {movements_name}"
        return message

    @classmethod
    def get_energy_by_attack(cls, movement, hit, is_special_attack):
        if is_special_attack:
            return cls.get_energy_by_special_attack(movement, hit)
        elif cls.get_energy_by_hit(hit) is not None:
            return cls.get_energy_by_hit(hit)
        return 0


class Player1CreateService(PlayerCreateService):
    enum_special_combination_energy_by_attack = Player1CombinationEnergyByAttack
    enum_special_attack_name = Player1CombinationNameByAttack


class Player2CreateService(PlayerCreateService):
    enum_special_combination_energy_by_attack = Player2CombinationEnergyByAttack
    enum_special_attack_name = Player2CombinationNameByAttack


class StartOfFightService:
    @classmethod
    def execute(cls, player1, player2):
        num_rounds = cls.get_num_rounds(player1, player2)
        players = [player1, player2]
        if cls.order_by(player1, player2) == "player2":
            players.reverse()
        player_win = None
        messages = []
        for x in range(num_rounds):
            player_first = players[0]
            player_second = players[1]
            if player_first.round_max() > x:
                player_first_message = cls.send_message_by_attack(player_first, player_second, x)
                messages.append(player_first_message)
                cls.reduce_energy(player_second, player_first.attacks[x].energy_attack)
                if not cls.is_valid_energy(player_second):
                    player_win = player_first
                    break
            if player_second.round_max() > x:
                player_second_message = cls.send_message_by_attack(player_second, player_first, x)
                cls.reduce_energy(player_first, player_second.attacks[x].energy_attack)
                messages.append(player_second_message)
                if not cls.is_valid_energy(player_first):
                    player_win = player_second
                    break
        messages.append(cls.send_message_by_win(player_win))
        return messages

    @classmethod
    def get_num_rounds(cls, player1, player2):
        return max([player1.round_max(), player2.round_max()])

    @classmethod
    def reduce_energy(cls, player_defend, energy):
        player_defend.reduce_energy(energy)
        return player_defend

    @classmethod
    def send_message_by_attack(cls, player_attack, player_defend, num_round):
        attack = player_attack.attacks[num_round]
        if attack.has_simple_attack():
            message = f"{attack.name_of_attack_or_movement} al pobre {player_defend.name}"
        else:
            message = f"{attack.name_of_attack_or_movement}"
        return message

    @classmethod
    def send_message_by_win(cls, player_win):
        return f"{player_win.name} Gana la pelea y aun le queda {player_win.energy} de energia"

    @classmethod
    def is_valid_energy(cls, player):
        return player.has_energy()

    @classmethod
    def order_by(cls, player1, player2):
        p1_len_movements = reduce(lambda x, y: x + len(y.movement), player1.attacks, 0)
        p1_len_hits = reduce(lambda x, y: x + len(y.hit), player1.attacks, 0)
        p2_len_movements = reduce(lambda x, y: x + len(y.movement), player2.attacks, 0)
        p2_len_hits = reduce(lambda x, y: x + len(y.hit), player2.attacks, 0)
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
            return "player2"
        else:
            return "player1"


def main(player_json):

    num_rounds = len(player_json["player1"]["movimientos"])
    player_1_movements = player_json["player1"]["movimientos"]
    player_1_hits = player_json["player1"]["golpes"]
    player_2_movements = player_json["player2"]["movimientos"]
    player_2_hits = player_json["player2"]["golpes"]
    tonyn_player1 = Player1CreateService.execute("Tonyn", player_1_movements, player_1_hits)
    arnaldor_player2 = Player2CreateService.execute("Arnaldor", player_2_movements, player_2_hits)
    result = StartOfFightService.execute(tonyn_player1, arnaldor_player2)
    result = "\n".join(result)
    print(result)


p = {
    "player1": {"movimientos": ["DSD", "S"], "golpes": ["P", ""]},
    "player2": {"movimientos": ["", "ASA", "DA", "AAA", "", "SA"], "golpes": ["P", "", "P", "K", "K", "K"]},
}


main(p)
# PlayerDomain(
#     name="Tonyn",
#     movements=["D", "DSD", "S", "DSD", "SD"],
#     hits=["K", "P", "", "K", "P"],
#     attacks=[
#         PlayerAttackDomain(movement="D", hit="K", energy_attack=1, is_special_attack=False),
#         PlayerAttackDomain(movement="DSD", hit="P", energy_attack=0, is_special_attack=True),
#         PlayerAttackDomain(movement="S", hit="", energy_attack=0, is_special_attack=False),
#         PlayerAttackDomain(movement="DSD", hit="K", energy_attack=0, is_special_attack=True),
#         PlayerAttackDomain(movement="SD", hit="P", energy_attack=1, is_special_attack=False),
#     ],
#     energy=6,
# )
# PlayerDomain(
#     name="Arnaldor",
#     movements=["SA", "SA", "SA", "ASA", "SA"],
#     hits=["K", "", "K", "P", "P"],
#     attacks=[
#         PlayerAttackDomain(movement="SA", hit="K", energy_attack=1, is_special_attack=False),
#         PlayerAttackDomain(movement="SA", hit="", energy_attack=0, is_special_attack=False),
#         PlayerAttackDomain(movement="SA", hit="K", energy_attack=1, is_special_attack=False),
#         PlayerAttackDomain(movement="ASA", hit="P", energy_attack=1, is_special_attack=False),
#         PlayerAttackDomain(movement="SA", hit="P", energy_attack=1, is_special_attack=False),
#     ],
#     energy=6,
# )
