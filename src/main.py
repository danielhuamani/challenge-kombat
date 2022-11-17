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
