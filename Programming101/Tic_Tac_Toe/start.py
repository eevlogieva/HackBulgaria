from board import Board
from node import Node
from minimax import min_max
import os


def main():
    board = Board()
    end_game = False
    while not end_game:
        win_check(end_game, board)
        print("Please choose a position (from 1 to 9)")
        human_position = input(">")
        board.real_move(1, int(human_position) - 1)
        print(str(board))
        os.system('clear')
        win_check(end_game, board)
        current_board = board.copy()
        current_node = Node(-1, current_board)
        value, position = min_max(current_node)
        board.real_move(-1, position)
        print(str(board))


def win_check(end_game, board):
    if board.is_winner(1):
        print("Congratulations! You won!")
        end_game = True
        exit(0)
    elif board.is_winner(-1):
        print("Sorry, you lose!")
        end_game = True
        exit(0)
    elif board.is_full():
        print("No one wins!")
        exit(0)

if __name__ == '__main__':
    main()
