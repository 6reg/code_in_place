"""
* 2 player game
* Start with pile of 20 stones
* Take turns choosing either 1 or 2 stones
* However is left with 1 stone loses
"""

def main():
    player = 1 # create variable for players
    stones = 20 # variable for stones

    while stones > 0: # play game until all 20 stones are used
        print("There are", str(stones), "stones left.")
        
        amount = input("Player " + str(player) +  
                 " would you like to remove 1 or 2 stones?") # get 1 or 2 
                                                             # play from player
        
        while int(amount) > 2 or int(amount) < 1:
            amount = int(input("Please enter 1 or 2: ")) # check that only 1 or                                                             2 are entered

        if player == 1: # switch players each iteration
            player = 2
        else: 
            player = 1

        stones = stones - int(amount) # update stones count

    print("Player", player, "wins!") # once stones == 0, print who won

main()
