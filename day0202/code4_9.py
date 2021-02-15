ages=[26,50,8,'ひみつ',20,78,25,'無回答',22,10,27,33]
num=5 #目標の抽出数
samples=list() #サンプルを格納するリスト
for age in ages:
    # isinstance(a,c) は、aがbの型であるかを判定する
    if not isinstance(age,int): #notなので[ageがint型でなかったら]になる
        continue
    if 20 <= age < 30:
        samples.append(age)
        if len(samples) == num:
            break
print(samples)
