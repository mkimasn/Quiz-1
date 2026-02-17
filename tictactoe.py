import tkinter as tk

#set up
playerX = "X"
playerO = "O"
curr_player = playerX
board = [" " for _ in range (9)]
buttons = [] 

lightpink = "#FFC7EB"
serenity = "#92A8D1"
pastelyellow = "#FFDC95"
white = "#FFFFFF"
text = "#332D2D"

turns = 0
game_over = False

def check_winner():
    global turns, game_over
    turns += 1
    
    #horizontal
    for row in range(3):
        
        if (board[row * 3] == board[row * 3 + 1] == board[row *3 + 2] and 
            board[row * 3] != " "):
            for col in range (3):
                index = row * 3 + col
                buttons[index].config(bg=lightpink, fg=text)
            label.config(text=f"{curr_player} is the winner!!", foreground=text)
            
            game_over = True
            return
        
    #vertical
    for col in range(3):
        if(board[col] == board[col + 3] == board[col + 6] and
           board[col] != " "):
            
            for row in range(3):
                index = row * 3 + col
                buttons[index].config(bg=lightpink, fg=text)
            label.config(text=f"{curr_player} is the winner!!", fg=text)
    
            game_over = True
            return

    #diagonal
    if (board [2] == board[4] == board[6] and board[2] != " "):
        for index in [2, 4, 6]:
            buttons[index].config(bg=lightpink, fg=text)
        label.config(text=f"{curr_player} is the winner!!", fg=text)
    
        game_over = True
        return
    
    #tie
    if (turns == 9):
        game_over = True
        label.config(text="It's a draw", fg=text)

def set_tile(row,column):
    global curr_player
    
    if (game_over):
        return
    
    index = row * 3 + column
    
    if board[index] != " ":
        return

    board[index] = curr_player
    buttons[index].config(text=curr_player)

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO
        
    label.config(text=curr_player + "'s turn")
    
    check_winner()

def new_game():
    global curr_player, board, turns, game_over
    
    curr_player = playerX
    board = [" " for _ in range(9)]
    turns = 0
    game_over = False
    
    if len(buttons) == 9:
        for i in range(9):
            buttons[i].config(text="", bg=serenity, fg=text) 
        label.config(text=curr_player + "'s turn", fg=text)

# ========== GUI SECTION ==========

#root setup
root = tk.Tk()
root.title("Tic Tac Toe") 
root.resizable(False, False)

frame = tk.Frame(root)
label= tk.Label(frame, text=curr_player+"'s turn", font=('Chalkboard SE', 18, "bold"), background=pastelyellow, 
                foreground=text)

label.grid(row=0, column=0, columnspan=3, pady=5)

#buttons
buttons = []  
for row in range(3):
    for column in range(3):
        button = tk.Button(frame, text="", font=('Chalkboard SE', 18, "bold"), background=serenity,
        foreground=text, width=5, height=2, command=lambda row=row, column=column: set_tile(row,column))

        button.grid(row=row+1, column=column)
        buttons.append(button)

# Restart button 
restart_btn = tk.Button(frame, text="restart", font=('Chalkboard SE', 18, "bold"), background=pastelyellow, 
                        foreground=text, command=new_game)
restart_btn.grid(row=4, column=0, columnspan=3, pady=5)

frame.pack()

root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width =root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root_x = int((screen_width/2) - (root_width/2))
root_y = int((screen_height/2)- (root_height/2))

root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")

root.mainloop()