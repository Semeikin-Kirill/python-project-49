from brain_games.games.brain_prime import DESCRIPTION, game_data_generation
from brain_games.create_game import create_game


def main():
    create_game(game_data_generation, DESCRIPTION)


if __name__ == '__main__':
    main()
