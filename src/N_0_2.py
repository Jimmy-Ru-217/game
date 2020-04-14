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
        self.core = []
        super(KO, self).__init__()

    def detach(self):
        self.get_pic()
        if self.is_found(self.ps.battle) and not self.is_found(self.ps.restore):
            #logging.info("主界面且无修理")
            return 1
        elif self.is_found(self.ps.n0_2) and not self.repair_flag and not self.is_found(self.ps.normal):
            #logging.info("任务选择")
            return 2
        elif self.is_found(self.ps.normal) :
            #logging.info("选择作战")
            return 3
        elif self.is_found(self.ps.start) and self.is_found(self.ps.symbol0_2) :
            #logging.info("初始任务地图并且执行")
            return 4
        elif self.is_found(self.ps.action_10_0) and self.is_found(self.ps.action_10_1)and self.is_found(self.ps.action_10_2):
            #行动
            return 5
        elif self.is_found(self.ps.settlement) or self.is_found(self.ps.share) or self.is_found(self.ps.over):
            #logging.info("结算")
            return 6
        elif self.is_found(self.ps.factory) and self.is_found(self.ps.coresymbol):
            self.core = self.find_all(self.ps.core)
            #logging.info("选择分解的人形")
            return 7
        elif self.is_found(self.ps.n0_2) and self.repair_flag:
            #logging.info("任务选择&需要修复")
            return 8
        elif self.is_found(self.ps.battle) and self.is_found(self.ps.restore):
            #logging.info("位于主界面且需要修理")
            return 13
        elif self.is_found(self.ps.fast):
            #logging.info("快速修理")
            return 14
        elif self.is_found(self.ps.full):
            #logging.info("仓库满了")
            return 15
        elif self.is_found(self.ps.factory)and self.is_found(self.ps.strength):
            #logging.info("前往分解")
            return 16
        elif self.is_found(self.ps.logistics):
            #logging.info("后勤")
            return 17
        elif self.is_found(self.ps.emergency) and self.repair_flag==0:
            #logging.info("队伍重创")
            return 18
        else:
            time.sleep(0.2)





    def solve(self):
        flag=1
        while 1:
            #print(self.repair_flag)
            index = self.detach()
            if index == 1:
                x = ran(625, 746)
                y = ran(696, 758)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
            elif index == 2:
                x=ran(308,908)
                y=ran(306,369)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(1 + random.random())
            elif index == 3:
                x = ran(491, 602)
                y = ran(656, 703)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(random.random()*0.5)
            elif index == 4:
                time.sleep(2)
                #基地
                x = ran(460, 492)
                y = ran(536, 572)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #部队编成
                time.sleep(2+random.random())
                x = ran(120, 230)
                y = ran(690, 715)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                if flag ==1:
                    flag = 0
                    time.sleep(3 + random.random())
                    #第一梯队第二位
                    x = ran(247, 347)
                    y = ran(374, 622)
                    self.mouse_left_click(x, y)
                    del x
                    del y
                    time.sleep(0.8 + random.random()*0.5)
                    time.sleep(2 + random.random())
                    #选择M4
                    x = ran(150, 254)
                    y = ran(135, 308)
                    self.mouse_left_click(x, y)
                    del x
                    del y
                    time.sleep(0.8 + random.random()*0.5)
                    time.sleep(2 + random.random())
                    # #选择第二梯队
                    # x = ran(9, 72)
                    # y = ran(230, 260)
                    # self.mouse_left_click(x, y)
                    # time.sleep(0.3 + random.random()*0.5)
                    # time.sleep(2 + random.random())
                    # #选择第二梯队第一位
                    # x = ran(113, 214)
                    # y = ran(367, 558)
                    # self.mouse_left_click(x, y)
                    # time.sleep(0.3 + random.random()*0.5)
                    # time.sleep(2 + random.random())
                    # #选择aug
                    # x = ran(149, 246)
                    # y = ran(342, 530)
                    # self.mouse_left_click(x, y)
                    # time.sleep(0.3 + random.random()*0.5)
                    #返回
                    x = ran(5, 86)
                    y = ran(61, 104)
                    self.mouse_left_click(x, y)
                    del x
                    del y
                    time.sleep(0.3 + random.random()*0.5)

                elif flag==0:
                    flag = 1
                    #第一梯队第二位
                    time.sleep(3 + random.random())
                    x = ran(247, 347)
                    y = ran(374, 622)
                    self.mouse_left_click(x, y)
                    del x
                    del y
                    time.sleep(0.3 + random.random()*0.5)
                    #选择ar15
                    time.sleep(1 + random.random())
                    x = ran(284, 389)
                    y = ran(128, 326)
                    self.mouse_left_click(x, y)
                    del x
                    del y
                    time.sleep(0.3 + random.random()*0.5)
                    # #选择第二梯队
                    # time.sleep(2 + random.random())
                    # x = ran(9, 72)
                    # y = ran(230, 260)
                    # self.mouse_left_click(x, y)
                    # time.sleep(0.3 + random.random()*0.5)
                    # #选择第二梯队第一位
                    # time.sleep(2 + random.random())
                    # x = ran(113, 214)
                    # y = ran(367, 558)
                    # self.mouse_left_click(x, y)
                    # time.sleep(0.3 + random.random()*0.5)
                    # #选择416
                    # time.sleep(2 + random.random())
                    # x = ran(6, 121)
                    # y = ran(337, 504)
                    # self.mouse_left_click(x, y)
                    # time.sleep(0.3 + random.random()*0.5)
                    #返回
                    x = ran(5, 86)
                    y = ran(61, 104)
                    self.mouse_left_click(x, y)
                    del x
                    del y
                    time.sleep(0.3 + random.random()*0.5)
                #基地
                time.sleep(4+random.random()*0.5)
                x = ran(460, 492)
                y = ran(536, 572)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #确定
