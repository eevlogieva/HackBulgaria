from sys import maxsize


def min_max(node, count=0):
    if node.children == []:
        node.value = node.real_value()
        return (node.value, -1)

    if(node.board.is_winner(1) or node.board.is_winner(-1)):
        node.value = node.real_value()
        return (node.value, -1)

    if node.player_num == 1:
        best_value = -maxsize
    else:
        best_value = maxsize

    best_move = -1
    for child in node.children:
        value = min_max(child, count+1)[0]
        if node.player_num == 1:
            if value > best_value:
                best_value = value
                best_move = node.board.difference(child.board)[0]
        else:
            if value < best_value:
                best_value = value
                best_move = node.board.difference(child.board)[0]

    node.value = best_value
    return (best_value, best_move)
