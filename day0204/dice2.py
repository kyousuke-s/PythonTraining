import random

num=int(input('サイコロを何回ふる?>>'))
dl=[random.randint(1,6) for _ in range(num)]
ds=set(dl)
print(dl)
print('出た目は{}の{}種類'.format(ds,len(ds)))

#解答
'''
import random
num=int(input('サイコロを何回ふる?>>'))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print('出た目は',set(dices),'の',len(set(dices)),'種類')
'''

