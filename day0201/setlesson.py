
#セットは要素の重複が出来ない
scores={70,80,55,80}

#追加(すでにある値の場合はerrorではなく無効になる)
scores.add(80)
print(scores)
print('要素数は{}'.format(len(scores)))
print('合計は{}'.format(sum(scores)))

#setコンストラクタを使用するとリスト内の要素が何種類かがわかる
list1=[2,3,4,5,2,3,4,5,6,7,8,9,3]
print(len(set(list1))) #種類の数がでる


#相互変換
scores={'network':60,'database':80,'security':60}
members=['松田','浅木','工藤']
print(tuple(members))       #タプルに変換
print(list(scores))         #リストに変換
print(set(scores.values())) #セットに変換

#ディクショナリのキーと内容を分けて記述
dict1=dict(zip(['赤','緑','青'],['r','g','b']))
print(dict1)

matsuda_scores={'network':60,'database':80,'security':50}
asaki_scores={'network':80,'database':75,'security':92}
member_scores={
        '松田':matsuda_scores,
        '浅木':asaki_scores
}
print(member_scores['松田']['network'])#60
print(len(member_scores))#2

member_hobbies={
        '松田':{'SNS','麻雀','自転車'},
        '浅木':{'麻雀','食べ歩き','数学','数学','数学'}
        }
print(member_hobbies)
print(member_hobbies['松田'])
print(member_hobbies['浅木'])

common_hobbies=member_hobbies['松田'] & member_hobbies['浅木']
print(type(common_hobbies))
print(common_hobbies)

#ネスト、入れ子
a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c)
print(c[0])
print(c[1][2])

d=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(d[2][2]) #9

A={1,2,3,4}
B={2,3,4,5}
print(A|B) #{1,2,3,4,5}
print(A&B) #{2,3,4}
print(A-B) #{1}
print(A^B) #{1,5}


