import tkinter as tk
import datetime
import bisect
import time

dt = datetime.datetime.now()
li = [660,770,920,1030,1140]
flag = False
def now():
	dt = datetime.datetime.now()
	return dt.hour * 60 + dt.minute
def last():
	dt = datetime.datetime.now()
	return ("残り",li[bisect.bisect(li,now())]-now() -1 ,"分", 59 - dt.second,"秒")

root = tk.Tk()
root.title(u"COUNTER GUI")
root.geometry("150x50")

def timePrint():
	now()
	lblMessage["text"] = last()
	
def repeat():
	timePrint()
	root.after(1000, repeat)#ループコード2

''' ボタン
btnMessageDisp = tk.Button(root, text="実行", width="12", command=timePrint)
btnMessageDisp.place(x=10, y=40)
'''

# Label = 表示
lblMessage = tk.Label(root, text=u"残り時間")
lblMessage.place(x=5, y=20)

root.after(1000, repeat)#ループコード１
root.attributes("-topmost", True) #最前面に固定
root.mainloop()