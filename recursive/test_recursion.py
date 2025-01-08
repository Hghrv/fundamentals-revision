import pytest
from recursive.recursion import ghost_buster
from recursive.ghost_data import ghost_data, nested_ghost_data

class TestGhostBuster():
    def test_ghost_buster_finds_ghost_when_passed(self):
        ghosts = [{'is_ghost': True}]
        found_ghosts = ghost_buster(ghosts)
        assert found_ghosts == 1

    @pytest.mark.skip
    def test_ghost_buster_finds_ghosts_when_passed_multiple(self):
        ghosts = [{'is_ghost': True}, {'is_ghost': True}]
        found_ghosts = ghost_buster(ghosts)
        assert found_ghosts == 2

    @pytest.mark.skip
    def test_ghost_buster_ignores_non_ghostly_entities(self):
        ghosts = [{'is_ghost': True}, {'is_ghost': False}]
        found_ghosts = ghost_buster(ghosts)
        assert found_ghosts == 1

    @pytest.mark.skip
    def test_ghost_buster_can_deal_with_large_amounts_of_data(self):
        ghosts = ghost_data
        found_ghosts = ghost_buster(ghosts)
        assert found_ghosts == 510

    @pytest.mark.skip
    def test_ghost_buster_can_deal_with_nested_data(self):
        ghosts = nested_ghost_data
        found_ghosts = ghost_buster(ghosts)
        assert found_ghosts == 510