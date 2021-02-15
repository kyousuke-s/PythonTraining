#手続き型
def num(n):
    ans=0
    for i in range(1,n+1):
        ans += i
    return ans

#関数型 結果は上記と同様
def num2(n):
    return sum(range(1,n+1))

#同上
def num3(n):
    ls = [i for i in range(1,n+1)]
    return sum(ls)

#同上 (再起処理)
def num4(n):
    #再起処理の際は必ず分岐で終了条件が無ければいけない
    if n <= 1:
        return n
    else:
        #リカーシブル(再起処理)
        return n + num4(n-1)

#階乗
def num5(n):
    if n <= 1:
        return n
    else:
        return n*num5(n-1)

print(num5(n = int(input('正の整数>'))))


