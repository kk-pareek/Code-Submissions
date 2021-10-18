print('Input number of rows for patterns, valid in most cases')
row = int(input())

# Increasing Star - 
print('Right Triangle Star Pattern')

for i in range(1, row+1):
    print('*'*(i))

# Decreasing Star -
print("Downward Triangle Star Pattern")

for i in range(row, 0, -1): 
    print('*'*(i))

# Increasing Stars from right side -
print('Mirrored Right Triangle Star')

for i in range(row, 0, -1):
    print((' '*(i-1))+('*'*((row-i)+1)))

# Decreasing Stars from right side -
print(' Left Triangle Star Pattern')

for i in range(row, 0, -1):
    print((' '*(row-i))+('*'*(i)))

# Pyramid -
print('Pyramid')

for i in range(row):
    print((' '*((row-1)- i))+'*'+('*'*(i+i)))

# Diamond -
print('Diamond')

for i in range(row):
    print((' '*((row-1)- i))+'*'+('*'*(i+i)))

for i in range(row-1, -1, -1):
    print((' '*((row-1)- i))+'*'+('*'*(i+i)))
