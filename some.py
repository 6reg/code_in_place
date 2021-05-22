def main():
    count = []
    for i in range(5):
        count += count[:3]
    print(count)

main()
