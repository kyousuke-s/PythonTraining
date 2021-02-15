import tkinter

root=tkinter.Tk()
root.geometry('300x200')

la=tkinter.Label(root,text='Hello everybody.',bg='yellow',relief=tkinter.RIDGE,bd=2)
la.place(x=10,y=10)
lb=tkinter.Label(root,text='Oh My God!',bg='red',bd=2)
lb.place(x=10,y=30)
lc=tkinter.Label(root,text='See You Tomorrow.',bg='LightSkyBlue',bd=2)
lc.place(x=30,y=50)

root.mainloop()
