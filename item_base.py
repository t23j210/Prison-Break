# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:18:34 2020

@author: rufiy
"""

import pygame

class Item_Base:
    def __init__(self, screen, item_get, item_use, w, h):
        self.img_item = [pygame.image.load("res/jail/item_diary.png"), #日記
                         pygame.image.load("res/jail/item_key.png"), #鍵
                         pygame.image.load("res/jail/item_page.png"), #ページ
                         pygame.image.load("res/workshop/item_map.png"), #マップ
                         pygame.image.load("res/workshop/item_no_needlever.png"), #ドリル
                         pygame.image.load("res/workshop/item_page1.png"), #ページ１
                         pygame.image.load("res/kitchen/item_battery.png"), #バッテリー
                         pygame.image.load("res/kitchen/item_page2.png"), #ページ２
                         pygame.image.load("res/storage_room/item_flashlight.png"), #懐中電灯
                         pygame.image.load("res/storage_room/item_page3.png"), #ページ３
                         pygame.image.load("res/underground_waterway/item_flame.png"), #フレーム
                         pygame.image.load("res/workshop/item_needle.png"),] #ニードル
        self.screen = screen
        self.item_get = item_get
        self.item_use = item_use
        self.w = w
        self.h = h
        self.cnt = 0
        self.target_face = 0
        self.img_target = pygame.image.load("res/common/target.png")
        """ アイテム画像を 64 x 64 に縮小 """
        for i, item in enumerate(self.img_item):
            self.img_item[i] = pygame.transform.scale(item, (64, 64))

    
    def click_event(self, id):
        idx_list = self.true_index(self.item_get)
        if id < len(idx_list):
            self.item_use[idx_list[id]] = not self.item_use[idx_list[id]]
    
    
    def do(self):
        self.cnt = (self.cnt + 1) % 24
        self.target_face = int(self.cnt / 3)
        

    def draw(self):
        for i, id in enumerate(self.true_index(self.item_get)):
            self.screen.blit(self.img_item[id], [self.w+8, 8 + 80*i])
            if self.item_use[id] == True:
                self.screen.blit(self.img_target, [self.w+4, 4 + 80*i],
                                 area=[72*self.target_face, 0, 72, 72])
    
    
    def true_index(self, lst):
        return [i for i, x in enumerate(lst) if x == True]