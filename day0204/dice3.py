import random

num=int(input('100~1000の範囲の偶数をいくつ生成する>>'))
dl=[random.randrange(100,1000,2) for _ in range(num)]
dls=sorted(dl,reverse=True)
print('{}個生成しました!降順に表示します{}'.format(num,dls))

#解答
'''
import random
num=int(input('100~1000の範囲の偶数をいくつ生成する>>'))
data=[random.randrange(100,1000,2) for _ in range(num)]
data.sort(reverse=True)
print(num,'個生成しました!降順に表示します',data)
'''
