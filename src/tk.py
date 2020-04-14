# coding=utf-8

import tkinter
import logging
import subprocess
import tkinter.messagebox

class TK(object):
    def __init__(self):#*号为未完成
        root = tkinter.Tk(className="少前减少精污 by:player217")
        self.root = root
        b0 = tkinter.Button(root, text="test", width=30, height=3, command=self.test)
        b0.pack()
        b1 = tkinter.Button(root, text="N_0_2", width=30, height=3, command=self.n_0_2)
        b1.pack()
        a2 = tkinter.Button(root, text="paper", width=30, height=3, command=self.paper)
        a2.pack()
        a3 = tkinter.Button(root, text="E_2_4", width=30, height=3, command=self.e_2_4)
        a3.pack()
        a4 = tkinter.Button(root, text="E_3_4", width=30, height=3, command=self.e_3_4)
        a4.pack()
        a5 = tkinter.Button(root, text="E_4_4", width=30, height=3, command=self.e_4_4)
        a5.pack()
        a6 = tkinter.Button(root, text="N_5_6", width=30, height=3, command=self.n_5_6)
        a6.pack()
        a7 = tkinter.Button(root, text="E_10_4", width=30, height=3, command=self.e_10_4)
        a7.pack()
        b3 = tkinter.Button(root, text="停止", width=30, height=3, command=self.stop)
        b3.pack()
        logging.info("Tk start.")
        self.list = []

    def start(self):
        self.root.mainloop()

    def e_10_4(self):
        tkinter.messagebox.showinfo(title='提示', message='开始')
        child = subprocess.Popen(["python", "main.py", "--mode", "E_10_4"])
        self.list.append(child)

    def paper(self):
        tkinter.messagebox.showinfo(title='提示', message='收集资料')
        child = subprocess.Popen(["python", "main.py", "--mode", "paper"])
        self.list.append(child)

    def test(self):
        tkinter.messagebox.showinfo(title='提示', message='开始测试')
        child = subprocess.Popen(["python", "main.py", "--mode", "test"])
        self.list.append(child)

    def e_2_4(self):
        tkinter.messagebox.showinfo(title='提示', message='提前将关卡选址第二大关紧急,第一梯队为打捞，初始弹药为满')
        child = subprocess.Popen(["python", "main.py", "--mode", "E_2_4"])
        self.list.append(child)

    def e_3_4(self):
        tkinter.messagebox.showinfo(title='提示', message='提前将关卡选址第三大关紧急,第一队狗粮第二队打捞,需要将缩放放至最大，且初始弹药为满')
        child = subprocess.Popen(["python", "main.py", "--mode", "E_3_4"])
        self.list.append(child)

    def e_4_4(self):
        tkinter.messagebox.showinfo(title='提示', message='提前将关卡选址第四大关紧急,第一队狗粮第二队打捞,需要将缩放放至最大，且初始弹药为满')
        child = subprocess.Popen(["python", "main.py", "--mode", "E_4_4"])
        self.list.append(child)

    def n_5_6(self):
        tkinter.messagebox.showinfo(title='提示', message='请提前将关卡选至第五大关，第一队位狗粮第二队为打捞队，需要将缩放放至最大，且初始弹药为满')
        child = subprocess.Popen(["python", "main.py", "--mode", "N_5_6"])
        self.list.append(child)

    def n_0_2(self):
        tkinter.messagebox.showinfo(title='提示', message='调至第0大关,缩放最大')
        child = subprocess.Popen(["python", "main.py", "--mode", "N_0_2"])
        self.list.append(child)



    def stop(self):
        logging.info("Stop.")
        for i in self.list:
            i.kill()
        self.list = []
        tkinter.messagebox.showinfo(title='提示', message='已停止')
        # import psutil
        # import os
        # pids = psutil.pids()
        # for pid in pids:
        #     p = psutil.Process(pid)
        #     if p.name() == 'main.exe':
        #         cmd = 'taskkill /F /IM main.exe'
        #         os.system(cmd)
