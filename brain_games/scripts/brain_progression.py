from brain_games.games.brain_progression import GAME_DESCRIPTION
from brain_games.games.brain_progression import game_data_generation
from brain_games.create_game import create_game


def main():
    create_game(game_data_generation, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
