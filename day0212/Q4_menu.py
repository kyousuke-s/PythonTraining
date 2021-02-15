import random

money=random.randint(500,1000)
menu={'うどん':200,'ペペロンチーノ':280,'かつ丼':320,'味噌ラーメン':300}
menu_keys=list(menu.keys()) #menu部分はdictionaryで設定した変数名

while True:
    print('メニュー表')
    for i in range(len(menu_keys)):
        print(f'{i} {menu_keys[i]} {menu[menu_keys[i]]}')

    print()

    print(f'所持金 {money}円')
    n=int(input('購入したいメニュー番号を入力してください>>'))
    if money >= menu[menu_keys[n]]:
        money -= menu[menu_keys[n]] 
        print(f'{menu_keys.pop(n)}を購入しました')
    else:
        print('お金が足りません')
        
    print()

    if menu_keys==[]:
        print('全て売り切れました')
        break
    elif money == 0:
        print('お金がなくなりました')
        break


