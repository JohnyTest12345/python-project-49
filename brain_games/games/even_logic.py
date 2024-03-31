import random


def get_task():
    question = random.randint(0, 20)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return (question, correct_answer)


def issue():
    return ('Answer "yes" if the number is even, otherwise answer "no".')
