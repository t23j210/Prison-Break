import pygame

class PasslockControl:
    def __init__(self, screen, lock_flag, se):
        self.lock_flag = lock_flag
        self.screen = screen
        self.se = se
        self.font = pygame.font.SysFont(None, 70)
        self.password = [0, 0, 0, 0]
        self.index = 0
        
    def onclick(self, x, y):
        if (581 < x < 625) and (572 < y < 615):
            self.push_number(0)
        elif (451 < x < 498) and (386 < y < 430):
            self.push_number(1)
        elif (515 < x < 561) and (386 < y < 430):
            self.push_number(2)
        elif (581 < x < 625) and (386 < y < 430):
            self.push_number(3)
        elif (451 < x < 498) and (448 < y < 490):
            self.push_number(4)
        elif (515 < x < 561) and (448 < y < 490):
            self.push_number(5)
        elif (581 < x < 625) and (448 < y < 490):
            self.push_number(6)
        elif (451 < x < 498) and (510 < y < 554):
            self.push_number(7)
        elif (515 < x < 561) and (510 < y < 554):
            self.push_number(8)
        elif (581 < x < 625) and (510 < y < 554):
            self.push_number(9)
        elif (515 < x < 572) and (572 < y < 615):
            self.reset_password()
        elif (451 < x < 498) and (572 < y < 615):
            self.unlock()
        
    def push_number(self, num):
        self.se[6].play()
        self.password[self.index] = num
        self.index = ( self.index + 1) % 4
        if self.index == 0:
            self.unlock()
        
    def reset_password(self):
        self.password = [0, 0, 0, 0]

    def unlock(self):
        if self.password == [4, 8, 1, 8]:
            self.se[7].play()
            self.lock_flag[6] = True
        else:
            self.reset_password()
            self.se[5].play()


    def disp_password(self):
        text = "{:d} {:d} {:d} {:d}".format(self.password[0], self.password[1], self.password[2], self.password[3])
        code = self.font.render(text, True, (255 , 255, 255))
        self.screen.blit(code, [446, 191]) 

