class Board:
    empty_box = 0
    x_box = 1
    o_box = 2
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],
                         [0, 4, 8], [2, 4, 6]]
    print_symbols = {empty_box: ' ', x_box: 'x', o_box: 'o'}

    def __init__(self):
        self.board = []
        for index in range(0, 9):
            self.board.append(Board.empty_box)

    def is_empty_box(self, position):
        return self.board[position] == Board.empty_box

    def is_full(self):
        return not Board.empty_box in self.board

    def copy(self):
        result = Board()
        result.board = self.board.copy()
        return result

    def real_move(self, player, position):
        if player == 1:
            self.board[position] = Board.x_box
        if player == -1:
            self.board[position] = Board.o_box

    def fake_move(self, player, position):
        duplicate = self.copy()
        if player == 1:
            duplicate.board[position] = Board.x_box
        if player == -1:
            duplicate.board[position] = Board.o_box
        return duplicate

    def get_available_positions(self):
        list_of_available_positions = []
        for index in range(0, 9):
            if self.board[index] == Board.empty_box:
                list_of_available_positions.append(index)
        return list_of_available_positions

    def is_winner(self, player_num):
        result = []
        if player_num == 1:
            box = Board.x_box
        if player_num == -1:
            box = Board.o_box
        for winning_position in Board.winning_positions:
            if self.board[winning_position[0]] == \
               self.board[winning_position[1]] == \
               self.board[winning_position[2]] == box:
                result.append(True)
        return True in result

    def __str__(self):
        string = "---------------\n"
        for index in range(0, 9):
            string += (" | " + Board.print_symbols[self.board[index]])
            if (index + 1) % 3 == 0:
                string += " |\n"
                string += "---------------\n"
        return string

    def difference(self, other):
        return [index2 for index1, element1 in enumerate(self.board)
                       for index2, element2 in enumerate(other.board)
                       if index1 == index2 and element1 != element2]
