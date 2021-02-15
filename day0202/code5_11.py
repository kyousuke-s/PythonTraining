def calc_average(scores):   #defはdefineの略で関数の定義に使用する
    avg = sum(scores)/len(scores)
    print(f'平均点は{avg}です')

calc_average([10,20,30])
calc_average((10,20,30))
calc_average(range(100))
calc_average({10,20,20,30,10,40})

def plus(x,y):
    answer=x+y
    return answer #戻り値

ans=plus(100,200)
print(ans)
