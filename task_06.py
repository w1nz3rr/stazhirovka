def rps_game_winner(list_players):
    #Валидация
    if len(list_players) != 2:
        raise ValueError("WrongNumberOfPlayersError")
    list_item = ['R', 'S', 'P']
    for item_player in list_players:
        if not item_player[1] in list_item:
            raise ValueError("NoSuchStrategyError")
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


#Исключения
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
except ValueError as error:
    print(error)
try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
except ValueError as error:
    print(error)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
except ValueError as error:
    print(error)

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
except ValueError as error:
    print(error)

