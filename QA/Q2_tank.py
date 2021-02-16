import random

def battle_day():
    global count,rest
    dest=random.randint(1,15)
    count+=dest
    state=random.randint(1,100)
    print('出撃!!')
    print(f'戦果報告:{dest}輌の戦車を撃破しました!')
    if state == 1:
        print('あなたは戦死してしまいました...')
        rest += 10
    elif state <= 11:
        print('あなたは撃墜され、怪我をしてしまいました。６日の入院が必要です')
        rest += 7
    else:
        print('明日も頑張りましょう!')

def rest_day(rest):
    print(f'あと{rest}日の入院が必要です')

def result(count,medal):
    print(f'最終戦果報告!!あなたは{count}輌の戦車を破壊した功績により{medal[min(count//100,5)]}を授与されました!!')

count=0
rest=0
MAX_DAYS=100
medal=['鉄十字勲章','騎士鉄十字勲章','柏葉付騎士鉄十字勲章','柏葉・剣付騎士鉄十字勲章','柏葉・ 剣・ダイヤモンド付騎士鉄十字勲章','黄金柏葉・剣・ダイヤモンド付騎士鉄十字勲章']

for day in range(1,MAX_DAYS+1):
    print(f'{day}日目の行動')
    #日程開始
    if rest > 0:
        rest_day(rest)
    else:
        battle_day()
    #日程終了
    if rest == 10 or day == 100:
        print('戦争は終結しました!!')
        result(count,medal)
        break
    elif rest > 0:
        print('今は休んで下さいね')
        rest -= 1
    input()





'''
import random
damage=0
MAX_DAYS=100
total_kill=0
titles=['鉄十字勲章','騎士鉄十字勲章','柏葉付騎士鉄十字勲章','柏葉・剣付騎士鉄十字勲章','柏葉・ 剣・ダイヤモンド付騎士鉄十字勲章','黄金柏葉・剣・ダイヤモンド付騎士鉄十字勲章']

for day in range(1,MAX_DAYS+1):
	if damage > 0: damage-=1
	print(f'{day}日目の行動')
	if damage > 0:
		print(f'後{damage}日の入院が必要です')
	else:
		print('出撃!!')
		kill=random.randint(1,15)
		print(f'戦功報告:{kill}輌の戦車を撃破しました!')
		total_kill+=kill
		i=random.randrange(100)
		if i==0:
			print('あなたは戦死してしまいました...')
			break;
		if 1<= i <= 10:
			damage=7
			print(f'あなたは撃墜され、怪我をしてしまいました。{damage-1}日間の入院が必要です')
	print('今は休んでくださいね' if damage > 0 else '明日も頑張りましょう!')
	#input()
else:
	print('戦争は終結しました!!')
print(f'最終戦果報告!!あなたは{total_kill}輌の戦車を破壊した功績により{titles[min(total_kill//100,5)]}を授与されました!')
'''
