'''
h=int(input('身長(cm)は？>>'))/100
w=float(input('体重(kg)は？>>'))
bmi=w/h/h
print(f'BMIは{bmi:.1f}です')
'''
h,w=int(input('身長(cm)は？>>'))/100,float(input('体重(kg)は？>>'))
print(f'BMIは{w/h**2 : .1f}です')

