import random


def get_task():
    question = random.randint(0, 100)
    dividers = []
    for i in range(1, question):
        if question % i == 0:
            dividers.append(i)

    correct_answer = 'yes' if len(dividers) == 1 else 'no'

    return (question, correct_answer)


def issue():
    return ('"yes" if given number is prime. Otherwise answer "no".')
