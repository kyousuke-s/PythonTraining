import tkinter as tk
def btn_click():
    #テキストをinsertで入力,引数は(場所,文言)
    #tk.ENDで文末を意味する
    text.insert(tk.END,'モンスターが現れた!')

root=tk.Tk()
root.title('My Window')
root.geometry('400x200')

btn=tk.Button(text='メッセージ',command=btn_click)
btn.pack()

text=tk.Text()
text.pack(padx=10,pady=10)

root.mainloop()
