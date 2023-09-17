import random

GAME_DESCRIPTION = 'What number is missing in the progression?'


def create_progression(first_number, step):
    result = [first_number]
    last_number = first_number
    for _ in range(9):
        last_number += step
        result.append(last_number)
    return result


def game_data_generation():
    first_number = random.randint(1, 1000)
    step_progression = random.randint(1, 10)
    progression = create_progression(first_number, step_progression)
    index = random.randint(0, 9)
    answer = progression[index]
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return (question, str(answer))
