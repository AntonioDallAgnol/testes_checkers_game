import pytest
from unittest.mock import MagicMock
from checkers import main
from game_control import GameControl

@pytest.fixture
def game_control():
    # Criação de uma instância de GameControl para testes (sem modo CPU)
    return GameControl("W", False)

def test_initial_turn(game_control):
    # Testa se o turno inicial é configurado corretamente
    assert game_control.get_turn() == "W"

def test_get_winner_no_winner(game_control):
    # Testa se não há vencedor no início
    assert game_control.get_winner() is None

def test_hold_piece_invalid_position(game_control):
    # Testa tentativa de pegar uma peça em uma posição inválida
    invalid_position = (-1, -1)
    result = game_control.hold_piece(invalid_position)
    assert not result

def test_release_piece_without_holding(game_control):
    # Testa liberar peça sem ter segurado nenhuma
    result = game_control.release_piece()
    assert not result

def test_game_loop(game_control):
    for _ in range(10):  # Simula 10 turnos do jogo
        assert game_control.get_turn() in ["W", "B"]
        if game_control.get_winner():
            break  # Termina o loop se houver vencedor
    assert game_control.get_winner() is None  # Garantia de que ninguém venceu ainda

def test_move_conditions(game_control):
    valid_position = (2, 2)  # Substituir por uma posição válida
    game_control.hold_piece(valid_position)
    assert game_control.get_turn() == "W"  # Verifica condição do turno

def test_get_turn_returns(game_control):
    # Testa os valores retornados pelo turno
    assert game_control.get_turn() in ["W", "B"]