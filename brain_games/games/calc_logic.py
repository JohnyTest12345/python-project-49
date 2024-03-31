import random


char = ['+', '-', '*']


def get_task():
    num = random.randint(0, 20)
    num2 = random.randint(0, 20)
    random_char = char[random.randint(0, 2)]
    question = f'{num} {random_char} {num2}'
    correct_answer = 0

    if random_char == '+':
        correct_answer = num + num2
    elif random_char == '-':
        correct_answer = num - num2
    elif random_char == '*':
        correct_answer = num * num2
    return (question, str(correct_answer))


def issue():
    return ('What is the result of the expression?')
