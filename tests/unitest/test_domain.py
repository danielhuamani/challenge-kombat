from app.domain.models import PlayerAttackDomain


class TestPlayerModels:
    def test_reduce_energy_success(self, player_tonyn):
        player_tonyn.reduce_energy(3)
        assert player_tonyn.energy == 3

    def test_has_energy_success(self, player_tonyn):
        player_tonyn.energy = 0
        assert player_tonyn.has_energy() == False

    def test_update_strike_success(self, player_tonyn):
        attack = PlayerAttackDomain("D", "P", 1, False, "")
        player_tonyn.update_strike([attack])
        assert player_tonyn.attacks == [attack]

    def test_round_max_success(self, player_tonyn):
        player_tonyn.update_strike(
            [
                PlayerAttackDomain("D", "P", 1, False, ""),
                PlayerAttackDomain("D", "P", 1, False, ""),
                PlayerAttackDomain("D", "P", 1, False, ""),
            ]
        )
        assert player_tonyn.round_max() == 3


class TestPlayerAttackModels:
    def test_has_simple_attack_is_true(player_tonyn):
        attack = PlayerAttackDomain("D", "P", 1, False, "")
        assert attack.has_simple_attack() == True

    def test_has_simple_attack_is_true_case_2(player_tonyn):
        attack = PlayerAttackDomain("D", "", 1, False, "")
        assert attack.has_simple_attack() == False

    def test_has_simple_attack_is_false(player_tonyn):
        attack = PlayerAttackDomain("D", "P", 1, True, "")
        assert attack.has_simple_attack() == False
