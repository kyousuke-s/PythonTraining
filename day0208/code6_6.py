scores1=[80,40,50]
scores2=[80,40,50]

print('scores1のidentity:{}'.format(id(scores1)))
print('scores2のidentity:{}'.format(id(scores2)))

#内容を比較(等価)
if scores1 == scores2:
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

#idを比較(等値)
if id(scores1) == id(scores2):
    print('同じ存在')
else:
    print('違う存在')

#住所を比較(等値)
if scores1 is scores2:
    print('同じ存在')
else:
    print('違うじ存在')


