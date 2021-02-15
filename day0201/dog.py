
#input()の中に入力した文が出力されたのち入力出来る
dog_name=input('戌の名前を入力してください>')

#カンマで区切って連続で出力できる
#print(dog_name,'と入力されました',3+8,'hello'*3,3**3)

dog_age=input('戌の年齢を入力してください>')

#inputの値は文字列になるのでint()で数値にする
human_age=int(dog_age)*7

#print('名前:',dog_name,'年齢:',dog_age,'人間に換算した年齢',human_age)

#末尾に[sep=]でカンマ部分に入れる文字を指定できる(''だと空文字)
#末尾に[end=""]で改行を無効にできる

print(dog_name,'は今',dog_age,'才、人間の年齢に換算すると',human_age,'才です。',sep='',end='')

