import random
balls=[i+1 for i in range(99)]
random.shuffle(balls)
#print(balls)
raund=5
win=0
for i in range(raund):
    a=balls.pop()
    b=balls.pop()
    print('{}回戦'.format(i+1))
    if a > b:
        print('A:{},B:{}...Aの勝ち'.format(a,b))
        win+=1
    else:
        print('A:{},B:{}...Bの勝ち'.format(a,b))

if win>raund-win:
    print('{}対{}でAの勝ち'.format(win,raund-win))
else:
    print('{}対{}でBの勝ち'.format(win,raund-win))

#解答
'''
import random
GAME_COUNT=5
balls=list(range(1,100))
random.shuffle(balls)
awin=bwin=0
for i in range(GAME_COUNT):
	print(f'{i+1}回戦')
	a,b=balls.pop(),balls.pop()
	if a>b:awin+=1;winner='A'
	else:bwin+=1;winner='B'
	print(f'A:{a},B:{b}...{winner}の勝ち')
print('{}対{}で{}の勝ち'.format(max(awin,bwin),min(awin,bwin),'A' if awin > bwin else 'B'))
'''
