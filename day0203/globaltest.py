name='松田'

def change_name():
    #グローバルネームを変更したい場合
    global name #global name='浅木' のように続けてはかけない
    name='浅木'
    print(name)

def hello():
    print('こんにちは'+name+'さん')

change_name()
hello()

#関数の中に関数を記述することもできる
'''
name='松田'

def hello():
    def change_name():
        name='浅木'
        print(name)
    change_name()
    print('こんにちは'+name+'さん')

hello()
'''
