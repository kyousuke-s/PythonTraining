import tkinter as tk

#画像番号用のインデックス
index=0

def btn_click():
    #グローバル宣言
    global index
    #インデックス番号の変更(インデックス番号+1割る配列の数の余りを出す)
    index=(index+1) % len(photos)
    #画像を消す
    canvas.delete('p1')
    #画像を配置
    canvas.create_image(320,213,image=photos[index],tag='p1')

root = tk.Tk()
root.geometry('700x560')
root['bg']='lightgrey'
#画像用のキャンバス作成(配置する場所,横幅,縦幅,ボーダー,bd以下の記述で余白を削除)
canvas=tk.Canvas(root,width=640,height=426,bd=0,highlightthickness=0,relief='ridge')
#キャンバスを設置(上下に20の余白)
canvas.pack(pady=20)

'''
#画像を用意
photo1=tk.PhotoImage(file='cat1.png')
#画像を描画(中点x,中点y,画像,タグ)
canvas.create_image(320,213,image=photo1,tag='p1')
#画像を用意
photo2=tk.PhotoImage(file='cat2.png')
#画像を描画(中点x,中点y,画像,タグ)
canvas.create_image(340,233,image=photo2,tag='p2')
canvas.delete('p2')
'''

#画像の配列
photos=[
        tk.PhotoImage(file='cat1.png'),
        tk.PhotoImage(file='cat2.png'),
        tk.PhotoImage(file='cat3.png'),
]
canvas.create_image(320,213,image=photos[index],tag='p1')

#ボタン作成(ボタンの文字,イベント)
btn=tk.Button(text='Click',command=btn_click)
#ボタン配置()
btn.pack(ipadx=10,ipady=5)
root.mainloop()
