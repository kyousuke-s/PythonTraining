import tkinter as tk
root=tk.Tk()
root.title('My Window')
#canvas=tk.Canvas(root,width=400,height=600,bg='skyblue')
canvas=tk.Canvas(root,width=400,height=600)
canvas.pack()
img=tk.PhotoImage(file='iroha.png')
i#x,y座標は画像の中点
canvas.create_image(200,300,image=img)
root.mainloop()
