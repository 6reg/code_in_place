def main():
    print("Welcome to the CodeInPlace Game Show!")

    door = int(input("Door: "))

    while door < 1 or door > 3 :
        print("Invalid door #!")

        door = int(input("Door: "))

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

    print("The prize is", prize, "!")

main()
