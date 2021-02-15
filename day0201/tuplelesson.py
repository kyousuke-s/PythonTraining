#tapleは後から変更が出来ない
tuple1=tuple(3,5,7)

print(len(tuple1)) #3

print(tuple1[1]) #5

print(sum(tuple1)) #15

#listにtupleの要素を入れる
list1=list(tuple1)
print(list1)
list1.append(10)
print(list1)

#アンパック代入
a,b,c=tuple1
print(a,b,c) #3,5,7

#ニッチの入れ替えが簡単に
x=10
y=20

x,y=y,x
print(x) #x=20

