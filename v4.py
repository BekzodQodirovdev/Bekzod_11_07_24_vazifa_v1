def sort(lst) :
    dct = {}
    for i in lst :
        count = 0
        for j in i :
            count = count + int(j)
        dct.setdefault(count,int(i))
    x = dict(sorted(dct.items()))
    answer = list(x.values())
    print(answer)

lst = []
n = int(input("Enter numbers length: "))
for i in range(n):
    num = input(f"{i+1} - num: ")
    if int(num) > 0:
        lst.append(num)
    else:
        break

sort(lst)