import tkinter as tk
import datetime
import bisect
import time
import webbrowser as wb

dt = datetime.datetime.now()
li = [560,660,670,770,820,920,930,1030,1040,1140]

def now():
	dt = datetime.datetime.now()
	return dt.hour * 60 + dt.minute
def last():
	dt = datetime.datetime.now()
	return ("残り",li[bisect.bisect(li,now())]-now() -1 ,"分", 59 - dt.second,"秒")
def place():
	dt
def jst():
	wb.open("https://www.nict.go.jp/JST/JST5.html")
def transparence(): #透明化
	root.wm_attributes("-alpha", 0.8)
def	nomal():
	root.wm_attributes("-alpha", 1)



root = tk.Tk()
root.title(u"COUNTER GUI")
root.geometry("150x50")


def timePrint():
	now()
	lblMessage["text"] = last()
	
def repeat():
	timePrint()
	root.after(1000, repeat)#ループコード2

#ボタン
btnMessageDisp = tk.Button(root, text="JST", width="4", command=jst)
btnMessageDisp.place(x=100, y=25)

btnTransparence = tk.Button(root, text="透", width="1", command=transparence)
btnTransparence.place(x=100,y=0)

btnNomal = tk.Button(root, text="戻", width="1", command=nomal)
btnNomal.place(x=120,y=0)


# Label = 表示
lblMessage = tk.Label(root, text=u"残り時間")
lblMessage.place(x=5, y=20)

lblJyugyo = tk.Label(root,text="授業")
lblJyugyo.place(x=5,y=1)

root.after(1000, repeat)#ループコード１
root.attributes("-topmost", True) #最前面に固定
root.mainloop()