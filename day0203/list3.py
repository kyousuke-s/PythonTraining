import pprint
H=10
W=10
data=[[0]*W]*H
pprint.pprint(data)

'''
以下と同様
data=[[0,0,0,0,0,0,0,0,0,0]]+[[0,0,0,0,0,0,0,0,0,0]]+....

シャローコピーとなるため同じ場所を参照するので注意
一部を変更するとほかも変更してしまう
data[1][1]=5
data=[[0,5,0,0,0,0,0,0,0,0]]+[[0,5,0,0,0,0,0,0,0,0]]+....


'''
