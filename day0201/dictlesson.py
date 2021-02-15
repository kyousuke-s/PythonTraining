dict1=dict() #空のdict

#追加
dict1['apple']='りんご'
dict1['orange']='みかん'
print(dict1)

print(len(dict1)) #要素数
dict1['banana']='ばなな'

#削除
del dict1['orange']
print(dict1)

#要素を指定
print(dict1['apple']) #りんご

#print(dict1['pine']) #error

#.get()は要素が無ければNoneを返す
print(dict1.get('pine')) #None

#指定したkeyが含まれているとき
if 'apple' in dict1:
    print('含まれている')

#指定したkeyが含まれていないとき
if 'pine' not in dict1:
    print('含まれていません')

#指定した内容が含まれているとき
if 'りんご' in dict1.values():
    print('含まれている')
