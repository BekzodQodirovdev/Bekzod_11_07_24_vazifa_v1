naqsh = input("Naqsh rangini kiriting: ").split()

time = 2

for i in range(1, len(naqsh)):
    time += 2
    if naqsh[i] != naqsh[i-1]:
        time += 1

print(time)    