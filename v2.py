def most_votes(dct):
    one = 0
    zero = 0

    for v in dct.values():
        if v == 1:
            one += 1
        elif v == 0:
            zero += 1

    return [1, 0] if one == zero else [1] if one > zero else [0]
    
dct = {}
n = int(input("Enter List length: "))

for i in range(n):
    name = input("name: ")
    num = int(input("1 or 0: "))
    dct.setdefault(name,num)

for i in most_votes(dct):
    print('\n', i)
    for key, val in dct.items():
        if val == i:
            print(key, end = ' ')