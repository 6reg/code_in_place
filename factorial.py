# Constant - visible to all functions
MAX_NUM = 4

def main():
    # repeat for several values
    for i in range(MAX_NUM):
        print(i, factorial(i))
        
# Hmm
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result 

main()
