# the first line of input is the number of rows of the array
n = int(input('n:')) 
a = []
for i in range(n):
    row = input('lll:').split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)
print(a)