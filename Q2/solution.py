N = int(input())
input_list = []
for i in range(N):
    input_list.append(input())

allValid = True
errorCodes = []

for i in input_list:
    if 'false' in i:
        allValid = False
        msg = list(i.split())
        errorCodes.append(msg[-1])

if allValid != False:
    print('Yes')
else:
    print('No')
    error = ''
    for i in errorCodes:
        error = error + i + ' '
    print(error)