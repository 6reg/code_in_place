def main():
    print("Welcome to the CodeInPlace Game Show!")

    door = get_door()

    prize = compute_prize(door)
   

    print("The prize is", prize, "!")
     
def compute_prize(door):
    """
    Compute prize, calculates how many treats you win.
    Based off door which was chosen
    """
    prize = 4 

    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        locked = prize % 2 != 0
        if not locked:
            prize += 6
    elif door == 3:
        
        for i in range(door):
           prize += i
    return prize

def get_door():
    """
    Get door, asks user to enter door
    Reprompts the user until they enter 1, 2 or 3
    Returns valide door choice
    """
    door = int(input("Door: "))
    # while input invalide
    while door < 1 or door > 3:
        # tell user invalid
        print("Invalid door!")
        # ask for new input
        door = int(input("Door: "))

main()
