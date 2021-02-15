#for num in range(3): #range()は0から()内の数値-1の回数繰り返す
#for num in range(1,3): #第一引数から第二引数-1の回数繰り返す
for num in range(1,10,3): #第三引数で[何回事に]という指定ができる
    print('Pythonは楽しい')
for _ in range(1,10,3): #変数名を[_]等で省略もできる
    print('Pythonは楽しい')

data=range(100,200) #range関数で連番の要素を持つリストが作られる
print(list(data)) #list型でなら表示できる
