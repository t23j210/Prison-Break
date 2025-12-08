# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Kitchen(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.img_room = pygame.image.load("res/kitchen/kitchen.png") #初期画像
        self.zoom_refrigerator = pygame.image.load("res/kitchen/zoom_refrigerator.png") #冷蔵庫
        self.item_battery = pygame.image.load("res/kitchen/item_battery.png") #バッテリー
        self.item_page2 = pygame.image.load("res/kitchen/item_page2.png") #ページ2
        self.zoom_state = 0
        self.item_sdriver_state = 0
        
    def click_event(self, x, y):
        if self.zoom_state == 0: #初期位置
            if (90 < x < 170) and (265 < y < 405):
                self.zoom_state = 1
            elif (725 < x < 819) and (486 < y < 524): #バッテリー入手
                self.item_sdriver_state = 1
                self.item_get[6] = True
            else:
                self.zoom_state = 0
        elif self.zoom_state == 1: #冷蔵庫
            if (333 < x <685) and (55 < y <640):
                if (436 < x < 469) and (202 < y < 237): #ページ2入手
                    self.item_sdriver_state = 2
                    self.item_get[7] = True
            else:
                self.zoom_state = 0
            
    def draw(self):
        self.screen.blit(self.img_room, (0,0)) #初期画像
        if self.zoom_state == 1:
           self.screen.blit(self.zoom_refrigerator, (0,0)) #冷蔵庫
           
    def next_state(self):
        return 2