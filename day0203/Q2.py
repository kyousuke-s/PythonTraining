import pprint
W=H=5
x=[[1 if i==j or j==W-1-i else 0 for j in range(W)] for i in range(H)]
pprint.pprint(x)
