def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i]+'さん'
    return names

before_names = ['松田','浅木','工藤']

#リストの複製
'''
copied_names = list()
for n in before_names:
    copied_names.append(n)
'''

#スライスでリストのコピーを作る
copied_names=before_names[:]


#複製したリストを引数で渡す
after_names = add_suffix(copied_names)

#参照型なので同じ場所の配列を見ている
print('さん付け後:'+ after_names[0])
print('さん付け前:'+ before_names[0])
