import pytest
from unittest.mock import MagicMock
from held_piece import HeldPiece

# Mock para o pygame e sua superfície
class MockSurface:
    def __init__(self, rect):
        self.rect = rect

    def get_rect(self):
        return self.rect

# Mock para o pygame.mouse.get_pos
@pytest.fixture(autouse=True)
def mock_get_mouse_pos(monkeypatch):
    mock_mouse_pos = MagicMock(return_value=(100, 100))
    monkeypatch.setattr("held_piece.get_mouse_pos", mock_mouse_pos)

#Teste de inicialização
def test_held_piece_initialization():
    surface = MockSurface(rect=MagicMock(x=0, y=0, width=50, height=50))
    held_piece = HeldPiece(surface, offset=(10, 20))
    assert held_piece.surface == surface
    assert held_piece.offset == (10, 20)
    assert held_piece.draw_rect == surface.get_rect()

#Teste do método draw_piece
def test_draw_piece():
    surface = MockSurface(rect=MagicMock(x=0, y=0, width=50, height=50))
    display_surface = MagicMock()
    held_piece = HeldPiece(surface, offset=(10, 20))
    held_piece.draw_piece(display_surface)

    # Valida o posicionamento com base no mouse simulado e no offset
    assert held_piece.draw_rect.x == 110
    assert held_piece.draw_rect.y == 120
    display_surface.blit.assert_called_once_with(held_piece.surface, held_piece.draw_rect)

#Teste de colisão (com colisão)
def test_check_collision_with_collision():
    surface = MockSurface(rect=MagicMock(x=0, y=0, width=50, height=50))
    held_piece = HeldPiece(surface, offset=(10, 20))
    rect_list = [MagicMock(colliderect=MagicMock(return_value=True))]

    result = held_piece.check_collision(rect_list)
    assert result == rect_list[0]

#Teste de colisão (sem colisão)
def test_check_collision_no_collision():
    surface = MockSurface(rect=MagicMock(x=0, y=0, width=50, height=50))
    held_piece = HeldPiece(surface, offset=(10, 20))
    rect_list = [MagicMock(colliderect=MagicMock(return_value=False))]

    result = held_piece.check_collision(rect_list)
    assert result is None

#Teste de múltiplas colisões (prioridade)
def test_check_collision_multiple_collisions():
    surface = MockSurface(rect=MagicMock(x=0, y=0, width=50, height=50))
    held_piece = HeldPiece(surface, offset=(10, 20))
    rect1 = MagicMock(colliderect=MagicMock(return_value=True))
    rect2 = MagicMock(colliderect=MagicMock(return_value=True))
    rect_list = [rect1, rect2]

    result = held_piece.check_collision(rect_list)
    assert result == rect1  # Verifica se retorna o primeiro retângulo em caso de múltiplas colisões

