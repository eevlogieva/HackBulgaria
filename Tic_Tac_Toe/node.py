from sys import maxsize


class Node(object):
    def __init__(self, player_num, board):
        self.player_num = player_num
        self.value = -1
        self.board = board
        self.children = []
        self.create_children()

    def create_children(self):
        #print(type(self.board))
        if not self.board.is_full():
            for position in self.board.get_available_positions():
                next_board = self.board.fake_move(self.player_num, position)
                self.children.append(Node(-self.player_num,
                                          next_board))

    def real_value(self):
        if self.board.is_winner(1):
            return maxsize
        elif self.board.is_winner(-1):
            return -maxsize
        else:
            return 0
