import pandas as pd
import numpy as np
import random

results=pd.read_excel("all_results.xlsx")
results = results.dropna(subset=[9])
df = results[results[9].str.contains('o')]
df= df.drop(9, axis=1)

def print_board(board):
    print("\n")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("\n")

def check_win(board, item):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == item:
            return True
    return False

board = [" " for x in range(9)]

my_item="x"
com_item="o"


def com_choice(df,choice):
    df= df[df[choice-1].str.contains('x')]
    num_o = df.apply(lambda x: x.str.count('o'))
    max_o_cols = num_o.columns[num_o.sum() == num_o.sum().max()].tolist()
    available_choices = [i for i, x in enumerate(board) if x == " "]
    for col in max_o_cols:
        if col in available_choices:
            computer_choice = col
            break
    df=df[df[computer_choice].str.contains('o')]
    return computer_choice, df



while True:
    print_board(board)
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = my_item
        if check_win(board, my_item):
            print("You win!\n")
            result=my_item
            break
        else:
            print("Your turn is over, computer is making move...\n")
            computer_choice, df=com_choice(df,choice)
            board[computer_choice] = com_item
            if check_win(board, com_item):
                print_board(board)
                print("Computer wins!\n")
                result=com_item
                board.append(result)
                son_oyun=pd.DataFrame([board])
                deneme=pd.concat([results,son_oyun])
                break
    else:
        print("Illegal move, try again.\n")



board.append(result)
son_oyun=pd.DataFrame([board])
deneme=pd.concat([results,son_oyun])
deneme.to_excel("all_results.xlsx",index=False)






