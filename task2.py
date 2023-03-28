import chessboard  
import turtle as t


#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    print("what is the width of your chess board")
    width = input()
    print("what is the height of your chessboard")
    height = input()
    starting = input("where do you want to start your board(x, y):  ")
    startX, startY = map(int, starting.split(", "))
    startX, startY = ((startX, startY))
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        chessboard.drawChessboard(startX, startY)
    elif height == "":
        chessboard.drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        chessboard.drawChessboard(startX, startY, height=eval(height))
    else:
        chessboard.drawChessboard(startX, startY, eval(width), eval(height))
    pause = input()

main()