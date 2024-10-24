#乱数を使用してビンゴを作成
#1~75の範囲で値を出力(表示)
#1~75はリストに入れて（範囲指定で宣言）、pop関数を使って出力する
#listのとこの説明

#ビンゴの司会者が会場の大画面で利用するシステムを，GUIで構築する。
#ボタンを押すたびに，1から75までの範囲の整数をランダムに選んで表示する。値は重複してはいけない。
#選択した値はすべて記憶して，履歴表示させる

import tkinter as tk
from tkinter import messagebox
import random

#list
selected_num = []
unselected_num = [n for n in range(1,76)]

#乱数で数値を出力する関数
def bingo():
    ball_num = -1
    ball_num = random.choice(unselected_num)
    if ball_num >= 1 & 75 >= ball_num:
        selected_num.append(ball_num)
        unselected_num.remove(ball_num)
        #print(ball_num)
        #messagebox.showinfo(message=ball_num)
    
#ウィンドウ
root = tk.Tk()
root.minsize(400,400)

bingo_btn = tk.Button(root,text="押すと抽選",command=lambda:bingo)
bingo_btn.pack()

#label = tk.Label(text=f'{selected_number}' for selected_number in selected_num )

bingo_btn.bind("<Button-1>",bingo())

#ウィンドウの設定はmainloopの前に書く？
root.mainloop()


#参考にしたサイト
#https://note.nkmk.me/python-random-choice-sample-choices/
#https://note.nkmk.me/python-random-shuffle/
#https://note.nkmk.me/python-list-clear-pop-remove-del/
#https://note.nkmk.me/python-range-usage/
#https://atmarkit.itmedia.co.jp/ait/articles/2012/04/news020.html
#https://pythonsoba.tech/tkinter/#st-toc-h-42