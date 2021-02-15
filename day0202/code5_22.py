def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))
    print()

eat('トースト','おにぎり')
eat('バナナ','そば','焼肉')

eat('トースト')
#end=''やsep=''と同じ仕組み
eat('トースト',dinner='焼きそば')#引数を入力するときにどの引数かを指定できる
