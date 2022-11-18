import pytest
from app.applicant.services.player import Player1CreateService, PlayerCreateService
from app.domain.models import PlayerAttackDomain


class TestPlayerCreateService:
    @pytest.mark.parametrize(
        "input,expected",
        [("P", 1), ("K", 1), ("", 0)],
    )
    def test_get_energy_by_hit_success(self, input, expected):
        assert PlayerCreateService.get_energy_by_hit(input) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (["DSD", False], "va a la derecha, se agacha y va a la derecha"),
            (["DSD", True], "va a la derecha, se agacha, va a la derecha"),
            (["D", False], "va a la derecha"),
            (["S", True], "se agacha"),
            (["", False], ""),
        ],
    )
    def test_get_movements_name_success(self, input, expected):
        assert PlayerCreateService.get_movements_name(input[0], input[1]) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [("P", 1), ("K", 1), ("", 0)],
    )
    def test_get_energy_by_hit_success(self, input, expected):
        assert PlayerCreateService.get_energy_by_hit(input) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [("P", "le da un puñetazo"), ("K", "da una patada")],
    )
    def test_get_hit_name_success(self, input, expected):
        assert PlayerCreateService.get_hit_name(input) == expected


class TestPlayer1CreateService:
    @pytest.mark.parametrize(
        "input,expected",
        [(["DSD", "P"], True), (["SD", "K"], True), (["AADSD", "P"], True), (["DSDAA", "P"], False)],
    )
    def test_get_is_special_attack_success(self, input, expected):
        assert Player1CreateService.get_is_special_attack(input[0], input[1]) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [(["DSD", "P"], 3), (["SD", "K"], 2), (["AADSD", "P"], 3), (["DSDAA", "P"], 0)],
    )
    def test_get_energy_by_special_attack_success(self, input, expected):
        assert Player1CreateService.get_energy_by_special_attack(input[0], input[1]) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            ("DSDP", "usa un Taladoken"),
            ("SDK", "conecta un Remuyuken"),
            ("AADSDP", "usa un Taladoken"),
            ("DSDAAP", ""),
        ],
    )
    def test_get_special_attack_name_success(self, input, expected):
        assert Player1CreateService.get_special_attack_name(input) == expected

    @pytest.mark.parametrize(
        "input,expected",
        [
            (["DSD", "P"], 3),
            (["SD", "K"], 2),
            (["SSDSD", "P"], 3),
            (["S", ""], 0),
            (["D", ""], 0),
            (["", "P"], 1),
            (["", "K"], 1),
        ],
    )
    def test_get_energy_by_attack_success(self, input, expected):
        assert Player1CreateService.get_energy_by_attack(input[0], input[1]) == expected

    def test_execute_case_1_success(self):
        movements = ["D", "DSD", "S", "DSD", "SD"]
        hits = ["K", "P", "", "K", "P"]
        player1 = Player1CreateService.execute("Tonyn", movements, hits)
        attacks = [
            PlayerAttackDomain("D", "K", 1, False, "Tonyn va a la derecha y da una patada"),
            PlayerAttackDomain("DSD", "P", 3, True, "Tonyn usa un Taladoken"),
            PlayerAttackDomain("S", "", 0, False, "Tonyn se agacha"),
            PlayerAttackDomain("DSD", "K", 2, True, "Tonyn conecta un Remuyuken"),
            PlayerAttackDomain("SD", "P", 1, False, "Tonyn se agacha, va a la derecha y le da un puñetazo"),
        ]
        assert player1.attacks == attacks
        assert player1.energy == 6

    def test_execute_case_2_success(self):
        movements = ["SDD", "DSD", "SA", "DSD"]
        hits = ["K", "P", "K", "P"]
        player1 = Player1CreateService.execute("Tonyn", movements, hits)
        attacks = [
            PlayerAttackDomain(
                "SDD", "K", 1, False, "Tonyn se agacha, va a la derecha, va a la derecha y da una patada"
            ),
            PlayerAttackDomain("DSD", "P", 3, True, "Tonyn usa un Taladoken"),
            PlayerAttackDomain("SA", "K", 0, False, "Tonyn no hace nada"),
            PlayerAttackDomain("DSD", "P", 3, True, "Tonyn usa un Taladoken"),
        ]
        assert player1.attacks == attacks
        assert player1.energy == 6
