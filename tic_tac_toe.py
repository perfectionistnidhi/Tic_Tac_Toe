board=[" " for i in range(9)]

#printing data

def display():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])

    print(f"\n{row1}\n{row2}\n{row3}\n")

#game logic   
def player_move(icon):
    if icon=='X':
        print(f"Player 1's Turn")
    else:
        print(f"Player 2's Turn")
    pos=int(input("Enter the position you want to insert in (1-9): "))
    if board[pos-1]==" ":
        board[pos-1]=icon
        
    else:
        print("\nThe space is taken!!")

#check if the game is draw

def is_draw():
    if " " in board:
        return False
    else:
        return True


# check who won the game
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
        
    
#game loop   
while True:
    display()
    player_move("X")
    display()
    if is_victory("X"):
        print("X Wins!!")
        break
    elif is_draw():
        print("It's a Draw..")
        break
    player_move("O")
    display()
    if is_victory("X"):
        print("X Wins!!")
        break
    elif is_draw():
        print("It's a Draw..")
        break




#ctrl+c to stop
