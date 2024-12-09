import pytest
from board import Board
from ai import AI

class MockPiece:
    def __init__(self, position, color, is_king=False):
        self.position = position
        self.color = color
        self._is_king = is_king  # atributo privado para armazenar o estado

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_color(self):
        return self.color

    def is_king(self):
        return self._is_king

    def set_is_king(self, value):
        self._is_king = value

    def set_has_eaten(self, value):
        self.has_eaten = value

    def get_moves(self, board):
        moves = []
        if self.color == "B":
            moves.append({"position": int(self.position) + 4, "eats_piece": False})
        else:
            moves.append({"position": int(self.position) - 4, "eats_piece": False})
        return moves

@pytest.fixture
def sample_board():
    pieces = [
        MockPiece("12", "B"),
        MockPiece("14", "W"),
        MockPiece("24", "B", is_king=True),
    ]
    return Board(pieces, color_up="W")

@pytest.fixture
def ai_player():
    return AI(color="B")

def test_minimax_maximizing(ai_player, sample_board):
    # maximização
    result = ai_player.minimax(sample_board, is_maximizing=True, depth=2, turn="B")
    assert isinstance(result, int)  # verificar se retorno é um inteiro

def test_minimax_minimizing(ai_player, sample_board):
    # minimização
    result = ai_player.minimax(sample_board, is_maximizing=False, depth=2, turn="W")
    assert isinstance(result, int)

def test_get_move(ai_player, sample_board):
    move = ai_player.get_move(sample_board)
    assert "position_to" in move
    assert "position_from" in move
    assert move["position_to"] in [16, 28]

def test_get_value_victory(ai_player, sample_board):
    # vitória
    sample_board.pieces = [MockPiece("12", "B")]
    value = ai_player.get_value(sample_board)
    assert value == 2

def test_get_value_defeat(ai_player, sample_board):
    # derrota
    sample_board.pieces = [MockPiece("12", "W")]
    value = ai_player.get_value(sample_board)
    assert value == -2

def test_get_value_draw(ai_player, sample_board):
    # empate
    sample_board.pieces = [
        MockPiece("12", "B"),
        MockPiece("14", "W"),
    ]
    value = ai_player.get_value(sample_board)
    assert value == 0

def test_conditional_logic(ai_player, sample_board):
    # movimentos de salto
    sample_board.pieces = [
        MockPiece("11", "B"),
        MockPiece("15", "W"),
    ]
    move = ai_player.get_move(sample_board)
    assert move["position_to"] == 15