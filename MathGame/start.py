from load_database import session
from command_parser import CommandParser
from fill_questions_table import fill_with_questions
from random import randint
from make_database import MathProblem, Score
from interact_with_user import * # I know that usually this is not a very good practice, but I need all the functions from this module


def main():
    fill_with_questions(session)
    command_parser = CommandParser()
    command_parser.add_command("begin", begin_interaction_with_user)
    command_parser.add_command("start", start_game)
    command_parser.add_command("highscores", show_highscores)
    command_parser.add_command("finish", finish)
    command_parser.run_command("begin")
    command = prompt_for_input()
    command_parser.run_command(command)
    while command != "finish":
        command = prompt_for_input()
        command_parser.run_command(command)


def start_game():
    playername = start_game_prompt_for_name()
    number_of_questions = 1
    asked_questions = []
    score = 0
    play_round(playername, score, number_of_questions, asked_questions)


def play_round(playername, score, number_of_questions, asked_questions):
    output("Question #{}".format(number_of_questions))
    current_question = randint(1, 50)
    while current_question in asked_questions:
        current_question = randint(1, 50)
    asked_questions.append(current_question)
    problem = session.query(MathProblem.question,
                            MathProblem.answer).filter(MathProblem.id == current_question).one()
    output(problem[0])
    given_answer = prompt_for_input()
    if given_answer == problem[1] and len(asked_questions) == 150:
        output('''Congratulations!
                 You answered all the questions correctly!
                 Your score is {}'''.format(score ** 2))
        session.add(Score(username=playername, points=score ** 2))
        session.commit()
    if float(given_answer) == float(problem[1]):
        output("Correct!")
        score += 1
        number_of_questions += 1
        play_round(playername, score, number_of_questions, asked_questions)
    else:
        output("Incorrect! Ending game. You score is: {}".format(score ** 2))
        session.add(Score(username=playername, points=score ** 2))
        session.commit()


def finish():
    pass


def show_highscores():
    scores = session.query(Score).order_by(Score.points.desc()).all()
    print_scores(scores)


if __name__ == '__main__':
    main()