#                time.sleep(1.5)
                x = ran(827, 910)
                y = ran(720, 746)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #飞机
#                time.sleep(1.5)
                x = ran(322, 348)
                y = ran(530, 556)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #确定
#                time.sleep(1)
                x = ran(827, 910)
                y = ran(720, 746)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #开始
#                time.sleep(3)
                x = ran(737, 935)
                y = ran(909, 965)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #飞机
                time.sleep(4)
                x = ran(322, 348)
                y = ran(530, 556)
                self.mouse_left_click(x, y)
                time.sleep(1.3 + 0.5*random.random())
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                # #飞机
                #
                # x = ran(312, 350)
                # y = ran(531, 571)
                # self.mouse_left_click(x, y)
                # del x
                # del y
                # time.sleep(0.8 + random.random())
                #补给
                x = ran(824, 915)
                y = ran(654, 683)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(1.3 + random.random()*0.5)

            elif index==5:
                #随机点其他地方
                # x = ran(104, 613)
                # y = ran(616, 879)
                # self.mouse_left_click(x, y)
                # time.sleep(1.3 + random.random()*0.5)
                #基地
                x = ran(464, 488)
                y = ran(541, 567)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(1.3 + random.random()*0.5)
                #计划
                x = ran(15, 103)
                y = ran(893, 908)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #第一部
                x = ran(470, 490)
                y = ran(355, 373)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #第二部
                x = ran(419, 441)
                y = ran(427, 450)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #第三部
                x = ran(415, 437)
                y = ran(317, 339)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                #第四部
                x = ran(620, 635)
                y = ran(390, 410)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random()*0.5)
                #执行
                time.sleep(1)
                x = ran(825, 927)
                y = ran(929, 966)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.8 + random.random())
                time.sleep(6)
            elif index == 6:
                for _ in range(ran(2,5)):
                    x = ran(100, 700)
                    y = ran(120, 720)
                    self.mouse_left_click(x, y)
                    del x
                    del y
                    time.sleep(0.06+random.random()*0.5)

            #全部拆解
            elif index == 7:
                # 自动确定（拆掉二星，在需要强化时候需要注释）
                #------------------------------------------

                x = ran(820, 922)
                y = ran(493, 546)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(1 + random.random())

                #------------------------------------------
                time.sleep(1)
                if self.core !=[]:
                    for i in self.core:#选择所有三星
                        x = ran(i[0][0], i[3][0])
                        y = ran(i[0][1], i[3][1])
                        self.mouse_left_click(x, y)
                        del x
                        del y
                        time.sleep(0.6 + random.random() * 0.5)
                #选择确定
                x = ran(820, 922)
                y = ran(493, 546)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(1 + random.random())
                #拆解
                x = ran(812, 911)
                y = ran(902, 933)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(1 + random.random())
                #确定
                x = ran(504, 626)
                y = ran(692, 739)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(1 + random.random())
                # 返回
                x = ran(5, 86)
                y = ran(61, 104)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())

            elif index == 8:#需要修复返回
                x = ran(5, 86)
                y = ran(61, 104)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
            elif index == 13:
                #修理
                x = ran(616, 739)
                y = ran(490, 550)
                self.mouse_left_click(x,y)
                del x
                del y
                time.sleep(0.6 + random.random())
                time.sleep(3.0)
            elif index == 14:
                #快速修理
                self.repair_flag = 0
                x = ran(40, 145)
                y = ran(393, 670)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.6 + random.random())
                time.sleep(0.5)
                x = ran(10,113)
                y = ran(140, 322)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.1+ random.random())
                #确定
                x = ran(821, 925)
                y = ran(424, 480)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.6 + random.random())
                x = ran(208, 245)
                y = ran(612, 643)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.5 + random.random())
                x = ran(631, 722)
                y = ran(612, 635)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(0.5 + random.random())
                #返回
                x = ran(5, 86)
                y = ran(61, 104)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
                x = ran(5, 86)
                y = ran(61, 104)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(3 + random.random())
            elif index == 15:
                x = ran(541, 652)
                y = ran(593, 630)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
            elif index == 16:#仓库界面
                #不需要强化时注释
                #-------------------------------------------------------

                # #选择强化角色
                # x = ran(182, 292)
                # y = ran(364, 696)
                # self.mouse_left_click(x, y)
                # time.sleep(2 + random.random())
                # #选择第一个强化角色
                # x = ran(27, 110)
                # y = ran(131, 258)
                # self.mouse_left_click(x, y)
                # time.sleep(2 + random.random())
                # #被强化角色（二星枪）
                # x = ran(332, 441)
                # y = ran(153, 204)
                # self.mouse_left_click(x, y)
                # time.sleep(1 + random.random())
                # #智能选择&确定
                # x = ran(818, 924)
                # y = ran(461, 508)
                # self.mouse_left_click(x, y)
                # time.sleep(0.5)
                # x = ran(818, 924)
                # y = ran(461, 508)
                # self.mouse_left_click(x, y)
                # time.sleep(1 + random.random())
                #
                # #强化
                # x = ran(817, 936)
                # y = ran(885, 931)
                # self.mouse_left_click(x, y)
                # time.sleep(1 + random.random())
                # #关闭
                # x = ran(2, 120)
                # y = ran(325, 365)
                # self.mouse_left_click(x, y)
                # time.sleep(2 + random.random())
                #-------------------------------------------------------
                #回收拆解
                x = ran(2, 120)
                y = ran(355, 385)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
                #选择拆解人行选项
                x = ran(219, 309)
                y = ran(169, 211)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
            elif index == 17:
                x = ran(100, 800)
                y = ran(120, 820)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
                x = ran(493, 596)
                y = ran(604, 635)
                self.mouse_left_click(x, y)
                del x
                del y
                time.sleep(2 + random.random())
            elif index == 18:
                self.repair_flag = 1
            else:
                pass
            time.sleep(0.2)
