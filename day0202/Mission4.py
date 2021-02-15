height=int(input('何段の階段を作る?>'))
for i in range(height):
    for j in range(height):
        div=' ' if j < height-(i+1) else '*'
        print(div,end='')
    print()
