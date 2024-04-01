import random


def get_task():
    num = random.randint(0, 20)
    index = random.randint(0, 9)
    step = random.randint(1, 10)
    nums = []
    for i in range(10):
        nums.append(str(num))
        num += step
    correct_answer = nums.pop(index)
    nums.insert(index, '..')

    question = ""
    for i in nums:
        question += i
        question += " "

    return (question, str(correct_answer))


def issue():
    return ('What number is missing in the progression?')
