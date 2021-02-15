def eat(breakfast,lunch,dinner='カレー',*desserts):
    print('朝は{}を食べました'.format(breakfastU))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))
    for d in desserts:
        print('おやつに{}を食べました'.format(d))

#eat(breakfast='納豆ごはん',dinner='カレーうどん')
#eat(dinner='カレーうどん',breakfast='納豆ごはん')
#eat('納豆ごはん',dinner='カレーうどん')
#eat(dinner='カレーうどん','納豆ごはん')

eat('トースト','パスタ','カレー','アイス','チョコ','カレー')
