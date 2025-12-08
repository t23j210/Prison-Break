# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Jail(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.img_room = pygame.image.load("res/jail/jail.png") #初期画像
        self.img_jail = pygame.image.load("res/jail/jail_no.png") #日記なし
        self.zoom_under_bed = pygame.image.load("res/jail/zoom_under_bed.png") #ベッドの下
        self.zoom_key = pygame.image.load("res/jail/zoom_key.png") #トイレの中の鍵
        self.close_safe = pygame.image.load("res/jail/zoom_under_bed(2).png") #ベッドの下（穴あき）
        self.zoom_toilet = pygame.image.load("res/jail/zoom_toiret.png") #何もないトイレ
        self.item_diary = pygame.image.load("res/jail/item_diary.png") #アイテム・日記
        self.item_key = pygame.image.load("res/jail/item_key.png") #アイテム・鍵
        self.item_page = pygame.image.load("res/jail/item_page.png") #アイテム・完成ページ
        self.zoom_state = 0
        self.item_sdriver_state = 0
        self.next_room = 0
    
    def click_event(self, x, y):
        if self.zoom_state == 0: #初期位置
            if (555 < x < 650) and (580 < y < 750):
                if self.lock_flag[0] == False: 
                    self.zoom_state = 1
                elif self.lock_flag[0] == True:
                    self.zoom_state = 5    
            elif (240 < x < 300) and (520 < y < 650): #鍵取得していたら何もないトイレの画像表示
                if self.item_get[1] == True:
                    self.zoom_state = 3
                else:
                    self.zoom_state = 2
            elif (95 < x < 223) and (523 < y < 575):
                self.item_sdriver_state = 1
                self.item_get[0] = True
                self.zoom_state = 4
            elif self.item_get[0] == True:
                self.zoom_state = 4           
            else:
                self.zoom_state = 0
        elif self.zoom_state == 1: #ベッドの下
            is_inside = (162 < x < 918) and (324 < y < 716)
            if self.lock_flag[0] == False:
                if self.item_use[10] == True:
                    if is_inside:
                        self.lock_flag[0] = True
                        self.zoom_state = 5
            if not is_inside:
                if self.item_get[0] == False:
                    self.zoom_state = 0
                elif self.item_get[0] == True: 
                    self.zoom_state = 4   
        elif self.zoom_state == 2:
            if (478 < x < 539) and (470 < y < 604):
                self.item_sdriver_state = 2
                self.item_get[1] = True
                self.zoom_state = 3
            else:
                if self.item_get[0] == False:
                    self.zoom_state = 0
                elif self.item_get[0] == True: 
                    self.zoom_state = 4 
        elif self.zoom_state == 3:
            if (0 < x < 1024) and (0 < y < 768):
                if self.item_get[0] == False:
                    self.zoom_state = 0
                elif self.item_get[0] == True: 
                    self.zoom_state = 4 
        elif self.zoom_state == 4:
            if (555 < x < 650) and (580 < y < 750):
                if self.lock_flag[0] == False: 
                    self.zoom_state = 1
                elif self.lock_flag[0] == True:
                    self.zoom_state = 5 
            elif (240 < x < 300) and (520 < y < 650):
                if self.item_get[1] == True:
                    self.zoom_state = 3
                else:
                    self.zoom_state = 2       
            else:
                self.zoom_state = 4
        elif self.zoom_state == 5:
            is_inside = (116 < x < 975  and 605 < y < 853)
            if is_inside:
                self.next_room = 4
            if not is_inside:
                if self.item_get[0] == False:
                    self.zoom_state = 0
                elif self.item_get[0] == True: 
                    self.zoom_state = 4      

    def draw(self):
        self.screen.blit(self.img_room, (0,0)) 
        if self.zoom_state == 1: #ベッドの下
            self.screen.blit(self.zoom_under_bed, (0,0))
        elif self.zoom_state == 2: #トイレ
            self.screen.blit(self.zoom_key, (0, 0))
        elif self.zoom_state == 3: #何もないトイレの画像
            self.screen.blit(self.zoom_toilet, (0, 0))
        elif self.zoom_state == 4:
            self.screen.blit(self.img_jail, (0, 0))
        elif self.zoom_state == 5: #ベット下（穴あき）
            self.screen.blit(self.close_safe, (0,0))
                    
    def next_state(self):
        next = self.next_room #次の部屋
        self.next_room = 1
        return next
