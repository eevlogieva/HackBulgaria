from load_database import session
from command_parser import CommandParser
from fill_questions_table import fill_with_questions
from random import randint
from make_database import MathProblem, Score


def main():
    fill_with_questions(session)
    command_parser = CommandParser()
    command_parser.add_command("begin", begin_interaction_with_user)
    command_parser.add_command("start", start_game)
    command_parser.add_command("highscores", show_highscores)
    command_parser.add_command("finish", finish)
    command_parser.run_command("begin")
    command = input("?>")
    command_parser.run_command(command)
    while command != "finish":
        command = input("?>")
        command_parser.run_command(command)


def begin_interaction_with_user():
    print('''Welcome to the "Do you even math?" game!
             Here are your options:
            - start
            - highscores''')


def start_game():
    print("Enter your playername")
    playername = input(">")
    number_of_questions = 1
    asked_questions = []
    score = 0
    play_round(playername, score, number_of_questions, asked_questions)


def play_round(playername, score, number_of_questions, asked_questions):
    print("Question #{}".format(number_of_questions))
    current_question = randint(1, 50)
    while current_question in asked_questions:
        current_question = randint(1, 50)
    asked_questions.append(current_question)
    problem = session.query(MathProblem.question,
                            MathProblem.answer).filter(MathProblem.id == current_question).one()
    print(problem[0])
    given_answer = input("?>")
    if given_answer == problem[1] and len(asked_questions) == 150:
        print('''Congratulations!
                 You answered all the questions correctly!
                 Your score is {}'''.format(score ** 2))
        session.add(Score(username=playername, points=score ** 2))
        session.commit()
    if float(given_answer) == float(problem[1]):
        print("Correct!")
        score += 1
        number_of_questions += 1
        play_round(playername, score, number_of_questions, asked_questions)
    else:
        print("Incorrect! Ending game. You score is: {}".format(score ** 2))
        session.add(Score(username=playername, points=score ** 2))
        session.commit()


def finish():
    pass


def show_highscores():
    scores = session.query(Score).order_by(Score.points.desc()).all()
    print("This is the current top10:")
    for i in range(min(10, len(scores))):
        print("{}. {} - {}".format(i+1, scores[i].username, scores[i].points))


if __name__ == '__main__':
    main()
