import time

cache={}

def fibo(n):

    global cache
    if n in cache:
        return cache[n]

    if n==0:
        result = 0
    elif n==1:
        result = 1
    else:
        result = fibo(n-1)+fibo(n-2)
    cache[n] = result
    return result

'''
for i in range(11):
    print(fibo(i))

'''

for i in range(20,101,5):
    #処理時間の計測(スタート時の時間)
    start=time.time()
    result=fibo(i)
    #処理時間の計測(終了時の時間)
    end=time.time()
    #差分で時間を出す
    duration=end-start
    print(i,result,duration)
