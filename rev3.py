my_dict = {
        "car": "green",
        "bike": "green",
        'boat': 'red',
        'plane': 'white'
        }

rev_dict = {}
for key in my_dict:
    new_key = my_dict[key]
    if new_key not in rev_dict:
        rev_dict[new_key] = [key]
    else:
        rev_dict[new_key].append(key)

print(rev_dict)
    
