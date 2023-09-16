import random

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def number_generation():
    return random.randint(1, 1000)


def game_data_generation():
    question_number = number_generation()
    correct_answer = 'yes' if is_even(question_number) else 'no'
    return (question_number, correct_answer)
