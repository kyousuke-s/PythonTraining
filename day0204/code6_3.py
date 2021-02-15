userinfo = input('名前と血液型をカンマで区切って1行で入力>>')
[name,blood]=userinfo.split(',')
blood=blood.upper().strip()
print('{}さんは{}型なので大吉です'.format(name,blood))

#小数点の桁
print('{:.1f}'.format(2.342))

#リストの中身を指定した文字で連結
l1=['1','2','3']
print('&'.join(l1))

#指定した文字が何回含まれているか
str='abacadaeafag'
print(str.count('a'))
#左側で指定した文字を右側の文字に置き換え
print(str.replace('a','&'))

#文字列もシーケンスの為for文で回せる
for s in 'hello': #一文字ずつ書き出し
    print(s)

#シーケンスの内容をインデックス付きで取り出す
for i,s in enumerate('hello',1):
    print('{}文字目は{}です'.format(i,s))

s1='hello'
#リストに一文字ずつ逆順に格納
s2=list(reversed(s1))
print(s2)
print(''.join(s2))

#文字列を逆順にする
s3=s1[::-1]
print(s3)

print(len(s1))
