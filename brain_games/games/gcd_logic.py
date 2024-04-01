import random


def nod(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


def get_task():
    num = random.randint(0, 20)
    num2 = random.randint(0, 20)
    question = f'{num} {num2}'
    correct_answer = nod(num, num2)
    return (question, str(correct_answer))


def issue():
    return ('Find the greatest common divisor of given numbers.')
