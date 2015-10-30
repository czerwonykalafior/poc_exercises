__author__ = 'CzerwonyKalafior'
__project__ = 'TTT'

"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
#
# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

    print board

    possible_moves = board.get_empty_squares()
    print possible_moves
    best_move = (-1,-1)
    best_score = float('-inf')

    for possible_move in possible_moves:
        temp_board = board.clone()
        temp_board.move(possible_move[0], possible_move[1], player)

        score = max_play(temp_board, player)
        print score, possible_move, player
        if score > best_score:
            print "s", possible_move
            best_move = possible_move
            best_score = score
        # if player == 2:
        #     if score > best_score:
        #         print "x", possible_move
        #         best_move = possible_move
        #         best_score = score
        # elif player == 3:
        #     if score < best_score:
        #         print "o", possible_move
        #         best_move = possible_move
        #         best_score = score

    return best_score, best_move

def min_play(board, player):
    if board.check_win():
        return SCORES[board.check_win()]
    moves = board.get_empty_squares()
    best_move = moves[0]
    best_score = float('inf')
    for move in moves:
        clone = board.clone()
        clone.move(move[0], move[1], player)
        score = max_play(clone, provided.switch_player(player))
        if score < best_score:
            best_move = move
            best_score = score
    return best_score

def max_play(board, player):
    print board
    if board.check_win():
        return SCORES[board.check_win()]
    moves = board.get_empty_squares()
    best_move = moves[0]
    best_score = float('-inf')
    for move in moves:
        clone = board.clone()
        clone.move(move[0], move[1], player)
        score = min_play(clone, provided.switch_player(player))
        if score > best_score:
            best_move = move
            best_score = score
    return best_score

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
list_board = [[3,3,1],[1,2,2],[1,1,1]]
board1 = provided.TTTBoard(3, False,list_board)

print "move"
print mm_move(board1, provided.PLAYERX)

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
