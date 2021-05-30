def main():
    year_of_college = {
            'Greg': 4,
            'Mike': 3,
            'Rahm': 4,
            'Bill': 2
            }

    print("Number of years spent in college")
    for person in year_of_college:
        print(person, '->', year_of_college[person])

    reverse = rev_dict(year_of_college)
    
    for num in reverse:
        print(num, '->', reverse[num])


def rev_dict(forward):
    rev = {}
    for key in forward:
        val = forward[key]
        if val not in rev:
            rev[val] = [key]
        else:
            rev[val].append(key)
    return rev

main()
