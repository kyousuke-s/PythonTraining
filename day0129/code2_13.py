#ディクショナリ
scores={'network':60,'database':80,'security':50}
print(scores)
print(scores['database'])
#追加
scores['programming']=65
#変更
scores['security']=55
print(scores)
'''
Map<String.Integer> map=new HashMap<>();
map.put("network",60);
'''
#削除
del scores['security']
print(scores)
#合計の出し方
print(sum(scores.values()))
