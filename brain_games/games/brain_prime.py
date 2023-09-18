import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    start_number = 2
    while number % start_number != 0:
        start_number += 1
    return start_number == number


def game_data_generation():
    question = random.randint(1, 1000)
    answer = 'yes' if is_prime(question) else 'no'
    return (question, str(answer))
