"""
This program takes in a dictionary and 
reverses it.
"""

def reverse(original):
    reversal = {} 
    for old_key in original:
        old_value = original[old_key]
        if old_value not in reversal:
            reversal[old_value] = [old_key]
        else:
            reversal[old_value].append(old_key)
    return reversal

def main():

    my_dict = {
            "Greg": 42,
            "Mike": 42,
            "Jim": 41,
            "Alex": 38,
            "Jacod": 38,
            "Jill": 39
            }

    print('Original:')
    for key in my_dict:
        print(key, '->', my_dict[key])

    my_dict_reversed = reverse(my_dict)

    print('Reversed:')
    for key in my_dict_reversed:
        print(key, '->', my_dict_reversed[key])

main()
