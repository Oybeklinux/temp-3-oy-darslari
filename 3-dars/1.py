n = 5

satr = str(n)
for i in range(n-1, 0, -1):
    print(" ", end="")
    print(" " * (i-1)*2, satr)
    satr = f"{i} {satr} {i}"
    
print(satr)
