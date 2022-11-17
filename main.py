from app.infrastructure.rest.fastapi_app import init_application


# p = {
#     "player1": {"movimientos": ["DSD", "S"], "golpes": ["P", ""]},
#     "player2": {"movimientos": ["", "ASA", "DA", "AAA", "", "SA"], "golpes": ["P", "", "P", "K", "K", "K"]},
# }


# main(p)
app = init_application()
