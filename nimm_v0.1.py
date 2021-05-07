"""
Ancient Game of Nimm
--------------------
Game starts with pile of 20 stones
Two players alternate turns 
On a given turn, player may take 1 pr 2 stones
Last player to take a stone loses
"""

def main():
    # Create variables for the pile of stones and the two players
    stones = 20
    player = 1

    # play game until the pile runs out
    while stones > 1:

        # tell how many stones are left
        print_stone_count(stones)
        
        # ask player to take a turn
        play = get_their_play(player)
        
        # calculate remaining stones
        stones = stones - int(play)

        # switch players
        player = get_player(player)

        # white space between rounds
        print('')
    
    # declare winnner
    if stones == 1:
        if player == 1:
            player = 2
        print("Player", player, "wins!")
    else:
        print("Player", player, "wins!")


def print_stone_count(stones):
    print("There are", stones, "stones left")


def get_their_play(player):
    play = input("Player " + str(player) + " would you like to remove 1 or 2 stones? ")
    while play < "1" or play > "2":
        play = input("Please enter 1 or 2: ")
    return play


def get_player(current_player):
    if current_player == 1:
        current_player = 2
        return current_player
    else:
        current_player = 1
        return current_player


if __name__ == '__main__':
    main()
