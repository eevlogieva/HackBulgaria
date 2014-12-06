from sys import maxsize


def min_max(node, depth, player_num):
    if node.children == []:
        return node.value

    best_value = maxsize * -player_num
    for child in node.children:
        value = min_max(child, depth - 1, -player_num)[0]
        if (abs(maxsize * player_num - value) < (abs(maxsize * player_num - best_value))):
            best_value = value
            #(filter )
            #best_move = child.
    #return (best_value, best_move)
    return best_value
