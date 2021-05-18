"""
This program checks if a sentence is a palindrome
"""

KAYAK = "a man, a plan, a canal - panama"

# Takes in string, looks only at alphanumeric chars to 
# determine if it's a valid palindrome, returns true or false
def is_palindrome(str):
    normalized = ''
    rev = ''
    for ch in str:
         if ch.isalpha():
            normalized += ch
            
    for ch in normalized:
         rev = ch + rev
    
    return normalized == rev
         

def main():
    if is_palindrome(KAYAK):
        print('this is a palindrome: ', KAYAK)
    else:
        print('not a palindrome: ', KAYAK)
    
main()
