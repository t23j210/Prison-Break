# -*- coding: utf-8 -*-
"""
@author: Ozaki
"""

import pygame
import sys
from start import Start
from jail import Jail
from workshop import Workshop
from kitchen import Kitchen
from storage_room import Storage_room
from underground_waterway import Underground_waterway
from ending import Ending
from item_base import Item_Base

def main():
    width = 1024
    height = 768
    pygame.init()
    screen = pygame.display.set_mode((width+80,768))
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    clock = pygame.time.Clock()
    
    lock_flag = [False, False, False, False, False, False, False]
    
    item_get = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    item_use = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    item_ctrl = Item_Base(screen, item_get, item_use, width, height)
    
    room_state = 0
    r_state = 0
    marge_state = 0
    next_room_state = 0
    alpha = 0

    pygame.mixer.init(frequency = 44100)
    music = ["res/music/music0.mp3",
             "res/music/music1.mp3",
             "res/music/music2.mp3",
             "res/music/music3.mp3",
             "res/music/music4.mp3",
             "res/music/music5.mp3",
             "res/music/music6.mp3"]
    music_state = -1
    next_music_state = 0

    se = []
    se.append(pygame.mixer.Sound("res/se/se0.mp3"))
    se.append(pygame.mixer.Sound("res/se/se1.mp3"))
    se.append(pygame.mixer.Sound("res/se/se2.mp3"))
    se.append(pygame.mixer.Sound("res/se/se3.mp3"))
    se.append(pygame.mixer.Sound("res/se/se4.mp3"))
    se.append(pygame.mixer.Sound("res/se/se5.mp3"))
    se.append(pygame.mixer.Sound("res/se/se6.mp3"))
    se.append(pygame.mixer.Sound("res/se/se7.mp3"))
    se.append(pygame.mixer.Sound("res/se/se8.mp3"))
    se[0].set_volume(0.2)
    se[0].set_volume(0.2)
    se[1].set_volume(0.2)
    se[2].set_volume(0.2)
    se[3].set_volume(0.2)
    se[4].set_volume(0.2)
    se[5].set_volume(0.2)
    se[6].set_volume(0.3)
    se[7].set_volume(0.3)
    se[8].set_volume(0.3)


    room_ctrl = [Start(screen, lock_flag, item_get, item_use, se),
                 Jail(screen, lock_flag, item_get, item_use, se),
                 Workshop(screen, lock_flag, item_get, item_use, se),
                 Kitchen(screen, lock_flag, item_get, item_use, se),
                 Storage_room(screen, lock_flag, item_get, item_use, se),
                 Underground_waterway(screen, lock_flag, item_get, item_use, se),
                 Ending(screen, lock_flag, item_get, item_use, se)]
    
    while True:

        """ マウスカーソル位置 """
        x, y = pygame.mouse.get_pos()
        room_ctrl[room_state].pos_event(x, y)
        
        """ クリックイベント，キーイベント """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if x < width:
                    room_ctrl[room_state].click_event(x, y)
                else:
                    item_ctrl.click_event(int(y/80))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    next_room_state = (room_state - 1) % 7
                elif event.key == pygame.K_RIGHT:
                    next_room_state = (room_state + 1) % 7
                elif event.key == pygame.K_a:
                    lock_flag[0] = not lock_flag[0]
                elif event.key == pygame.K_b:
                    lock_flag[1] = not lock_flag[1]
                elif event.key == pygame.K_c:
                    lock_flag[2] = not lock_flag[2]
                elif event.key == pygame.K_d:
                    lock_flag[3] = not lock_flag[3]
                elif event.key == pygame.K_e:
                    lock_flag[4] = not lock_flag[4]
                elif event.key == pygame.K_f:
                    lock_flag[5] = not lock_flag[5]
                elif event.key == pygame.K_g:
                    lock_flag[6] = not lock_flag[6]
                elif event.key == pygame.K_0:
                    item_get[0] = not item_get[0]
                    item_use[0] = False
                elif event.key == pygame.K_1:
                    item_get[1] = not item_get[1]
                    item_use[1] = False
                elif event.key == pygame.K_2:
                    item_get[2] = not item_get[2]
                    item_use[2] = False
                elif event.key == pygame.K_3:
                    item_get[3] = not item_get[3]
                    item_use[3] = False
                elif event.key == pygame.K_4:
                    item_get[4] = not item_get[4]
                    item_use[4] = False
                elif event.key == pygame.K_5:
                    item_get[5] = not item_get[5]
                    item_use[5] = False
                elif event.key == pygame.K_6:
                    item_get[6] = not item_get[6]
                    item_use[6] = False
                elif event.key == pygame.K_7:
                    item_get[7] = not item_get[7]
                    item_use[7] = False
                elif event.key == pygame.K_8:
                    item_get[8] = not item_get[8]
                    item_use[8] = False
                elif event.key == pygame.K_9:
                    item_get[9] = not item_get[9]
                    item_use[9] = False
                elif event.key == pygame.K_h:
                    item_get[10] = not item_get[10]
                    item_use[10] = False
                elif event.key == pygame.K_i:
                    item_get[11] = not item_get[11]
                    item_use[11] = False
                elif event.key == pygame.K_j:
                    item_get[12] = not item_get[12]
                    item_use[12] = False
                elif event.key == pygame.K_k:
                    item_get[13] = not item_get[13]
                    item_use[13] = False
                elif event.key == pygame.K_n:
                    item_get[14] = not item_get[14]
                    item_use[14] = False
                elif event.key == pygame.K_l:
                    r_state = 1
                elif event.key == pygame.K_m:
                    marge_state = 1
                elif event.key == pygame.K_v:
                    if item_get[0] == True and item_use[0] == True and sum(item_use) == 1:
                        if room_ctrl[room_state].look_state == 0:
                            room_ctrl[room_state].look_state = 1
                        elif room_ctrl[room_state].look_state == 1:
                            room_ctrl[room_state].look_state = 0
                            item_use[0] = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        """ 処理 """
        if alpha == 240:
            offset = -20
            room_state = next_room_state
        elif room_state != next_room_state:
            offset = 20
        elif alpha == 0:
            offset = 0
            
        if marge_state == 1:
            if item_use == [False, False, False, False, True, False, True, False, False, False, False, True, False, False, False]: #ドリル
                item_get[4] = False
                item_get[11] = False
                item_use[4] = False
                item_use[6] = False
                item_use[11] = False
                item_get[12] = True
                marge_state = 0
            elif item_use == [False, False, False, False, False, True, False, True, False, True, False, False, False, False, False]: #ページ合成
                item_get[5] = False
                item_get[7] = False
                item_get[9] = False
                item_use[5] = False
                item_use[7] = False
                item_use[9] = False
                item_get[2] = True
                marge_state = 0
            elif item_use == [False, False, True, False, False, False, False, False, False, False, True, False, False, False, False]: #暗証番号
                item_get[2] = False
                item_get[10] = False
                item_use[2] = False
                item_use[10] = False
                item_get[13] = True
                marge_state = 0
            elif item_use == [False, False, False, False, False, False, True, False, True, False, False, False, False, False, False]: #懐中電灯
                item_get[6] = False
                item_get[8] = False
                item_use[6] = False
                item_use[8] = False
                item_get[14] = True
                marge_state = 0


        if r_state == 1:
            if room_state == 2:
                if item_use == [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False]:
                    room_state = 3
                    item_use[3] = False
                    r_state = 0
            elif room_state == 3:
                if item_use == [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False]:
                    room_state = 2
                    item_use[3] = False
                    r_state = 0


        room_ctrl[room_state].do()
        item_ctrl.do()
        
        """ 描画 """
        screen.fill((0,0,0))
        room_ctrl[room_state].draw()
        if offset != 0:
            alpha += offset
            surface.fill((0, 0, 0, alpha))
            screen.blit(surface, (0, 0))
        item_ctrl.draw()
        pygame.display.update()
        
        """部屋移動"""
        if offset == 0:
            next_room_state = room_ctrl[room_state].next_state()

        """曲変更"""
        next_music_state = room_ctrl[room_state].next_music()
        if music_state != next_music_state:
            pygame.mixer.music.load(music[next_music_state])
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
            music_state = next_music_state    
        
        clock.tick(30)
        
        
if __name__ == '__main__':
    main()
