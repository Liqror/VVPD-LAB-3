def main():
    str = input()
    amount = 0
    broken_letters = set()
    pseudo_broken_letters = set()
    letter = str[0]
    for i in str:
        print(i, letter, amount, broken_letters, pseudo_broken_letters)
        if i == letter:
            amount += 1
        else:
            if amount % 2 == 0:
                broken_letters.add(letter)
            else:
                pseudo_broken_letters.add(letter)
            letter = i
            amount = 1
    print(broken_letters - pseudo_broken_letters)


if __name__ == '__main__':
    main()
