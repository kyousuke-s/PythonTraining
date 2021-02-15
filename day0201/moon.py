dist=384400*1000*1000 #月までの距離(mm)
thickness=1 #紙の厚さ(mm)
count=0 #折り曲げた回数

while thickness < dist: #距離が厚みより大きければTrue
    thickness *= 2 #厚みを2倍に
    count += 1 #回数を1増やす
    print(count,'回折り曲げた','厚み:',thickness) #一回折り曲げるごとの途中経過
print(count,'回で月に到達しました。') #最終結果
