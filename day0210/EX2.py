def gcd(x,y):
    if max(x,y)%min(x,y) == 0:
        return min(x,y) 
    else:
        return gcd(min(x,y),max(x,y)%min(x,y))

#print(gcd(1071,1029))
print(gcd(int(input('x>')),int(input('y>'))))
