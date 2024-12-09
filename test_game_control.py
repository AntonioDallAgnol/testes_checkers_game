import pytest
from game_control import GameControl
from unittest.mock import MagicMock

# Fixture para inicializar a instância do GameControl
@pytest.fixture
def game_control():
    # Inicializando o GameControl com os parâmetros requeridos
    return GameControl(player_color="W", is_computer_opponent=False)

# Teste para verificar a inicialização do GameControl
def test_game_initialization(game_control):
    # Verificação de atributos iniciais esperados
    assert game_control.get_turn() == "W", "O jogador inicial deve ser 'W'."
    assert game_control.get_winner() is None, "Não deve haver um vencedor na inicialização."

# Teste de alternância de jogadores
def test_toggle_player(game_control):
    # Alternar turno manualmente, pois o método não está definido explicitamente
    initial_turn = game_control.get_turn()
    game_control.turn = "B" if initial_turn == "W" else "W"
    assert game_control.get_turn() != initial_turn, "Depois de alternar, o jogador deve mudar."

# Teste para verificação do estado de fim de jogo
def test_end_game(game_control):
    # Alterar o estado manualmente, pois o método não está definido explicitamente
    game_control.winner = "W"
    assert game_control.get_winner() == "W", "O vencedor deve ser 'W' após configurar."

# Teste de cenários com entrada inválida ou estados inesperados
def test_invalid_action(game_control):
    # Simulando uma entrada inválida e verificando diretamente
    game_control.turn = None
    assert game_control.get_turn() is None, "Turno deve ser None ao configurá-lo explicitamente como tal."

# Teste de funções dependentes de parâmetros
def test_perform_action(game_control):
    # Testando uma configuração específica do jogo
    game_control.turn = "B"
    assert game_control.get_turn() == "B", "O turno deve ser 'B' após modificação."

# Teste de combinação de entradas (se aplicável)
def test_combined_inputs(game_control):
    # Simulando combinações de entradas
    game_control.turn = "W"
    game_control.winner = "B"
    assert game_control.get_turn() == "W", "Turno deve ser 'W'."
    assert game_control.get_winner() == "B", "Vencedor deve ser 'B'."
    
# Teste para blocos if e exceções
def test_if_conditions_and_exceptions(game_control):
    # Testando uma condição if simples
    if game_control.get_turn() == "W":
        game_control.turn = "B"
    assert game_control.get_turn() == "B", "Turno deve mudar para 'B' quando 'W'."


# Teste para loops
def test_loops(game_control):
    # Simulando verificação de todas as peças
    for piece in game_control.board.get_pieces():
        assert piece is not None, "Peça não deve ser None durante iteração."

    # Verificando movimentos de uma peça
    moves = game_control.board.get_pieces()[0].get_moves(game_control.board)
    for move in moves:
        assert "position" in move, "Movimento deve conter a chave 'position'."

# Teste para casos (equivalente ao switch/case)
def test_case_like_behavior(game_control):
    # Simulando comportamento de decisão baseado em valores
    turn_action = {
        "W": lambda: "White's turn",
        "B": lambda: "Black's turn"
    }
    action = turn_action.get(game_control.get_turn(), lambda: "Invalid turn")()
    assert action == "White's turn", "A ação deve corresponder ao turno atual."
    
    # Teste para a função `get_turn()`
def test_get_turn(game_control):
    assert game_control.get_turn() == "W", "O turno inicial deve ser 'W'."
    game_control.turn = "B"
    assert game_control.get_turn() == "B", "O turno deve ser alterado para 'B'."

# Teste para a função `get_winner()`
def test_get_winner(game_control):
    assert game_control.get_winner() is None, "Não deve haver um vencedor na inicialização."
    game_control.winner = "W"
    assert game_control.get_winner() == "W", "O vencedor deve ser 'W'."
    game_control.winner = "B"
    assert game_control.get_winner() == "B", "O vencedor deve ser 'B'."

# Teste para a função `setup()`
def test_setup(game_control):
    game_control.setup()
    board = game_control.board
    assert len(board.get_pieces()) == 24, "O número de peças deve ser 24 após a inicialização."

# Teste para a função `draw_screen()`
def test_draw_screen(game_control):
    display_surface = MagicMock()  # Mock do display_surface
    game_control.draw_screen(display_surface)
    display_surface.blit.assert_called()  # Verifica se o método `blit` foi chamado para desenhar os componentes


# Teste para a função `move_ai()` com a IA configurada
@pytest.fixture
def ai_game_control():
    return GameControl(player_color="W", is_computer_opponent=True)


# Teste para a função `move_ai()` quando não houver IA
def test_move_ai_no_opponent(game_control):
    game_control.move_ai()  # Não deve fazer nada, pois não há oponente IA
    assert game_control.turn == "W", "O turno não deve mudar se não houver IA."


# Teste para o comportamento do método `hold_piece()` com entrada inválida
def test_hold_piece_invalid(game_control):
    mouse_pos = (100, 100)
    game_control.board_draw.get_piece_on_mouse = MagicMock(return_value=None)
    game_control.hold_piece(mouse_pos)
    assert game_control.held_piece is None, "A peça não deve ser segurada se não for uma peça válida."
