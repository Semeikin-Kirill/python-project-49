import random

GAME_DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = ('+', '-', '*')

operation_result = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}


def game_data_generation():
    first_number = random.randint(1, 1000)
    second_number = random.randint(1, 1000)
    operation = random.choice(OPERATIONS)
    answer = operation_result[operation](first_number, second_number)
    return (f'{first_number} {operation} {second_number}', str(answer))
