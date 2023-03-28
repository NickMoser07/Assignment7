import turtle as t

t.seth(90)
def drawRectangle(height, width):
    t.speed(0)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)

def drawAllRectangles(x, y, height, width):
    t.seth(90)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for row in range(4):
        t.penup()
        t.setx(x)
        t.pendown()
        for rect in range(4):
            t.penup()
            t.sety(y + height*row*2)
            t.pendown()
            t.begin_fill()
            drawRectangle(height, width)
            t.end_fill()
            t.penup()
            t.rt(90)
            t.forward(width*2)
            t.lt(90)
            t.pendown()





def drawChessboard(x, y, width=250, height=250):
    #drawing board
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)


    #drawing rectangle

    #rectangle math
    rectheight = height/8
    rectwidth = width/8

    drawAllRectangles(x, y, rectwidth, rectheight)
    drawAllRectangles(x+rectwidth, y+rectheight,  rectwidth, rectheight)