count=1
print('カレーを召し上がれ')
while True:
    print(f'{count}皿のカレーを食べました')
    ans=input('お代わりはいかがですか?(y/n)>>')
    if ans == 'n':
        break
    count+=1
print('ごちそうさまでした')
