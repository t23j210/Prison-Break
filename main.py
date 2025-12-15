# -*- coding: utf-8 -*-
"""
@author: Ozaki
"""

import pygame
import sys
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
    
    item_get = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    item_use = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    item_ctrl = Item_Base(screen, item_get, item_use, width, height)
    
    room_state = 0
    r_state = 0
    marge_state = 0
    next_room_state = 0
    alpha = 0
    room_ctrl = [Jail(screen, lock_flag, item_get, item_use),
                 Workshop(screen, lock_flag, item_get, item_use),
                 Kitchen(screen, lock_flag, item_get, item_use),
                 Storage_room(screen, lock_flag, item_get, item_use),
                 Underground_waterway(screen, lock_flag, item_get, item_use),
                 Ending(screen, lock_flag, item_get, item_use)]
    
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
                    next_room_state = (room_state - 1) % 6
                elif event.key == pygame.K_RIGHT:
                    next_room_state = (room_state + 1) % 6
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
                elif event.key == pygame.K_l:
                    r_state = 1
                elif event.key == pygame.K_m:
                    marge_state = 1
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
            if item_use == [False, False, False, False, True, False, True, False, False, False, False, True, False, False]:
                item_get[4] = False
                item_get[6] = False
                item_get[11] = False
                item_use[4] = False
                item_use[6] = False
                item_use[11] = False
                item_get[12] = True
                marge_state = 0
            elif item_use == [False, False, False, False, False, True, False, True, False, True, False, False, False, False]:
                item_get[5] = False
                item_get[7] = False
                item_get[9] = False
                item_use[5] = False
                item_use[7] = False
                item_use[9] = False
                item_get[2] = True
                marge_state = 0
            elif item_use == [False, False, True, False, False, False, False, False, False, False, True, False, False, False]:
                item_get[2] = False
                item_get[10] = False
                item_use[2] = False
                item_use[10] = False
                item_get[13] = True
                marge_state = 0


        if r_state == 1:
            if item_use == [False, False, False, True, False, False, False, False, False, False, False, False, False]:
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
        
        clock.tick(30)
        
        
if __name__ == '__main__':
    main()
