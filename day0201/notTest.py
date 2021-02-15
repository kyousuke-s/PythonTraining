food='カレーライス'
if 'カレー' in food:
    print('カレーが含まれています')

food2='すし'

if not 'カレー' in food2:
    print('カレーが含まれていません')

if 'カレー' not in food2:
    print('カレーが含まれていません')

#pythonでできる書き方
score=80
if 60 < score < 80:
    print('良')


#教科書 p154 練習3-3

#1
isError=False
n=50
if isError and n < 100:
    pass

#2
num=10
if num % 2 == 0:
    print('偶数')

#3
aisatsu='さようなら'
if aisatsu == 'こんにちは':
    print('ようこそ')
elif aisatsu == '景気は?':
    print('ぼちぼちです')
elif aisatsu == 'さようなら':
    print('お元気で!')
else:
    print('どうしました?')

#教科書 p154 練習3-4

month=int(input('今は何月ですか?(数字を入力)>>'))

if month in [1,3,5,7,8,10,12]:
    print('31日までありますね')
else:
    if month != 2:
        print('30日までですね')
    else:
        print('1年で一番寒い月ですね')
    print('年が明けてから')
print('{}ヶ月が過ぎました'.format(month))

#三項条件演算子の書き方

number=10
#値1 if 条件式 else 値2
div = '偶数' if number % 2 == 0 else '奇数'
'''
#下記の三項演算子と同様
String div=number % 2 ==0 ? "偶数":"奇数";
'''
#複数の条件式を続けて記述
result='優' if score >= 80 else '良' if score >= 60 else '可' if score >= 40 else '不可'
