#宝探し
import random
import pprint

def makeTG(targets):
    for row in targets:
        for i in row:
            print(i,end='')
        print()

#表のサイズ
r=3
count=0

#表作成
print('****宝探し****')
targets=[[r*i+j for j in range(1,r+1)] for i in range(r)]

#答え作成
ans=targets[random.randint(0,len(targets)-1)][random.randint(0,len(targets)-1)]

#当てるまで繰り返し
while True:

    makeTG(targets)
    #入力画面
    you=int(input('好きな場所の数字を選んで入力してください>>'))
    you_ans=targets[(you-1)//r][(you-1)%r]
    if you_ans == ans:
        targets[(you-1)//r][(you-1)%r] = 'O'
        print('お宝を見つけました!')
        count+=1
        break
    elif you_ans == 'X':
        print('選択済みの場所です')
    else:
        targets[(you-1)//r][(you-1)%r] = 'X'
        if you_ans > ans:
            print('ハズレです。ここより小さな数字の場所にあります')
        else:
            print('ハズレです。ここより大きな数字の場所にあります')
    count += 1

makeTG(targets)
print(f'あなたはお宝を{count}回で発見しました!')


#解答
'''
import random

data=[i for i in range(1,10)]
def showData():
	global data
	for i in range(len(data)):
		print(data[i],end='')
		if (i+1) %3 ==0:
			print()
ans=random.randint(1,9)
showData()
count=0
while True:
	count+=1
	index=int(input('好きな場所の数字を選んで入力してください>>'))-1
	if data[index]==ans:
		print('お宝を見つけました!')
		data[index]='O'
		showData()
		break
	elif data[index]=='X':
		print('選択済みの場所です')
	else:
		print('ハズレです。ここより{}数字の場所にあります'.format('大きな' if ans>data[index] else '小さな'))
		data[index]='X'
	showData()
print(f'あなたはお宝を{count}回で発見しました!')
'''