import pprint
W=H=10
x=[[i*H-j*W for j in range(W)] for i in range(H)]
pprint.pprint(x)
