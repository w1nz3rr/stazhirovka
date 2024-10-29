class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def valid_count_players(list_plaers):
    if len(list_plaers) != 2:
        raise WrongNumberOfPlayersError("Число игроков должно быть ровно двум")

def valid_for_items(list_players):
    list_item = [ 'R', 'S', 'P' ]
    for item_player in list_players:
        if not item_player[ 1 ] in list_item:
            raise NoSuchStrategyError("Нет такого варианта хода, у вас на выбор R, S, P")

def rps_game_winner(list_players):
    #Валидация
    try:
        valid_count_players(list_players)
    except WrongNumberOfPlayersError as error:
        return error

    try:
        valid_for_items(list_players)
    except NoSuchStrategyError as error:
        return error
    # Код функции
    player1, player2 = list_players
    name1, item1 = player1
    name2, item2 = player2
    res = ' '
    if item1 == item2:
        return res.join(player1)

    if (item1 == 'R' and item2 == 'S') or (item1 == 'S' and item2 == 'P') or (item1 == 'P' and item2 == 'R'):
        return res.join(player1)
    else:
        return res.join(player2)



print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))


