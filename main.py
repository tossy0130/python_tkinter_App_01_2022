from tkinter import *
import sys
import tkinter
import tkinter as tk

# ====================
# ウィンドウを作成
root = tk.Tk()

# ウィンドウズタイトル
root.title("なおにゃ校正チェック")

# ウィンドウサイズ
root.geometry("1200x600")

# === 入力 ボックス 01
text_box = tk.Text(bg="#000", fg="#fff", insertbackground="#fff", font=('', 16),
                   height=20, width=40, bd=10, relief="solid")

text_box.grid(row=2, column=0, padx=60, pady=10)
text_box.place(x=10, y=10, relx=0.1, rely=0.1)

# === 入力 ボックス 02
text_box2 = tk.Text(bg="#000", fg="#fff", insertbackground="#fff", font=('', 16),
                    height=20, width=40, bd=10, relief="solid")

text_box2.grid(row=2, column=0, padx=60, pady=10)
text_box2.place(x=100, y=10, relx=0.5, rely=0.1)

# テキストボックスの値を取得

# ボタン
ok_button = tk.Button(text="OK")
ok_button.place(relx=0.2, rely=0.2, y=400)

# ボタンが押された処理


def ok_click():
    #input_text01 = text_box.get("1.0", "end")
    # １文字ずつ配列に入れる
    input_text01_arr = list(text_box.get("1.0", "end-1c"))  # 改行コード取得　なし
    input_text02_arr = list(text_box2.get("1.0", "end-1c"))

    text01_arr_len = len(input_text01_arr)
    text02_arr_len = len(input_text02_arr)

    if text01_arr_len > text02_arr_len:
        for i in range(text02_arr_len):
            # ====== 文字列の比較
            if input_text02_arr[i] == input_text01_arr[i]:
                text_box2.insert(tk.END, input_text02_arr[i])
            else:
                # 文字の背景色を変える
                text_box2.insert(tk.END, "-")


# ボタンと function の紐づけ
ok_button["command"] = ok_click

# ウィンドウ表示継続
root.mainloop()
