import pytest
from board import Board
from unittest.mock import MagicMock

# Exemplos de objetos de teste
class MockPiece:
    def __init__(self, position, color, is_king=False):
        self.position = position
        self.color = color
        self.is_king = is_king
        self.has_eaten = False
    
    def get_position(self):
        return self.position
    
    def get_color(self):
        return self.color
    
    def is_king(self):
        return self.is_king
    
    def set_position(self, position):
        self.position = position

    def set_is_king(self, is_king):
        self.is_king = is_king
    
    def set_has_eaten(self, has_eaten):
        self.has_eaten = has_eaten

@pytest.fixture
def board_setup():
    pieces = [
        MockPiece("12", "W"),
        MockPiece("14", "B"),
        MockPiece("24", "W")
    ]
    return Board(pieces, "W")

def test_get_color_up(board_setup):
    assert board_setup.get_color_up() == "W"

def test_get_pieces(board_setup):
    pieces = board_setup.get_pieces()
    assert len(pieces) == 3
    assert pieces[0].get_position() == "12"

def test_has_piece(board_setup):
    assert board_setup.has_piece(12) is True
    assert board_setup.has_piece(13) is False

def test_get_row_number(board_setup):
    assert board_setup.get_row_number(5) == 1
    assert board_setup.get_row_number(16) == 4

def test_get_col_number(board_setup):
    assert board_setup.get_col_number(5) == 3
    assert board_setup.get_col_number(16) == 0

def test_get_winner(board_setup):
    # Simula um estado de vitória
    board_setup.pieces = [MockPiece("12", "W"), MockPiece("14", "W")]
    assert board_setup.get_winner() == "W"

    # Simula um estado de empate
    board_setup.pieces.append(MockPiece("24", "B"))
    assert board_setup.get_winner() is None


def test_exceptions_and_error_handling():
    with pytest.raises(IndexError):
        board = Board([], "W")
        board.get_piece_by_index(0)  # Índice inválido

def test_get_piece_by_invalid_index(board_setup):
    """
    Testa acesso a um índice inválido no tabuleiro.
    """
    with pytest.raises(IndexError):
        board_setup.get_piece_by_index(100)  # Índice fora do intervalo

def test_message_on_invalid_position(board_setup):
    """
    Testa o comportamento para posições inválidas, como retornar False.
    """
    invalid_position = 50  # Uma posição fora do tabuleiro
    result = board_setup.has_piece(invalid_position)
    assert result is False, f"Esperado False para posição inválida {invalid_position}, mas obtido {result}."


def test_loop_through_pieces(board_setup):
    positions = [piece.get_position() for piece in board_setup.get_pieces()]
    assert positions == ["12", "14", "24"], "A iteração pelo loop não retornou as posições corretas."


def test_user_inputs(board_setup):
    """
    Testa entradas inválidas no método has_piece.
    """
    invalid_inputs = ["invalid", -1, None, 3.14]  # Tipos de entrada inválidos

    for invalid_input in invalid_inputs:
        result = board_setup.has_piece(invalid_input)
        assert result is False, f"Esperado False para entrada inválida {invalid_input}, mas obtido {result}."

        




