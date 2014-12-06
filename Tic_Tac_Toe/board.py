class Board:
    empty_box = 0
    x_box = 1
    o_box = 2
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],
                         [0, 4, 8], [2, 4, 6]]

    def __init__(self, start_position):
        self.board = []
        for index in range(0, 9):
            if index == start_position:
                self.board.append(Board.x_box)
            else:
                self.board.append(Board.empty_box)

    def is_empty_box(self, position):
        return self.board[position] == Board.empty_box

    def is_full(self):
        return not Board.empty_box in self.board

    def copy(self, other):
        self.board.deepcopy(other.board)

    def real_move(self, player, position):
        if player == 1:
            self.board[position] = Board.x_box
        if player == -1:
            self.board[position] = Board.o_box

    def fake_move(self, player, position):
        duplicate = self.board.copy()
        if player == 1:
            duplicate[position] = Board.x_box
        if player == -1:
            duplicate[position] = Board.o_box
        return duplicate

    def get_available_positions(self):
        list_of_available_positions = []
        for index in range(1, 9):
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
            if self.board.winning_position[0] == \
               self.board.winning_position[1] == \
               self.board.winning_position[2] == box:
                result.append(True)
        return True in result

    def __str__(self):
        string = "-------\n"
        for index in range(0, 9):
            string += ("|" + str(self.board[index]))
            if (index + 1) % 3 == 0:
                string += "|\n"
                string += "-------\n"
        return string
