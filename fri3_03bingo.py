#乱数を使用してビンゴを作成
#1~75の範囲で値を出力(表示)
#1~75はリストに入れて（範囲指定で宣言）、pop関数を使って出力する
#listのとこの説明

#ビンゴの司会者が会場の大画面で利用するシステムを，GUIで構築する。
#ボタンを押すたびに，1から75までの範囲の整数をランダムに選んで表示する。値は重複してはいけない。
#選択した値はすべて記憶して，履歴表示させる

import tkinter as tk
from tkinter import messagebox as tkmsg
import random

#list
selected_num = []
unselected_num = [n for n in range(1,76)]

#乱数で数値を出力する関数
def bingo(shoki):
    ball_num = shoki
    print(ball_num)
    ball_num = random.choice(unselected_num)
    print(ball_num)
    if 75 >= ball_num >= 1:
        selected_num.append(ball_num)
        unselected_num.remove(ball_num) 
        #tkmsg.showinfo("出力する値",f"{ball_num}")
        print(selected_num)
        bingo_label.config(text=f"乱数リスト: {selected_num}")
    
#ウィンドウ
root = tk.Tk()
root.minsize(400,400)

bingo_btn = tk.Button(root,text="押すと抽選",command=lambda:bingo(-1))
bingo_label = tk.Label(root,text = "[]")
bingo_btn.pack()
bingo_label.pack()

#ウィンドウの設定はmainloopの前に書く？
root.mainloop()


#参考にしたサイト
#https://note.nkmk.me/python-random-choice-sample-choices/
#https://note.nkmk.me/python-random-shuffle/
#https://note.nkmk.me/python-list-clear-pop-remove-del/
#https://note.nkmk.me/python-range-usage/
#https://atmarkit.itmedia.co.jp/ait/articles/2012/04/news020.html
#https://pythonsoba.tech/tkinter/#st-toc-h-42