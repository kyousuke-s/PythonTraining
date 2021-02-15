def add_suffix(name):
    name = name+'さん'
    return name

before_name = '松田'

after_name = add_suffix(before_name)

#参照型なので同じ場所の配列を見ている
print('さん付け後:'+ after_name)
print('さん付け前:'+ before_name)
