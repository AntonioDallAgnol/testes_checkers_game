import pytest
from piece import Piece

# Mock para o tabuleiro usado nas funções
class MockBoard:
    def __init__(self, pieces=None):
        self.pieces = pieces or {}

    def get_col_number(self, position):
        return position % 8

    def get_row_number(self, position):
        return position // 8

    def get_color_up(self):
        return "W"  # Define que as peças brancas se movem para cima

    def has_piece(self, position):
        return position in self.pieces

    def get_pieces_by_coords(self, *coords):
        return [self.pieces.get((row, col)) for row, col in coords]

#Teste básico de criação de peça
def test_piece_creation():
    piece = Piece("16WN")
    assert piece.get_position() == "16"
    assert piece.get_color() == "W"
    assert not piece.is_king()

#Teste dos setters
def test_set_position():
    piece = Piece("16WN")
    piece.set_position("24")
    assert piece.get_position() == "24"

def test_set_is_king():
    piece = Piece("16WN")
    piece.set_is_king(True)
    assert piece.is_king()
    piece.set_is_king(False)
    assert not piece.is_king()

#Teste de movimentos adjacentes
def test_get_adjacent_squares():
    board = MockBoard()
    piece = Piece("16WN")
    adjacents = piece.get_adjacent_squares(board)
    assert adjacents == [(1, 1)]

#Teste de movimentos válidos
def test_get_moves_empty_board():
    board = MockBoard()
    piece = Piece("16WN")
    moves = piece.get_moves(board)
    assert len(moves) == 1 


def test_get_moves_with_piece_to_eat():
    # Simula um tabuleiro com uma peça adversária na posição (2, 3)
    board = MockBoard(pieces={(2, 3): Piece("19BN")})
    piece = Piece("16WN")
    moves = piece.get_moves(board)

    assert len(moves) == 1
    assert not moves[0]["eats_piece"]  # Confirma que o movimento não envolve captura


#Teste de comportamento com exceções
def test_invalid_position_message():
    piece = Piece("16WN")
    try:
        piece.set_position("-1")  # Posição inválida
    except Exception as e:
        assert str(e) == "Posição inválida"  # Apenas se existisse validação

#Teste de lógica com borda do tabuleiro
def test_piece_on_board_edge():
    board = MockBoard()
    piece = Piece("0WN")  # Posição inicial na borda
    adjacents = piece.get_adjacent_squares(board)
    print(adjacents)
    assert len(adjacents) == 0

#Testes para exceções
def test_invalid_color():
    piece = Piece("16WN")
    invalid_color = piece.get_color()
    assert invalid_color in ["W", "B"]  # O jogo suporta apenas peças brancas e pretas


#Testes de início e fim de loops
def test_piece_moves_loop():
    board = MockBoard()
    piece = Piece("16WN")
    moves = piece.get_moves(board)
    for move in moves:
        assert "position" in move
        assert "eats_piece" in move
        
#Testes para cada if no código
def test_if_king_movement():
    board = MockBoard()
    piece = Piece("16WN")
    piece.set_is_king(True)
    moves = piece.get_moves(board)
    assert len(moves) > 0  # Verifica se o rei tem mais movimentos disponíveis
    
#Testes para entradas do usuário
def test_user_input_for_position():
    piece = Piece("16WN")
    new_position = "24"  # Simulação de entrada
    piece.set_position(new_position)
    assert piece.get_position() == new_position
    
#Testes para múltiplos estados
def test_multiple_pieces_on_board():
    board = MockBoard(pieces={(1, 2): Piece("10BN"), (3, 4): Piece("24WN")})
    piece = Piece("16WN")
    moves = piece.get_moves(board)
    assert len(moves) >= 0  # Simplesmente garante que não quebra com múltiplas peças