'''
for i in range(1,10):
    if i%2 == 0:
        continue
    for j in range(1,10):
        ans=i*j
        print(ans,end=' ')
        if ans >= 50:
            break
    print()
'''
for i in range(1,10):
    if i%2 == 0:
        continue
    for j in range(1,10):
        ans=i*j
        div = ' ',ans if ans < 10 else ans
        print(div,end=' ')
        if ans >= 50:
            break
    print()
