#!/usr/bin/env python3

import prompt
import random


def main():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    sum = 0
    while sum < 3:
        num = random.randint(0, 20)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if num % 2 == 0 else 'no'

        if correct_answer == answer:
            print('Correct!')
            sum += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
            break
    if sum == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
