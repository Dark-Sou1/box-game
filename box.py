import os
import sys

x = 100  # border
a = 0  # air
b = 2  # box
c = 1  # character
e = 3  # end

board = {
    # y'
    0: [x, x, x, x, x, x, x],
    1: [x, a, a, a, a, e, x],
    2: [x, a, a, a, a, a, x],
    3: [x, a, c, a, b, a, x],  # x
    4: [x, a, a, a, a, a, x],
    5: [x, a, a, a, a, a, x],
    6: [x, x, x, x, x, x, x]
}  # y


def main():
    inp = get_input()
    posx, posy = get_pos()
    os.system("cls")
    if inp == "w" or inp == "Key.up":
        if board[posy-1] == 0 or board[posy-1] == 6 or board[posy-1][posx]+c == 4:
            view()
        elif board[posy-1][posx]+c == 1:
            move("w")
            view()
        elif board[posy-1][posx]+c == 3:
            if board[posy-2][posx]+b == 2:
                move_box("w")
                move("w")
            elif board[posy-2][posx]+b == 5:
                won()
            view()
        else:
            view()
    elif inp == "s" or inp == "Key.down":
        if board[posy+1] == 0 or board[posy+1] == 6 or board[posy+1][posx]+c == 4:
            view()
        elif board[posy+1][posx]+c == 1:
            move("s")
            view()
        elif board[posy+1][posx]+c == 3:
            if board[posy+2][posx]+b == 2:
                move_box("s")
                move("s")
            elif board[posy+2][posx]+b == 5:
                won()
            view()
        else:
            view()
    elif inp == "a" or inp == "Key.left":
        if board[posy][posx-1]+c>100 or board[posy][posx-1]+c == 4:
            view()
        elif board[posy][posx-1]+c == 1:
            move("a")
            view()
        elif board[posy][posx-1]+c == 3:
            if board[posy][posx-2]+b == 2:
                move_box("a")
                move("a")
            elif board[posy][posx-2]+b == 5:
                won()
            view()
        else:
            view()
    elif inp == "d" or inp == "Key.right":
        if board[posy][posx+1]+c>100 or board[posy][posx+1]+c == 4:
            view()
        elif board[posy][posx+1]+c == 1:
            move("d")
            view()
        elif board[posy][posx+1]+c == 3:
            if board[posy][posx+2]+b == 2:
                move_box("d")
                move("d")
            elif board[posy][posx+2]+b == 5:
                won()
            view()
        else:
            view()



def get_pos():
    posx = 0
    posy = 0
    for i in board:
        for j in board[i]:
            if j == 1:
                return posx, posy
            posx += 1
        posx = 0
        posy += 1


def get_box_pos():
    posx = 0
    posy = 0
    for i in board:
        for j in board[i]:
            if j == 2:
                return posx, posy
            posx += 1
        posx = 0
        posy += 1


def move(direction):
    global board
    posx,posy = get_pos()
    if direction == "w":
        board[posy][posx] = 0
        board[posy-1][posx] = 1
    elif direction == "s":
        board[posy][posx] = 0
        board[posy+1][posx] = 1
    elif direction == "a":
        board[posy][posx] = 0
        board[posy][posx-1] = 1
    elif direction == "d":
        board[posy][posx] = 0
        board[posy][posx+1] = 1

def move_box(direction):
    global board
    posx,posy = get_box_pos()
    if direction == "w":
        board[posy][posx] = 0
        board[posy-1][posx] = 2
    elif direction == "s":
        board[posy][posx] = 0
        board[posy+1][posx] = 2
    elif direction == "a":
        board[posy][posx] = 0
        board[posy][posx-1] = 2
    elif direction == "d":
        board[posy][posx] = 0
        board[posy][posx+1] = 2


def won():
    print("you won")
    sys.exit()

inp = None

def get_input():
    from pynput import keyboard

    def on_press(key):
        global inp
        try:
            inp = key.char
        except AttributeError:
            inp = key
        return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    return str(inp)

def view():
    for i in board:
        for j in board[i]:
            if j == 100:
                j = '🟦'
            elif j == 1:
                j = '🤖'
            elif j == 2:
                j = '🍞'
            elif j == 0:
                j = '  '
            elif j == 3:
                j = '⬛'
            print(j,end="   ")
        print("\n")


if __name__ == "__main__":
    view()
    while True:
        main()
