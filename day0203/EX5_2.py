def is_leapyear(year):
    if year%400 == 0:
        return True
    if year%4 == 0 and year%100 != 0:
        return True
    return False

year=int(input('西暦>>'))

if is_leapyear(year):
    print(f'西暦{year}年は閏年です')
else:
    print(f'西暦{year}年は閏年ではありません')
