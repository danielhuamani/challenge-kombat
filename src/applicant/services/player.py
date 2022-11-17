from domain.models import PlayerDomain, PlayerAttackDomain
from domain.constants import (
    Player1CombinationEnergyByAttack,
    Player2CombinationEnergyByAttack,
    Player1CombinationNameByAttack,
    Player2CombinationNameByAttack,
)
from applicant.services.shared import PlayerCreateService
from functools import reduce


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


class Player1CreateService(PlayerCreateService):
    enum_special_combination_energy_by_attack = Player1CombinationEnergyByAttack
    enum_special_attack_name = Player1CombinationNameByAttack


class Player2CreateService(PlayerCreateService):
    enum_special_combination_energy_by_attack = Player2CombinationEnergyByAttack
    enum_special_attack_name = Player2CombinationNameByAttack
