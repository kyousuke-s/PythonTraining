import random

max_num=100
lucky_num=77
count=0

nums=list()
for i in range(max_num):
    num=random.randint(1,100)
    nums.append(num)
print(nums)
for i in range(max_num):
    count+=1
    if nums[i]==lucky_num:
        print(lucky_num,'->',count)
        break
else:
    print(lucky_num,'->なし')

#答え
'''
data=list()
data_count=100
for _ in range(data_count):
    data.append(random.randint(1,100))
print(data)
for i in range(data_count):
    if data[i]==77:
        print('77->',i)
        break
else:
    print('77->なし')
'''
"""
# コレクションを回しながら、カウンタ変数も使いたい場合
for i,num in enumerate(data):
    if num == 77:
        print('77->',i)
        break
else:
    print('77->なし')
"""
