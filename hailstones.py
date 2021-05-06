"""
Hailstone Sequence
-------------------------
A problem from Douglas Hofstadter's book, "Godel, Escher, Bach":
    Pick some positve integer and call it n
    If n is even, divide by two
    If n is odd, multiply by three and + 1
    Continue until n is equal to one
"""

def main():
    counter = 0
    start = get_number()
    while start > 1:
        if start % 2:
            next_num = odd_math(start)
            print(start, "is odd, so I make 3n + 1:", next_num)
            start = next_num
            counter+=1
        else:
            next_num = even_math(start)
            print(start, "is even, so I take half:", next_num)
            start = next_num
            counter+=1
    print("The process took", counter, "steps to reach 1")
        

def get_number():
    start = input("Enter a number:")
    return int(start)

def odd_math(n):
    return 3*n+1

def even_math(n):
    return int(n/2)

if __name__ == "__main__":
    main()

