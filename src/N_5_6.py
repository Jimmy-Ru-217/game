# coding=utf-8

import time
import logging
from template import Template,ran
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
        if self.is_found(self.ps.battle) and not self.is_found(self.ps.restore):
            logging.info("主界面且无修理")
            return 1
        elif self.is_found(self.ps.emergency) and self.repair_flag==0:
            logging.info("队伍重创")
            return 18
        elif self.is_found(self.ps.p5_6) and not self.repair_flag and not self.is_found(self.ps.normal):
            logging.info("任务选择")
            return 2
        elif self.is_found(self.ps.normal) :
            logging.info("选择作战")
            return 3
        elif  self.is_found(self.ps.boss5) and self.is_found(self.ps.start) :
            logging.info("初始任务地图并且执行")
            return 4
        elif self.is_found(self.ps.end1) and self.is_found(self.ps.end2):
            logging.info("结束本局")
            return 5
        elif self.is_found(self.ps.settlement) or self.is_found(self.ps.share) or self.is_found(self.ps.over):
            logging.info("结算")
            return 6
        elif self.is_found(self.ps.corestar):
            self.core=self.find_all(self.ps.core)
            logging.info("获得核心")
            return 7
        elif self.is_found(self.ps.p5_6) and self.repair_flag:
            logging.info("任务选择&需要修复")
            return 8
        elif self.is_found(self.ps.battle) and self.is_found(self.ps.restore):
            logging.info("位于主界面且需要修理")
            return 13
        elif self.is_found(self.ps.fast):
            logging.info("快速修理")
            return 14
        elif self.is_found(self.ps.full):
            logging.info("仓库满了")
            return 15
        elif self.is_found(self.ps.factory)and self.is_found(self.ps.strength):
            logging.info("强化")
            return 16
        else:
            time.sleep(0.2)
            return 0

    def sleep(self):
        random1=ran(self.times,self.times+149)
        #150次上限,次数越多休息几率越大 时间越多,最长0.75小时
        if random1>=150:
            self.times=0
            time.sleep(18*self.times)

    def touch(self):
        random1 = ran(1, 4)
        #模拟触摸
        if random1==3:
            x = ran(284, 475)
            y = ran(259, 593)
            self.mouse_left_click(x, y)
            time.sleep(0.2+random.random())

    def drag(self):#模拟拖拽
        random1= ran(1,2)
        if random1==1:
            self.mouse_drag(51,103,489,649)
            time.sleep(0.2 + random.random())

    def solve(self):
        while 1:
            #print(self.repair_flag)
            index = self.detach()
            if index == 1:
                self.touch()
                self.sleep()
                x = ran(490, 616)
                y = ran(510, 592)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
            elif index == 2:
                x=ran(250,765)
                y=ran(493,555)
                self.mouse_left_click(x, y)
                time.sleep(1 + random.random())
            elif index == 3:
                x = ran(403, 495)
                y = ran(496, 539)
                self.mouse_left_click(x, y)
                time.sleep(1 + random.random())
            elif index == 4:
                #基地
                x = ran(583, 637)
                y = ran(618, 674)
                self.mouse_left_click(x, y)
                time.sleep(0.5 + random.random())
                #确定
                x = ran(661, 762)
                y = ran(539, 578)
                self.mouse_left_click(x, y)
                time.sleep(0.3 + random.random())
                #飞机
                x = ran(610, 658)
                y = ran(99, 148)
                self.mouse_left_click(x, y)
                time.sleep(0.6 + random.random())
                #确定
                x = ran(661, 762)
                y = ran(539, 578)
                self.mouse_left_click(x, y)
                time.sleep(0.3 + random.random())
                #开始
                x = ran(601, 763)
                y = ran(701, 762)
                self.mouse_left_click(x, y)
                time.sleep(3.5 + random.random()*2)
                #飞机
                x = ran(610, 658)
                y = ran(99, 148)
                self.mouse_left_click(x, y)
                time.sleep(0.2 + random.random()*0.5)
                #补给
                if self.pair==2 :
                    x = ran(610, 658)
                    y = ran(99, 148)
                    self.mouse_left_click(x, y)
                    time.sleep(0.6 + random.random())
                    x = ran(650, 770)
                    y = ran(489, 527)
                    self.mouse_left_click(x, y)
                    time.sleep(1.5 + random.random())
                    self.pair=0
                elif self.pair ==1:
                    if int(2*random.random())==1:
                        x = ran(610, 658)
                        y = ran(99, 148)
                        self.mouse_left_click(x, y)
                        time.sleep(0.6 + random.random())
                        x = ran(650, 770)
                        y = ran(489, 527)
                        self.mouse_left_click(x, y)
                        time.sleep(1.5 + random.random())
                        self.pair=0
                else:
                    pass
                self.pair=self.pair+1

                #计划
                x = ran(10, 89)
                y = ran(685, 706)
                self.mouse_left_click(x, y)
                time.sleep(0.7 + random.random())
                #boss
                x = ran(76, 121)
                y = ran(117, 166)
                self.mouse_left_click(x, y)
                time.sleep(0.7 + random.random())
                #执行
                x = ran(659, 759)
                y = ran(712, 760)
                self.mouse_left_click(x, y)
                time.sleep(0.7 + random.random())
            elif index == 5:
                self.times = self.times+1
                x = ran(659, 759)
                y = ran(712, 760)
                self.mouse_left_click(x, y)
                time.sleep(0.7 + random.random())
                self.sleep()
            elif index == 6:
                for _ in range(ran(2,5)):
                    x = ran(100, 700)
                    y = ran(100, 700)
                    self.mouse_left_click(x, y)
                    time.sleep(0.06+random.random()*0.5)
            elif index == 7:
                if self.core !=[]:
                    for i in self.core:#选择所有三星
                        x = ran(i[0][0], i[3][0])
                        y = ran(i[0][1], i[3][1])
                        self.mouse_left_click(x, y)
                        time.sleep(0.6 + random.random() * 0.5)
                    #选择确定
                    x = ran(659, 760)
                    y = ran(342, 413)
                    self.mouse_left_click(x, y)
                    time.sleep(1 + random.random())
                    #拆解
                    x = ran(660, 762)
                    y = ran(687, 730)
                    self.mouse_left_click(x, y)
                    time.sleep(1 + random.random())
                    #确定
                    x = ran(399, 501)
                    y = ran(446, 484)
                    self.mouse_left_click(x, y)
                    time.sleep(1 + random.random())
                    # 返回
                    x = ran(10, 51)
                    y = ran(6, 41)
                    self.mouse_left_click(x, y)
                    time.sleep(2 + random.random())
                else:
                    x = ran(10, 51)
                    y = ran(6, 41)
                    self.mouse_left_click(x, y)
                    time.sleep(0.5)
                    x = ran(10, 51)
                    y = ran(6, 41)
                    self.mouse_left_click(x, y)
                    time.sleep(2 + random.random())
            elif index == 8:#需要修复返回
                x = ran(10, 51)
                y = ran(6, 41)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
            elif index == 13:
                #修理
                x = ran(590, 619)
                y = ran(362, 394)
                self.mouse_left_click(x,y)
                time.sleep(0.6 + random.random())
                time.sleep(3.0)
            elif index == 14:
                #快速修理
                self.repair_flag = 0
                x = ran(35, 130)
                y = ran(260, 570)
                self.mouse_left_click(x, y)
                time.sleep(0.6 + random.random())
                time.sleep(0.5)
                x = ran(10,105)
                y = ran(70, 239)
                self.mouse_left_click(x, y)
                time.sleep(0.1+ random.random())
                x = ran(120, 210)
                y = ran(70, 239)
                self.mouse_left_click(x, y)
                time.sleep(0.1+random.random())
                #确定
                x = ran(662, 766)
                y = ran(298, 365)
                self.mouse_left_click(x, y)
                time.sleep(0.6 + random.random())
                x = ran(169, 212)
                y = ran(450, 497)
                self.mouse_left_click(x, y)
                time.sleep(0.5 + random.random())
                x = ran(504, 606)
                y = ran(453, 493)
                self.mouse_left_click(x, y)
                time.sleep(0.5 + random.random())
                #返回
                x = ran(10, 51)
                y = ran(6, 41)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
                x = ran(10, 51)
                y = ran(6, 41)
                self.mouse_left_click(x, y)
                time.sleep(3 + random.random())
            elif index == 15:
                x = ran(428, 538)
                y = ran(448, 485)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
            elif index == 16:#仓库界面
                #选择强化角色
                x = ran(138, 245)
                y = ran(245, 561)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
                #选择第一个强化角色
                x = ran(9, 108)
                y = ran(67, 242)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
                #被强化角色（二星枪）
                x = ran(267, 371)
                y = ran(93, 161)
                self.mouse_left_click(x, y)
                time.sleep(1 + random.random())
                #智能选择&确定
                x = ran(659, 760)
                y = ran(342, 413)
                self.mouse_left_click(x, y)
                time.sleep(0.5)
                x = ran(659, 760)
                y = ran(342, 413)
                self.mouse_left_click(x, y)
                time.sleep(1 + random.random())

                #强化
                x = ran(660, 762)
                y = ran(687, 730)
                self.mouse_left_click(x, y)
                time.sleep(1 + random.random())
                #回收拆解
                x = ran(4, 105)
                y = ran(237, 290)
                self.mouse_left_click(x, y)
                time.sleep(0.5)
                x = ran(4, 105)
                y = ran(237, 290)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
                #选择拆解人行选项
                x = ran(157, 265)
                y = ran(85, 149)
                self.mouse_left_click(x, y)
                time.sleep(2 + random.random())
            elif index == 18:
                self.repair_flag = 1
            else:
                pass
            time.sleep(0.2)
