from sys import maxsize


class Node(object):
    def __init__(self, depth, player_num, value, board):
        self.depth = depth
        self.player_num = player_num
        self.value = value
        self.board = board
        self.children = []
        self.create_children()

    def create_children(self):
        if self.depth >= 0:
            for position in self.board.get_available_positions():
                next_board = self.board.fake_move(self.player_num, position)
                self.children.append(Node(self.depth - 1,
                                          -self.player_num,
                                          self.real_value(),
                                          next_board))

    def real_value(self):
        if self.board.is_winner(self.player_num):
            return maxsize * self.player_num
        elif self.board.is_winner(-self.player_num):
            return maxsize * -self.player_num
        else:
            return 0
