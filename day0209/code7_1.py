'''
text = input('何を記録しますか?>>')
file = open('diary.txt','a')
file.write(text+'\n')
file.close()
'''
import codecs #文字コードの指定ができるようになる
text = input('今日は何をした?>>')
with codecs.open('diary.txt','a','utf-8') as file:
    file.write(text+'\n')
