import random

print('数当てゲームを始めます3桁の数を当ててください!')

#答え作成
answer = list()
for _ in range(3):
    answer.append(random.randint(0,9))
print(answer)

while True:

    #解答入力
    prediction = list()
    for i in range(3):
        prediction.append(int(input(f'{i+1}桁目の予想を入力(0~9)>>')))
    print(prediction)

    #答え合わせ
    hit = 0
    blow = 0

    for i in range(3):
        if prediction[i] == answer[i]:
            hit += 1
        else:
            for n in range(3):
                if prediction[i] == answer[n] and i != n:
                    blow += 1

#リザルト
    print(f'{hit}ヒット!{blow}ボール!')
    if hit == 3:
        print('正解です!')
        break
    else:
        if int(input('続けますか?1:続ける2:終了>>')) == 2:
            print(f'正解は{answer[0]}{answer[1]}{answer[2]}でした')
            break

#解答
'''
import random
print('数あてゲームを始めます。3桁の数をあててください')
answer=[random.randint(0,9) for i in range(3)]
while True:
	hit=ball=0
	for i in range(3):
		num=int(input(f'{i+1}桁目の予想を入力(0-9)>>'))
		for j in range(3):
			if answer[j]==num:
				if i==j:
					hit+=1
				else:
					ball+=1
	print(f'{hit}ヒット!{ball}ボール')
	if hit==3:
		print('正解です!')
		break
	else:
		select=int(input('続けますか?1:続ける 2:終了>>'))
		if select == 2:
			print(f'正解は{answer[0]}{answer[1]}{answer[2]}でした!')
			break
'''
