class Hero:
    name = '松田'
    hp=100
    def sleep(self,hours):
        print('{}は{}時間寝た!'.format(self.name,hours))
        self.hp += hours

print('スッキリファンタジーⅦ ～金色の理想郷～')
h=Hero()
h.sleep(3)
print('{}の現在のHPは{}です'.format(h.name,h.hp))
