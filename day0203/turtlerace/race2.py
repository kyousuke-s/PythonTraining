import random
import turtle
ts=[]

def setup():
    global ts
    startline=-620
    screen=turtle.Screen()  #画面を設定
    screen.setup(1290,720)  #画面サイズ
    screen.bgpic('pavement.gif')    #画面背景

    t_y=[-40,-20,0,20,40]
    t_color=['blue','red','purple','brown','green']

    for i in range(len(t_y)):
        t=turtle.Turtle()
        t.shape('turtle')
        t.penup()
        t.setpos(startline,t_y[i])
        t.color(t_color[i])
        t.pendown()
        ts.append(t)

def race():
    global ts
    finishline=550
    t_speed=[[][][][][]]

    while True:
        for current_t in ts:
            if current_t.color()=='red':
                move=250
                current_t.forward(move)
            else:
                move=random.randint(0,10)
                current_t.forward(move)

            x=current_t.xcor()
            if x >= finishline:
                winner_color=current_t.color()
                current_t.write('Win!'+winner_color[0],font=('Arial',16,'normal'))
                break
        else:
            continue
        break

setup()
race()
turtle.mainloop()
