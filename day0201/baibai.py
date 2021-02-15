n=1 #最初の個数
minute=0 #経過時間
days=1 #検証日数
day_minute=days*60*24 #一日の分数に換算
while minute < day_minute: #一日の分数が経過時間よりも大きければTrue
    n*=2 #個数を倍にする
    minute+=5 #5分進める
    print(minute,'分後',n) #5分毎の途中経過
print(n) #最終結果
