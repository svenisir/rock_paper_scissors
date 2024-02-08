import random


def get_bot_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def get_winner(player_choice, bot_choice):
    normalize_dict = {
        'Камень 🗿': 'rock',
        'Бумага 📜': 'paper',
        'Ножницы ✂': 'scissors',
    }

    game_rule = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }

    if normalize_dict[player_choice] == bot_choice:
        return 'nobody_won'
    elif game_rule[bot_choice] == normalize_dict[player_choice]:
        return 'user_won'
    else:
        return 'bot_won'
