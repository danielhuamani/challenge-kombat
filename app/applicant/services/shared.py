from app.domain.models import PlayerDomain, PlayerAttackDomain
from app.domain.constants import (
    PlayerBaseEnergyByAttack,
    MovementsNameEnum,
    HitsNameEnum,
)


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
        if len_movement:
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
        message = "{name} no hace nada"
        special_combination = f"{movement}{hit}"
        if is_special_attack:
            attack_name = cls.get_special_attack_name(special_combination)
            message = f"{name} {attack_name}"
        else:
            movements_name = cls.get_movements_name(movement, bool(hit))
            if hit:
                hit_name = cls.get_hit_name(hit)
                if movements_name:
                    message = f"{name} {movements_name} y {hit_name}"
                else:
                    message = f"{name} {hit_name}"
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
