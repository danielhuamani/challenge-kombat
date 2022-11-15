class Player:
    MOVEMENTS = {"W": "Arriba", "S": "Abajo", "A": "Izquierda", "D": "Derecha"}
    HITS = {"P": "Puño", "K": "Patada"}
    LIFE_ENERGY = 6
    DEATH_ENERGY = 0


class TonynPlayer(Player):
    HITS_SPECIAL = {"ASAP": "Taladoken", "SAK": "Remuyuken"}


class ArnaldorPlayer(Player):
    HITS_SPECIAL = {"DSDP": "Taladoken", "SDK": "Remuyuken"}


def main(play_json):
    tonyn_player = TonynPlayer()
    arnaldor_player = ArnaldorPlayer()
    movements_len = len(play_json[0]["player1"]["movimientos"])
    for x in range(movements_len):
        ...


p = {
    "player1": {"movimientos": ["D", "DSD", "S", "DSD", "SD"], "golpes": ["K", "P", "", "K", "P"]},
    "player2": {"movimientos": ["SA", "SA", "SA", "ASA", "SA"], "golpes": ["K", "", "K", "P", "P"]},
}

main(p)
