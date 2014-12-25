def prompt_for_input():
    result = input("?>")
    return result


def begin_interaction_with_user():
    print('''Welcome to the "Do you even math?" game!
             Here are your options:
            - start
            - highscores''')


def start_game_prompt_for_name():
    print("Enter your playername")
    playername = input(">")
    return playername


def print_scores(scores):
    print("This is the current top10:")
    for i in range(min(10, len(scores))):
        print("{}. {} - {}".format(i+1, scores[i].username, scores[i].points))


def output(output):
    print(output)
