# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:05:46 2020

@author: rufiy
"""

import pygame
from room_base import Room_Base

class Storage_room(Room_Base):
    def __init__(self, screen, lock_flag, item_get, item_use, se):
        super().__init__(screen, lock_flag, item_get, item_use, se)
        self.img_room1 = pygame.image.load("res/storage_room/storage_room.png") #初期部屋
        self.img_room2 = pygame.image.load("res/storage_room/storage_room_no.png") #懐中電灯なしver
        self.zoom_door = pygame.image.load("res/storage_room/zoom_door1.png") #扉
        self.zoom_door2 = pygame.image.load("res/storage_room/zoom_door_no.png") #鍵なし扉
        self.item_flashlight = pygame.image.load("res/storage_room/item_flashlight.png") #懐中電灯
        self.item_page3 = pygame.image.load("res/storage_room/item_page3.png") #ページ3
        self.img_look = pygame.image.load("res/jail/zoom_diary.png")
        self.zoom_state = 0
        self.item_sdriver_state = 0
        self.next_room = 4
        
    def click_event(self, x, y):
        if self.look_state == 1:
            return
        
        if self.zoom_state == 0: #初期位置
            if (490 < x < 615) and (260 < y < 390):
                if self.lock_flag[4] == True:
                    self.zoom_state = 3
                else:
                    self.zoom_state = 1
            elif (703 < x < 829) and (578 < y < 612): #懐中電灯を入手
                self.item_sdriver_state = 1
                self.item_get[8] = True
                self.se[0].play()
                self.zoom_state = 2
            elif self.item_get[8] == True: #懐中電灯を取得していたら部屋画像を懐中電灯なしverにする
                self.zoom_state = 2
            elif (840 < x < 918) and (420 < y < 455): #ページ3を入手
                self.item_sdriver_state = 2
                self.item_get[9] = True
                self.se[0].play()
                if self.item_get[8] == False:
                    self.zoom_state = 0
                else:
                    self.zoom_state = 2
            elif (338 < x < 400) and (123 < y < 152):
                self.next_room = 2
            elif (566 < x < 602) and (190 < y < 226):
                self.next_room = 3  
            else:
                self.zoom_state = 0      
        elif self.zoom_state == 1: #扉拡大
            if self.lock_flag[4] == False:
                if self.item_use == [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]:
                    if (475 < x < 570) and (370 < y < 450):
                        self.lock_flag[4] = True
                        self.se[8].play()
                        self.item_use[1] = False
                        self.zoom_state = 3
            if not (170 < x < 850) and (0 < y < 640):
                if self.item_get[8] or self.item_get[14] == True:
                    self.zoom_state = 2
                else:
                    self.zoom_state = 0
        elif self.zoom_state == 2: #懐中電灯なしver
            if (490 < x < 615) and (260 < y < 390):
                if self.lock_flag[4] == True:
                    self.zoom_state = 3
                else:
                    self.zoom_state = 1    
            elif (840 < x < 918) and (420 < y < 455): #ページ3を入手
                self.item_sdriver_state = 2
                self.item_get[9] = True
                self.se[0].play()
                if self.item_get[8] or self.item_get[14] == True:
                    self.zoom_state = 2
                else:
                    self.zoom_state = 0
            elif (338 < x < 400) and (123 < y < 152):
                self.next_room = 2
            elif (566 < x < 602) and (190 < y < 226):
                self.next_room = 3       
            else:
                self.zoom_state = 2
        elif self.zoom_state == 3:
            if (490 < x < 615) and (260 < y < 390):
                self.next_room = 5
            if not (170 < x < 850) and (0 < y < 640):
                if self.item_get[8] == True:
                    self.zoom_state = 2
                else:
                    self.zoom_state = 0
        
    def draw(self):
        self.screen.blit(self.img_room1, (0,0)) #初期位置
        if self.zoom_state == 1:
           self.screen.blit(self.zoom_door, (0,0)) #扉画像
        elif self.zoom_state == 2:
            self.screen.blit(self.img_room2, (0,0)) #懐中電灯なしver
        elif self.zoom_state == 3:
            self.screen.blit(self.zoom_door2, (0,0)) #鍵なし扉

        if self.look_state == 1:
            self.screen.blit(self.img_look, (0, 0))     
            
    def next_state(self):
        next = self.next_room
        self.next_room = 4
        return next
    
    def next_music(self):
        return 4
    