import random

num=int(input('サイコロを何回ふる?>>'))
dl=[random.randint(1,6) for _ in range(num)]
print(dl)
print('合計は{}でした'.format(sum(dl)))

#解答
'''
import random
num=int(input('サイコロを何回ふる？>>'))
dices=[random.randint(1,6) for _ in range(num)]
print(dices)
print('合計は',sum(dices),'でした')
'''
