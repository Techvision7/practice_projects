game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def win(currrent_game):
    #horizontal
    for row in game:
        print(row)
        if now.count(row[0]) == len(row) and row[0] != 0:
            print("player {row[0} is the winner Horizontally!")

    #vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.apend(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("player {check[0} is the winner Vertically!")

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) diags[0]!= 0:
        print("player {diags[0} has won diagonally(/)")

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if diags.count(diags[0]) == len(diags) diags[0]!= 0:
        print("player {diags[0} has won diagonally(\)")


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0, 1, 2")
        count = 1
        if not just_display:
            game_map[row][column] = player
        for row in game:
"""for count, row in enumerate(game):print(count, row)"""
#enumerate iterates elements or lists with their index numbers you can use this insted of above for loop 
            print(count, row)
            count += 1
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2?", e)
    
    except Exception as e:
        print("something went wrong!!!", e)

