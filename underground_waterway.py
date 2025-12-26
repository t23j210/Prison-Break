# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base
from passlockcontrol import PasslockControl

class Underground_waterway(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use):
        super().__init__(screen, lock_flag, item_get, item_use)
        self.img_room0 = pygame.image.load("res/underground_waterway/underground_waterway0.png")
        self.img_room = pygame.image.load("res/underground_waterway/underground_waterway.png")
        self.zoom_underground_waterway = pygame.image.load("res/underground_waterway/zoom_underground_waterway.png")
        self.zoom_no_underground_waterway = pygame.image.load("res/underground_waterway/zoom_no_underground_waterway.png")
        self.zoom_door2 = pygame.image.load("res/underground_waterway/zoom_door2.png")
        self.zoom_password = pygame.image.load("res/underground_waterway/zoom_password.png")
        self.item_flame = pygame.image.load("res/underground_waterway/item_flame.png")
        self.zoom_state = 0
        self.item_sdriver_state = 0
        self.next_room = 5
        self.pcon = PasslockControl(screen, lock_flag)
        
    def click_event(self, x, y):
        if self.zoom_state == 0:
            if self.lock_flag[5] == False:
                if self.item_use == [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]:
                    if (0 < x < 1024) and (0 < y < 709):
                        self.lock_flag[5] = True
                        self.zoom_state = 5
                        self.item_use[14] = False
                elif (0 < x < 1024) and (710 < y < 768):
                    self.next_room = 4                       
        elif self.zoom_state == 5:
            if (507 < x < 564) and (296 < y < 392):
                self.zoom_state = 1
            elif (348 < x < 692) and (531 < y < 748):
                if self.item_get[10] == True:
                    self.zoom_state = 4
                else:    
                    self.zoom_state = 2
            elif (0 < x < 1024) and (710 < y < 768):
                self.next_room = 4        
            else:
                self.zoom_state = 5
        elif self.zoom_state == 1:
            if (574 < x < 646) and (342 < y < 448):
                self.zoom_state = 3
            else:
                self.zoom_state = 5
        elif self.zoom_state == 2:
            if (403 < x < 707) and (414 < y < 533):
                if self.item_sdriver_state == 0:
                    self.item_sdriber_state = 1
                    self.item_get[10] = True
                self.zoom_state = 4
            else:
                self.item_sdriver_state = 0
                self.zoom_state = 5
        elif self.zoom_state == 3:
            if (378 < x < 696) and (128 < y < 669):
                self.pcon.onclick(x,y)
                if self.lock_flag[6] == True:
                    self.next_room = 6
            else:
                self.zoom_state = 1
        elif self.zoom_state == 4:
            if (0 < x < 1024) and (0 < y < 768):
                self.zoom_state = 5
    def draw(self):
        self.screen.blit(self.img_room0, (0, 0))
        if self.zoom_state == 1:
            self.screen.blit(self.zoom_door2, (0, 0))
        elif self.zoom_state == 2:
            self.screen.blit(self.zoom_underground_waterway, (0, 0))
        elif self.zoom_state == 3:
            self.screen.blit(self.zoom_password, (0, 0))
            self.pcon.disp_password()
        elif self.zoom_state == 4:
            self.screen.blit(self.zoom_no_underground_waterway, (0, 0))
        elif self.zoom_state == 5:
            self.screen.blit(self.img_room, (0, 0))         
    def next_state(self):
        next = self.next_room #次の部屋
        self.next_room = 5
        return next
    
    def next_music(self):
        return 5