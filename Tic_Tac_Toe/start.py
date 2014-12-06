from board import Board


def main():
    print("Hello! Please choose a position (from 1 to 9)")
    first_position = input(">")
    current_board = Board(int(first_position) - 1)
    print(str(current_board))


if __name__ == '__main__':
    main()
