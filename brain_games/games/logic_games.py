

import prompt


def logic(issue, get_task):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{issue}')
    sum = 0
    while sum < 3:
        correct_answer = get_task()
        print(f'Question: {correct_answer[0]}')
        answer = prompt.string('Your answer: ')

        if correct_answer[1] == answer:
            print('Correct!')
            sum += 1
        else:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer[1]}.')
            print(f"Let's try again, {name}!")
            break

    if sum == 3:
        print(f'Congratulations, {name}!')
