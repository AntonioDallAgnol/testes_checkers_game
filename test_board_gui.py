import pytest
import pygame
from unittest.mock import Mock
from board_gui import BoardGUI

@pytest.fixture
def mock_board(): # cria um board falso
    board = Mock()
    board.get_pieces.return_value = [
        Mock(get_position=lambda: 1, get_color=lambda: "B", is_king=lambda: False),
        Mock(get_position=lambda: 2, get_color=lambda: "W", is_king=lambda: True),
    ]
    board.get_row_number.side_effect = lambda pos: pos // 8
    board.get_col_number.side_effect = lambda pos: pos % 8
    return board

@pytest.fixture
def board_gui(mock_board):
    return BoardGUI(mock_board)

def test_get_piece_properties(board_gui, mock_board):
    pieces = board_gui.get_piece_properties(mock_board)
    assert len(pieces) == 2
    assert pieces[0]["color"] == "B"
    assert pieces[1]["is_king"]

def test_hide_and_show_piece(board_gui):
    board_gui.hide_piece(1)
    assert board_gui.hidden_piece == 1
    revealed = board_gui.show_piece()
    assert revealed == 1
    assert board_gui.hidden_piece == -1

def test_get_piece_by_index(board_gui):
    piece = board_gui.get_piece_by_index(0)
    assert piece["color"] == "B"

def test_set_and_get_move_marks(board_gui):
    board_gui.set_move_marks([(1, 2), (3, 4)])
    move_marks = board_gui.get_move_marks()
    assert len(move_marks) == 2

def test_get_position_by_rect(board_gui):
    rect = pygame.Rect(90, 90, 44, 44)
    position = board_gui.get_position_by_rect(rect)
    assert position == 4

def test_get_piece_on_mouse(board_gui):
    mouse_pos = (50, 50)
    piece = board_gui.get_piece_on_mouse(mouse_pos)
    
    # resultado esperado
    expected_piece = {
        "index": 0,
        "piece": {"rect": pygame.Rect(34, 34, 41, 41), "color": "B", "is_king": False},
    }
    assert piece == expected_piece

def test_set_pieces(board_gui):
    custom_pieces = [{"color": "W", "is_king": False, "rect": pygame.Rect(0, 0, 10, 10)}]
    board_gui.set_pieces(custom_pieces)
    assert len(board_gui.pieces) == 1
    assert board_gui.pieces[0]["color"] == "W"
