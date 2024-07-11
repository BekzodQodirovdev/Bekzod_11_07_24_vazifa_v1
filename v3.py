with open("employe_information.txt") as file:
    data = file.read().split('\n')

for i, line in enumerate(data):
    data[i] = line.split()
    data[i][-2] = int(data[i][-2]) 

ls = {}

for line in data:
    if len(line) < 5:
        continue  
    _, _, _, bonus, group = line
    if group not in ls:
        ls[group] = 0
    if bonus > 0:
        ls[group] += 1
    elif bonus < 0:
        ls[group] -= 1

best_score = max(ls.values())

for gr, val in ls.items():
    if val == best_score:
        print(gr)
