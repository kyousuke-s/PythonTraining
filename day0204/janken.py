import random

hands=['グー','チョキ','パー']
while True:
    you=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
    pc=random.randint(0,2)
    print('あなたは{},PCは{}'.format(hands[you],hands[pc]))
    if (you-pc+3)%3 == 0:
        print('あいこ')
    elif (you-pc+3)%3 == 2:
        print('あなたの勝ち')
        break
    else:
        print('あなたの負け')
        break

#解答
'''
import random
while True:
	user=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
	pc=random.randint(0,2)
	hands=['グー','チョキ','パー']
	print(f'あなたは{hands[user]},PCは{hands[pc]}')
	if user==pc:
		print('あいこ')
		continue
	elif (user+3-pc)%3==1 :
		print('あなたの負け')
	else:
		print('あなたの勝ち')
	break
'''
