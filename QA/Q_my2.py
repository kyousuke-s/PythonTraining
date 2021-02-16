import tkinter as tk

def bt_click():
    global cs,s
    cs=[]
    for i in str(s):
        ord_c = ord(i)
        cs.append(ord_c)
    result['text']=f'{sum(cs)}'


root=tk.Tk()
#ウィンドウサイズの固定
root.resizable(False,False)
cvs=tk.Canvas(root,width=600,height=600)
cvs.pack()

s = tk.Entry(width=50)
s.place(x=100,y=300)
cs=[]

btn=tk.Button(text='決定',font=('Arial',20),command=bt_click)
btn.place(x=100,y=400)

result=tk.Label(text='',font=('Arial',20),bg='skyblue')
result.place(x=100,y=500)

root.mainloop()
