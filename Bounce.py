from tkinter import *
import random
import time

root =Tk()

root.title('Bounce')
root.resizable(0,0)
root.wm_attributes('-topmost', 1)


drawingpad = Canvas(root, width=500, height=500, bd=0, highlightthickness=0)
drawingpad.pack()
root.update()


#****code for the ball class*****

class Ball:

    def __init__(self, drawingpad, paddle, color):
        self.drawingpad = drawingpad
        self.paddle = paddle
        self.id = drawingpad.create_oval(10,10,25,25, fill=color)
        self.drawingpad.move(self.id,245, 100)
        start = [-3, -2, -1, 0, 1, 2, 3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-5
        self.drawingpad_height = self.drawingpad.winfo_height()
        self.drawingpad_width = self.drawingpad.winfo_width()
        self.hit_bottom = False


    def hit_paddle(self, pos):
        paddle_pos = self.drawingpad.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.drawingpad.move(self.id,self.x, self.y)
        pos = self.drawingpad.coords(self.id)
        print(pos)
        if pos[1] <= 0:
            self.y=5
        if pos[3] >= self.drawingpad_height:
            self.hit_bottom = True
            drawingpad.create_text(245, 100, text='GAME OVER!', fill='red')
        if pos[0] <= 0:
            self.x = 5
        if pos[2] >= self.drawingpad_width:
            self.x = -5
        if self.hit_paddle(pos) == True:
            self.y = -5




#****Class for the Bounce Paddle*****
class Paddle:
    def __init__(self, drawingpad, color):
        self.drawingpad=drawingpad
        self.id = drawingpad.create_rectangle(0,0, 100, 10, fill=color)
        self.drawingpad.move(self.id, 200, 300)
        self.x=0
        self.drawingpad_width=self.drawingpad.winfo_width()
        self.drawingpad.bind_all('<KeyPress-Left>', self.Turn_Left)
        self.drawingpad.bind_all('<KeyPress-Right>', self.Turn_Right)

    def draw(self):
        self.drawingpad.move(self.id,self.x,0)
        pos=self.drawingpad.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.drawingpad_width:
            self.x = 0

    def Turn_Left(self, event):
        self.x=-5

    def Turn_Right(self, event):
        self.x=5

#***code for creating instances/Object of the Classes*****
paddle = Paddle(drawingpad, 'red')
ball = Ball(drawingpad, paddle, 'blue')





#****code block for the main loop *****
while 1:
    if ball.hit_bottom == False:
        paddle.draw()
        ball.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.05)























