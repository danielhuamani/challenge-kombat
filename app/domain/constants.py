from enum import Enum, IntEnum


class PlayerBaseEnergyByAttack(IntEnum):
    P = 1
    K = 1


class Player1CombinationEnergyByAttack(IntEnum):
    DSDP = 3
    SDK = 2


class Player2CombinationEnergyByAttack(IntEnum):
    SAK = 3
    ASAP = 2


class Player1CombinationNameByAttack(Enum):
    DSDP = "usa un Taladoken"
    SDK = "conecta un Remuyuken"


class Player2CombinationNameByAttack(Enum):
    SAK = "conecta un Remuyuken"
    ASAP = "usa un Taladoken"


class MovementsNameEnum(Enum):
    W = "salta"
    S = "se agacha"
    A = "va a la izquierda"
    D = "va a la derecha"


class Player1MovementsNameEnum(Enum):
    W = "salta"
    S = "se agacha"
    D = "va a la derecha"


class Player2MovementsNameEnum(Enum):
    W = "salta"
    S = "se agacha"
    A = "va a la izquierda"


class HitsNameEnum(Enum):
    P = "le da un puñetazo"
    K = "da una patada"


PLAYER_1 = "player1"
PLAYER_2 = "player2"
