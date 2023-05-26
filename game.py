import pygame


pygame.init()

ticker = pygame.time.Clock()
width = 700
height = 600
window = pygame.display.set_mode((width,height))


groundHitboxes = [(pygame.Rect(0,400,width,5))]

class Player:
    def __init__(self,type,up,down,left,right):
        self.upkey = up
        self.downkey = down
        self.leftkey = left
        self.rightkey = right
        self.type = type
        self.x = 20
        self.y = -4
        self.len = 10
        self.wid = 30
        self.vely = 0
        self.velx = 0
        self.dir = "left"
        self.resistSpeed = 1
        self.maxXSpeed = 10
        

        self.maxYSpeed = 20
        self.jump = False
        self.grav = 2.5
        self.grounded = False
        self.jumpTimer = 0
        self.hitbox = pygame.Rect(self.x,self.y,self.len,self.wid)


    def printThem(self):
        if self.velx > 0:
            self.dir = "right"
        if self.velx < 0:
            self.dir = "left"
        if self.velx == 0:
            self.dir = "stopped"
        
        #JUMPING
        if pygame.key.get_pressed()[self.upkey]:# and self.grounded
            if self.jumpTimer == 0:
                self.vely = -5
            if self.jumpTimer < 10:
                self.jump = True
                self.jumpTimer += 1
        else:
            if not self.grounded:
                self.jumpTimer = 10
        if self.jump:
            self.vely -= 1
            self.jump = False
        #falling script
        elif (self.vely < self.maxYSpeed) and (not self.grounded) and (not self.jump):
            self.vely += (self.grav/2) * 1.03
            if self.vely > self.maxYSpeed:
                self.vely = self.maxYSpeed
        self.y += self.vely
        if self.y >= 400 and (not self.jump):
            self.y = 400
            self.vely = 0
            self.grounded = True
            self.jumpTimer = 0
        else:
            self.grounded = False

        

       
        
        
        


            
        if pygame.key.get_pressed()[self.downkey]:
            print("down")





        #RIGHT
        if pygame.key.get_pressed()[self.rightkey] and not pygame.key.get_pressed()[self.leftkey]:
            if self.velx < self.maxXSpeed:
                self.temp = 0
                self.temp += 0.5
                self.temp **= 1.03
                self.velx += self.temp
                if self.velx < 0:
                    self.velx += 0.5
            elif self.velx > self.maxXSpeed:
                self.velx = self.maxXSpeed

        #LEFT
        elif pygame.key.get_pressed()[self.leftkey] and not pygame.key.get_pressed()[self.rightkey]:
            if self.velx > -self.maxXSpeed:
                self.temp = 0
                self.temp += 0.5
                self.temp **= 1.03
                self.temp *= -1
                self.velx += self.temp
                if self.velx > 0:
                    self.velx -= 0.5
            elif self.velx < self.maxXSpeed:
                self.velx = -self.maxXSpeed

        #Ground and Drag
        elif (pygame.key.get_pressed()[self.leftkey] and pygame.key.get_pressed()[self.rightkey]) or not (pygame.key.get_pressed()[self.leftkey] and pygame.key.get_pressed()[self.rightkey]):
            if self.velx > 0:
                if self.grounded:
                    self.velx -= 1
                if not self.grounded:
                    self.velx -= 0.2
                if self.velx <= 0:
                    self.velx = 0
            if self.velx < 0:
                if self.grounded:
                    self.velx += 1
                if not self.grounded:
                    self.velx += 0.2
                if self.velx >= 0:
                    self.velx = 0
        
                
        self.vely = round(self.vely,2)
        self.velx = round(self.velx,2)
        
        self.x += self.velx
        #print(self.vely, self.y,self.grav)
        pygame.draw.rect(window,(255,255,255), pygame.Rect(self.x,self.y-30,self.len,self.wid))
        self.hitbox = pygame.Rect(self.x,self.y-30,self.len,self.wid)
        pygame.draw.rect(window,(255,0,0), self.hitbox, 1)
        

players = []
playerCount = 1
for i in range (playerCount):
    if i == 0:
        players.append(Player(1,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT))
    if i == 1:
        players.append(Player(2,pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d))
    if i == 2:
        players.append(Player(3,pygame.K_y,pygame.K_h,pygame.K_g,pygame.K_j))
    if i == 3:
        players.append(Player(4,pygame.K_p,pygame.K_SEMICOLON,pygame.K_l,pygame.K_QUOTE))

while True:
    window.fill(0)
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
        break
    for i in range(playerCount):
        players[i].printThem()


    pygame.draw.rect(window, (255,0,0), groundHitboxes[0], 1)


    pygame.display.flip()
    ticker.tick(60)


pygame.quit()
