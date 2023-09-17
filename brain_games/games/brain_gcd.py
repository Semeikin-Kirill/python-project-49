import random
import math

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game_data_generation():
    first_number = random.randint(1, 1000)
    second_number = random.randint(1, 1000)
    answer = math.gcd(first_number, second_number)
    return (f'{first_number} {second_number}', str(answer))
