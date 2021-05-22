def main():
    list_a = [1, 'Fred', 0.5]
    for i in range(len(list_a)):
        print(list_a[i], '=>', i)
    list_b = ['something', [1,2,3], 'one_more_thing']
    for i in range(len(list_b)):
        print(list_b[i], 'is', i)
        print(list_b[i][2])

main()
