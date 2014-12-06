from make_database import MathProblem
from random import randint


def fill_with_questions(session):
    if len(session.query(MathProblem).all()) == 150:
        pass
    else:
        for i in range(50):
            add_problem(session)


def generate_problem():
    operations = {1: ("+", lambda x, y: x + y),
                  2: ("-", lambda x, y: x - y),
                  3: ("*", lambda x, y: x * y),
                  4: ("/", lambda x, y: x / y),
                  5: ("^", lambda x, y: x ** y)}
    op_index = randint(1, 5)
    if op_index == 5:
        operand_one = randint(0, 5)
        operand_two = randint(0, 5)
    elif op_index == 4:
        operand_one = randint(0, 10)
        operand_two = randint(1, 10)
    else:
        operand_one = randint(0, 10)
        operand_two = randint(0, 10)
    answer = operations[op_index][1](operand_one, operand_two)
    return ("What is the answer to {} {} {}?".format(operand_one,
                                                     operations[op_index][0],
                                                     operand_two), answer)


def add_problem(session):
    problem = generate_problem()
    session.add(MathProblem(question=problem[0],
                            answer=problem[1]))
    session.commit()


# def operation(op_index, first, second):
#     if op_index == 1:
#         return first + second
#     elif op_index == 2:
#         return first - second
#     elif op_index == 3:
#         return first * second
#     elif op_index == 4:
#         return first / second
#     else:
#         return first ** second
