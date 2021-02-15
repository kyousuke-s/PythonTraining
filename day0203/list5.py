import pprint
x=[n for n in range(1,8)]
print(x)

#2乗のリスト
x=[n**2 for n in range(1,8)]
print(x)

#偶数のリスト
x=[n for n in range(1,8) if n%2 == 0]
print(x)
'''
x=list()
for n in range(1,8):
    if n%2==0:
        x.append(n)
'''

#入れ子のforでリスト
x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)
'''
x=list()
for i in range(1,3):
    for j in range(2,5):
        x.aapend(i*10+j)
'''

#二次元リスト
x=[[1*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

#単位行列の生成
row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(matrix)

matrix2=[]
for i in range(row):
    temp=[]
    for j in range(col):
        temp.append(1 if i==j else 0)
    matrix2.append(temp)
print(matrix2)

#練習
row=col=5
matrix=[[1 if i==j else 0 if i<j else 2 for j in range(col)] for i in range(row)]
pprint.pprint(matrix)



