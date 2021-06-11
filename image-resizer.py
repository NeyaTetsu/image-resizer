#初期設定
import cv2
import os
import glob
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


#ファイル選択
def click1():
    global paths
    if mode.get() == 0:
        paths = filedialog.askopenfilenames(initialdir=os.path.abspath(os.path.dirname(__file__)))
    else:
        paths = filedialog.askdirectory(initialdir=os.path.abspath(os.path.dirname(__file__)))
    print(paths)


#GUI
#メインウィンドウ
root = tk.Tk()
root.title(u'FileName Translate')
root.geometry('480x190')

#フレーム1（モード選択）
frame1 = tk.Frame(root)
frame1.pack(fill='x')

#ラベル1
modetitle = tk.Label(frame1,text=u'翻訳モード',font=('','20'))
modetitle.pack(side='left',anchor='w',fill='y',ipadx='50')
#ラジオボタン（翻訳モード選択）
mode = tk.IntVar()
mode.set(0)
mode1 = tk.Radiobutton(frame1,text=u'選択したファイル名を翻訳',value=0,variable=mode)
mode1.pack(anchor='nw')
mode2 = tk.Radiobutton(frame1,text=u'選択したディレクトリ内のファイル名を翻訳',value=1,variable=mode)
mode2.pack(anchor='nw')
mode3 = tk.Radiobutton(frame1,text=u'選択したディレクトリ名を翻訳',value=2,variable=mode)
mode3.pack(anchor='nw')


#フレーム2（パス指定）
frame2 = tk.Frame(root)
frame2.pack(fill='x')

#ラベル2
dialogtitle = tk.Label(frame2,text=u'パス',font=('','20'))
dialogtitle.pack(side='left',anchor='w',ipadx='80')
#ボタン（ファイル選択ダイアログを開く）
dialog = tk.Button(frame2,text='参照',command=click1)
dialog.pack(anchor='w',fill='x')

root.mainloop()