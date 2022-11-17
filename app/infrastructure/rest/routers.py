from fastapi.routing import APIRouter
from fastapi import FastAPI
from app.domain.schemas import PlayersCreateBody
from app.applicant.services.player import Player1CreateService, Player2CreateService, StartOfFightService

router = APIRouter()


@router.post("/play")
def play(players: PlayersCreateBody):
    player_1_movements = players.player1.movimientos
    player_1_hits = players.player1.golpes
    player_2_movements = players.player2.movimientos
    player_2_hits = players.player2.golpes
    tonyn_player1 = Player1CreateService.execute("Tonyn", player_1_movements, player_1_hits)
    arnaldor_player2 = Player2CreateService.execute("Arnaldor", player_2_movements, player_2_hits)
    result = StartOfFightService.execute(tonyn_player1, arnaldor_player2)
    return result


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(router)
    return app
