# coding=utf-8

import win32api
import win32con
import win32gui
import win32ui
import time
import logging
import cv2
import aircv
from src.img import PIC
from abc import ABCMeta, abstractmethod
import random

def ran(x,y):
    return random.randint(x,y)

class Template(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            filename='gf.log',
                            format='[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filemode='a')
        self.title = u'ドルフロ - MuMu模拟器'
        self.source = None
        self.hwnd = None
        self.pic = None
        #self.height = 576
        self.height = 1024
        self.weight = 1024
        self.ps = PIC()
        self.filename = 'image/temp.bmp'
        self.get_handle()

    @staticmethod
    def get_child_windows(parent):
        """
        获得parent的所有子窗口句柄
        返回子窗口句柄列表
        """
        if not parent:
            return
        hwnd_child_list = []
        win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwnd_child_list)
        return hwnd_child_list

    def get_pic(self):
        hwnd_dc = win32gui.GetWindowDC(self.hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        save_bit_map = win32ui.CreateBitmap()
        save_bit_map.CreateCompatibleBitmap(mfc_dc, self.weight, self.height)
        save_dc.SelectObject(save_bit_map)
        save_dc.BitBlt((0, 0), (self.weight, self.height), mfc_dc, (0, 0), win32con.SRCCOPY)
        save_bit_map.SaveBitmapFile(save_dc, self.filename)
        self.pic = cv2.imread(self.filename)
        win32gui.DeleteObject(save_bit_map.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwnd_dc)

    def get_handle(self):
        self.source = win32gui.FindWindow(None, self.title)
        logging.info("Source program is %d." % self.source)
        #self.hwnd = self.get_child_windows(self.source)[-1]
        self.hwnd = self.source
        #logging.info("Picture program is %d" % self.hwnd)

    # def clear(self):
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    #     time.sleep(0.02)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


    def mouse_left_click(self, x, y):
        hwnd = self.source
        #y += 19
        #逍遥判定
        #time.sleep(0.02)
        #win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        #time.sleep(0.02)
        #win32api.SendMessage(hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x+1, y-1))
        #win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(x - 1, y - 1))
        #time.sleep(0.02)
        #mumu判定
        time.sleep(0.02)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(0.02)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(0.02)

    def mouse_drag(self,x1,y1,x2,y2):#模拟鼠标拖拽，拖拽时间为1~2秒内,在矩形内随机拖拽,x1,y1左上角坐标,x2,y2右下角坐标
        hwnd = self.source
        time.sleep(0.05)
        a=1+(random.random())
        x=ran(x1,x2)
        y=ran(y1,y2)
        s1=int(2 * random.random())
        s2=int(2 * random.random())
        # xx与yy为鼠标松开的坐标
        if s1 == 1:
            xx=ran(x1,x)
        else:
            xx=ran(x,x2)
        if s2 == 1:
            yy=ran(y1,y)
        else:
            yy=ran(y,y2)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(a)
        win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(xx, yy))
        time.sleep(0.05)

    @staticmethod
    def find_pic(source, tmp):
        res = aircv.find_all_template(source, tmp)
        #print(res)
        r = []
        for dic in res:
            if dic['confidence'] < 0.9:
                continue
            r.append([int(x) for x in dic['result']])
        return r

    @staticmethod
    def find_pic1(source, tmp):
        res = aircv.find_all_template(source, tmp)
        #print(res)
        r = []
        for dic in res:
            if dic['confidence'] < 0.9:
                continue
            r.append([x for x in dic['rectangle']])
        return r
    def find_all(self, template):
        tmp = self.find_pic1(self.pic,template)
        #print(tmp)
        return tmp
    def is_found(self, template):
        tmp = self.find_pic(self.pic, template)

        if len(tmp) != 0:
            return 1
        else:
            return 0

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def solve(self):
        pass
