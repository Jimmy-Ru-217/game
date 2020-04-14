# coding=utf-8

import time
import logging
from src.template import Template,ran
import random


class KO(Template):
    def __init__(self):
        self.times = 0
        self.index = -1
        self.repair_flag = 0
        self.pair = 0
        self.core =[]
        super(KO, self).__init__()

    def detach(self):
        self.get_pic()
        if self.is_found(self.ps.test):
            print('test')
            return 1000
        else:
            return 0

    def sleep(self):
        random1=ran(self.times,self.times+149)
        #150次上限,次数越多休息几率越大 时间越多,最长0.75小时
        if random1>=150:
            self.times=0
            time.sleep(18*self.times)
    def touch(self):
        random1 = ran(1, 3)
        #模拟触摸
        if random1==3:
            x = ran(284, 475)
            y = ran(259, 593)
            self.mouse_left_click(x, y)
            time.sleep(0.2+random.random())
    def solve(self):
        while 1:
            self.sleep()
            #print(self.repair_flag)
            index = self.detach()
            if index == 11:
                self.touch()
                self.sleep()
                x = ran(490, 616)
                y = ran(510, 592)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
            time.sleep(0.2)
