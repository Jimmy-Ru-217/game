# coding=utf-8

import cv2


class PIC(object):
    def __init__(self):
        self.battle = cv2.imread('image/battle.bmp')
        self.combat = cv2.imread('image/combat.bmp')
        self.normal = cv2.imread('image/normal.bmp')
        self.command = cv2.imread('image/command.bmp')
        self.settlement = cv2.imread('image/settlement.bmp')
        self.share = cv2.imread('image/share.bmp')
        self.over = cv2.imread('image/over.bmp')
        self.restore = cv2.imread('image/restore.bmp')
        self.fast = cv2.imread('image/fast.bmp')
        self.full = cv2.imread('image/full.bmp')
        self.factory = cv2.imread('image/factory.bmp')
        self.emergency = cv2.imread('image/emergency.bmp')
        self.p5_6 = cv2.imread('image/5_6.png')
        self.start = cv2.imread('image/start.png')
        self.confirm = cv2.imread('image/confirm.png')
        self.plan =cv2.imread('image/plan.png')
        self.boss5 = cv2.imread('image/boss5.png')
        self.strength = cv2.imread('image/strength.png')
        self.logistics = cv2.imread('image/logistics.png')
        self.coresymbol = cv2.imread('image/coresymbol.png')

        self.test = cv2.imread('image/test.png')

        self.end1 = cv2.imread('image/end1.png')
        self.end2 = cv2.imread('image/end2.png')
        self.core = cv2.imread('image/core.png')
        self.corestar = cv2.imread('image/corestar.png')

        self.e2_4 = cv2.imread('image/E_2_4/2_4.png')
        self.boss2 = cv2.imread('image/E_2_4/boss2.png')
        self.end2_4_1 = cv2.imread('image/E_2_4/end1.png')
        self.end2_4_2 = cv2.imread('image/E_2_4/end2.png')

        self.e3_4 = cv2.imread('image/E_3_4/3_4.png')
        self.boss3 = cv2.imread('image/E_3_4/boss3.png')
        self.end3_4_1 = cv2.imread('image/E_3_4/end1.png')
        self.end3_4_2 = cv2.imread('image/E_3_4/end2.png')

        self.e4_4 = cv2.imread('image/E_4_4/4_4.png')
        self.boss4 = cv2.imread('image/E_4_4/boss4.png')
        self.end4_4_1 = cv2.imread('image/E_4_4/end1.png')
        self.end4_4_2 = cv2.imread('image/E_4_4/end2.png')

        self.n0_2 = cv2.imread('image/N_0_2/0_2.png')
        self.boss0 = cv2.imread('image/N_0_2/boss0.png')
        self.symbol0_2 = cv2.imread('image/N_0_2/command.png')
        self.action_10_0 = cv2.imread('image/N_0_2/action.png')
        self.action_10_1 = cv2.imread('image/N_0_2/action1.png')
        self.action_10_2 = cv2.imread('image/N_0_2/action2.png')

        self.vall = cv2.imread('image/vall/vall.png')
        self.chicken = cv2.imread('image/vall/chicken.png')
        self.vallsymbol = cv2.imread('image/vall/symbol.png')

        self.e_10_4 = cv2.imread('image/E_10_4/10_4.png')
        self.e_10_4_start_flag1 = cv2.imread('image/E_10_4/flag1.png')
        self.e_10_4_end_flag = cv2.imread('image/E_10_4/flag2.png')
        self.e_10_4_start_flag2 = cv2.imread('image/E_10_4/flag3.png')

        self.n4_6=cv2.imread('image/paper/N_4_6.png')
        self.n4_6_end1 = cv2.imread('image/paper/end1.png')
        self.n4_6_boss = cv2.imread('image/paper/boss4.png')
        self.n4_6_battle = cv2.imread('image/paper/battle.png')