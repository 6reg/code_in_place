def reverse(original):
    rev_dict = {}
    for old_key in original:
        print('old_key: ', old_key)
        old_value = original[old_key]
        print('old_value: ', old_value)
        if old_value not in rev_dict:
            rev_dict[old_value] = [old_key]
            print('rev_dict[old_value]: ', rev_dict[old_value])
        else:
            rev_dict[old_value].append(old_key)
    return rev_dict

def main():
    print("Keys become values and values become keys")
    favorite_food = {
            'Greg': 'pizza',
            'Mike': 'tacos',
            'Larry': 'tacos',
            'Abe': 'steak',
            'Jill': 'pizza'
            }
    
    print('Original:')
    for key in favorite_food:
        print(key, '->', favorite_food[key])
    reversed_dict = reverse(favorite_food)

    print('Reversed:')
    for key in reversed_dict:
        print(key, '->', reversed_dict[key])

main()
