list1=[] #空のリスト
list2=list() #空のリスト

#リストの追加
list1.append(3)
print(list1)
list1.append(5)
print(list1[0])

list2.append(10)
list2.append(20)
print(list2)

list3=list1+list2
print(list3)

#リストの中身をかけた回数繰り返す
list4=list3*3
print(list4)

#要素数
print(len(list4)) #12
print(sum(list4)) #合計114

#インデックスを指定して削除
del list4[0]
print(list4)

#見つけた最初の1つを削除
list4.remove(5)
print(list4)

#指定した範囲(最後の値は未満になる)
list5=list4[3:8]
print(list5)

print(list5[-1]) #最後の要素
