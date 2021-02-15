class GameCharacter:
    def __init__(self,job,life):#コンストラクタ,書き方は__init__()
        self.job=job
        self.life=life
    
    #メソッド：クラス内に定義されている関数
    def info(self):
        print(self.job)
        print(self.life)

warrior=GameCharacter('戦士',100)
#print(warrior.job)
#print(warrior.life)
warrior.info()#呼び出し時に引数にselfは不要
