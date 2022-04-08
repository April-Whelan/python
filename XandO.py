def pickX(selected):
    x = int(input("pick x "))
    if x > 8 or x < 0:
        print("out of range, choose between 0 and 8")
        pickX(selected)
    if selected[x] == "X":
        print("Already X")
        pickX(selected)
    elif selected[x] == "O":
        print("Already O")
        pickX(selected)
    else:
        selected[x] = "X"
    return selected

def pickO(selected):  
    o = int(input("pick o "))
    if o > 8 or o < 0:
        print("out of range, choose between 0 and 8")
        pickO(selected)
    if selected[o] == "O":
        print("Already O")
        pickO(selected)
    elif selected[o] == "X":
        print("Already x")
        pickO(selected)
    else:
        selected[o] = "O"
    return selected

def checkWin(selected,char):
    #across
    if selected[0] == char and selected[1] == char and selected[2] == char :
       return char
    if selected[3] == char and selected[4] == char and selected[5] == char :
       return char
    if selected[6] == char and selected[7] == char and selected[8] == char :
       return char
    #down
    if selected[0] == char and selected[3] == char and selected[6] == char :
       return char
    if selected[1] == char and selected[4] == char and selected[7] == char :
       return char
    if selected[2] == char and selected[5] == char and selected[8] == char:
       return char
    #diagonal
    if selected[0] == char and selected[5] == char and selected[8] == char:
       return "X"
    return ""
def grid(row,col,width,height,selected):
    across = "-"*width + " "
    down = "|"+ " %s "
    out= ""
    count = 0
    roof = row + 1

    for line in range(0, roof+row):
        if count%2 == 0: 
            out += " " +(across*col)
            out +="\n"
        else:
            walls = (down* col) + "|" + "\n"
            out+= walls * height
        count+=1

    print(out %tuple(selected)) 


gameOver = False
selected = [" "," "," "," "," "," "," "," "," "]
count = 0
while not gameOver :
    
    grid(3,3,3,1,selected)
    if checkWin(selected,"X") == "X":
        print("X wins")
        gameOver = True
    if checkWin(selected,"O") == "O":
        print("O wins")
        gameOver = True

 
    
    pickX(selected)
    count+=1

    grid(3,3,3,1,selected)
    if checkWin(selected,"X") == "X":
        print("X wins")
        gameOver = True
    if checkWin(selected,"O") == "O":
        print("O wins")
        gameOver = True
        
    if count <= 8 and not gameOver:  
        pickO(selected)
        count+=1
    else:
        gameOver = True
        
grid(3,3,3,1,selected)
if checkWin(selected,"X") == "X":
    print("X wins")
if checkWin(selected,"O") == "O":
    print("O wins")
else:
    print("out of tries, no one wins")
