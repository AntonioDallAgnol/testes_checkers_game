import pytest
from utils import (
    get_position_with_row_col,
    get_piece_position,
    get_piece_gui_coords,
    get_surface_mouse_offset,
)

#Testes para get_position_with_row_col
def test_get_position_with_row_col():
    assert get_position_with_row_col(0, 0) == 0  # Canto superior esquerdo
    assert get_position_with_row_col(0, 2) == 1  # Segunda coluna
    assert get_position_with_row_col(1, 0) == 4  # Segunda linha, primeira coluna
    assert get_position_with_row_col(7, 6) == 31  # Canto inferior direito

def test_get_position_with_row_col_invalid():
    with pytest.raises(TypeError):
        get_position_with_row_col("row", 2)  # Entrada inválida
    with pytest.raises(TypeError):
        get_position_with_row_col(0, "col")  # Entrada inválida

#Testes para get_piece_position
def test_get_piece_position():
    top_left_coords = (10, 10)
    square_dist = 50
    coords = (60, 110)  # Coordenadas de clique
    position = get_piece_position(coords, square_dist, top_left_coords)
    assert position == 8  # Calculado a partir dos valores

def test_get_piece_position_edge():
    top_left_coords = (0, 0)
    square_dist = 100
    coords = (800, 700)  # Valores máximos no tabuleiro (8x8)
    position = get_piece_position(coords, square_dist, top_left_coords)
    assert position == 32  # Última posição válida do tabuleiro

#Testes para get_piece_gui_coords
def test_get_piece_gui_coords():
    top_left_coords = (10, 10)
    square_dist = 50
    coords = (3, 2)  # Posição da peça na matriz
    gui_coords = get_piece_gui_coords(coords, square_dist, top_left_coords)
    assert gui_coords == (160, 160)  # Coordenadas esperadas no GUI

def test_get_piece_gui_coords_odd_row():
    top_left_coords = (10, 10)
    square_dist = 50
    coords = (1, 2)  # Linha ímpar
    gui_coords = get_piece_gui_coords(coords, square_dist, top_left_coords)
    assert gui_coords == (160, 60)  # Ajuste para linha ímpar

#Testes para get_surface_mouse_offset
def test_get_surface_mouse_offset():
    surface_pos = (100, 200)
    mouse_pos = (120, 220)
    offset = get_surface_mouse_offset(surface_pos, mouse_pos)
    assert offset == (-20, -20)  # Diferença esperada

def test_get_surface_mouse_offset_negative():
    surface_pos = (50, 50)
    mouse_pos = (100, 100)
    offset = get_surface_mouse_offset(surface_pos, mouse_pos)
    assert offset == (-50, -50)  # Diferença esperada
