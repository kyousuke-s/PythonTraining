#BMI測定器の作成

height=input('身長(cm)を入力してください>')
weight=input('体重(kg)を入力してください>')

#小数点のある実数への変換はfloat()
height=float(height)/100
weight=float(weight)

bmi=weight/height**2
print('BMI:',bmi)

if bmi>=25:
    result='肥満'
elif bmi>=18.5:
    result='標準体重'
else:
    result='痩せ型'

print(result)
