import prompt
from brain_games.cli import welcome_user

ROUND_COUNT = 3


def create_game(get_game_data, description):
    player_name = welcome_user()
    print(description)
    for _ in range(ROUND_COUNT):
        current_question, expect_answer = get_game_data()
        print(f'Question: {current_question}')
        player_answer = prompt.string('Your answer: ')
        if player_answer == expect_answer:
            print('Correct!')
        else:
            print(f"'{player_answer}' is wrong answer ;(.",
                  f"Correct answer was '{expect_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')
