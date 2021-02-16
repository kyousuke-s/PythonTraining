import tkinter as tk
key=''
#引数にイベントオブジェクトが渡される
def key_down(e):
    global key
    #e.keysymで押したボタンの名前を取得
    key=e.keysym
    #eが持っている情報が見れる(今回は情報を見るため。本来はいらない項目)
    print(e)

def key_up(e):
    global key
    key=''

cx=400
cy=300
#移動処理
def main_proc():
    global cx,cy
    if key=='Up':
        cy=cy-5
    if key=='Down':
        cy=cy+5
    if key=='Left':
        cx=cx-5
    if key=='Right':
        cx=cx+5
    #coords(コーズ)は表示中の画像を新しい位置に移動する
    canvas.coords('MYCHR',cx,cy)
    #afterは指定時間後に処理を実行する(ms,処理) 今回は1/10秒毎にmain_procを実行
    root.after(20,main_proc)

root=tk.Tk()
root.bind('<KeyPress>',key_down)#キーを押したときのイベントをバインド
root.bind('<KeyRelease>',key_up)#キーを離した時のイベントをバインド
canvas=tk.Canvas(width=800,height=600,bg='lightgreen')
canvas.pack()

img=tk.PhotoImage(file='mimi.png')
#作った画像にMYCHRというタグを付与
canvas.create_image(cx,cy,image=img,tag='MYCHR')
main_proc()
root.mainloop()

