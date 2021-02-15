def plus_and_minus(a,b):
    return a+b,a-b #タプルで返している
    #return [a+b,a-b] #戻り値を配列にしてもいける
#アンパック代入で戻ってきたタプルをnextとprevそれぞれに代入
next,prev=plus_and_minus(1978,1) 
print(next,prev)
