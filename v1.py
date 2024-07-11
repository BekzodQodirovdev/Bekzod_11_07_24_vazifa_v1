def process_list(n_list):
    result = []
    temp = []
    
    for i in range(len(n_list) - 1):
        if (n_list[i] >= 0 and n_list[i + 1] >= 0) or (n_list[i] < 0 and n_list[i + 1] < 0):
            if not temp:
                temp.append(n_list[i])
            temp.append(n_list[i + 1])
        else:
            if temp:
                result.append(" ".join(map(str, temp)))
                temp = []

    if temp:
        result.append(" ".join(map(str, temp)))
    
    return result


n = list(map(int,input("enter numbers: ").split()))

print(process_list(n))