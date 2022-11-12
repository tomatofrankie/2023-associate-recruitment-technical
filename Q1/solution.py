N = int(input())
sizes_available = input()
M = int(input())
requested = input()

tshirt_list = sizes_available.split()
requested_list = requested.split()

size_list = ['S','M','L']
Xs = 'S'
Xl = 'L'
for i in range(1000,0,-1):
    Xs = 'X' + Xs
    Xl = 'X' + Xl
    size_list.insert(0,Xs)
    size_list.append(Xl)


for i in range(M):
    for j in range(N):
        if size_list.index(requested_list[i]) < size_list.index(tshirt_list[j]):
            result = True
            break
        else:
            result = False
            break

print(result)

