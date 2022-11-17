from enum import IntEnum, Enum


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
    A = "retrocede"
    D = "avanza"


class HitsNameEnum(Enum):
    P = "le da un puñetazo"
    K = "da una patada"
