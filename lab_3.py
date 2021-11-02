s = 'azzaa'
number = 0
nugno = set()
nenugno = set()
bukva = s[0]
for i in s:
    print(i, bukva, number, nugno, nenugno)
    if i == bukva:
        number += 1
    else:
        if number % 2 == 0:
            nugno.add(bukva)
        else:
            nenugno.add(bukva)
        bukva = i
        number = 1
print(nugno - nenugno)
