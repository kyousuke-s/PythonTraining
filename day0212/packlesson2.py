import tkinter

#画面作成
root=tkinter.Tk()
root.geometry('300x200')

#ボタン作成
#btn=tkinter.Button(root,text='終了')

#配置
#btn.pack()
#横幅いっぱいに表示
#btn.pack(fill='x')
#横幅いっぱいに余白を付けて表示
#btn.pack(fill='x',padx=30,pady=10,ipady=10)

#ボタンを横に並べて表示
btn=tkinter.Button(root,text='開始',width=14)
btn.pack(fill='x',padx=20,side='left')
btn=tkinter.Button(root,text='終了',width=14)
btn.pack(fill='x',padx=20,side='left')

root.mainloop()
