import pytest
from football_game import FootballGame

@pytest.fixture
def game():
    print("\nGame is being created")
    yield FootballGame(name="Eliminacje", city="Kraków")
    print("Game removed")

@pytest.fixture
def game_with_poland(game):
    print("Team is added")
    game.add_team("Polska")
    yield game
    print("Team removed")

def test_first_team_should_win(game_with_poland):
    game_with_poland.add_team("Szwecja")
    winner = game_with_poland.play()
    assert winner == "Polska"
    game_with_poland.end_game()


def test_there_is_no_winner_if_only_one_team_played(game):
    winner = game.play()
    assert winner is None
    game.end_game()