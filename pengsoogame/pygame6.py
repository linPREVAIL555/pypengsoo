import pygame
import time

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption(";)")

color1 = 0
color2 = 0
color3 = 255

health1 = 200
health2 = 200
ult = 0
x = 50
ax = 400
y = 50
ay = 400
width = 50
height = 50
vel1 = 10
vel2 = 10
a1 = 5
a2 = 5
exp = 0

healmode = 1

music = pygame.mixer.music.load('pengsoosong.mp3')
pygame.mixer.music.play(-1)

pengsoo = pygame.image.load('standing.png')





run = True

while run:
    hitbox1 = (x + 25, x + 25, 50, 50)
    hitbox2 = (ax + 25, x + 25, 50, 50)
    hitbox3 = (x + 25, 0, 5, 500)
    hitbox4 = (0, ay + 25, 500, 5)
   # if ult == 1:
  #      hitbox4 = (0, ay , 500, 50)
  #  if secondline == 1:
   #     hitbox5 = (ax + 25, 0, 5, 500)
    

    
    pygame.time.delay(10)
    if ax > x-150 and ax < x + 150 and ay > y - 150 and ay < y +150  and exp == 1:
        print ("HitHard")
        health1 -= 30
        exp = 0
    else:
        exp = 0

    if x == ax and ult == 0:
        print("hit")
       # pygame.time.delay(200)
        health1 -= a2
        #health2 += 2
    if y == ay and ult == 1:
        #pygame.time.delay(200)
        health2 -= 40
        ult = 0
        vel2 = 20
        a2 = 5
        print("hit")
    if y == ay:
        print("hit1")
        #pygame.time.delay(200)
        health2 -= a2
        #health1 += 2
    if health1 < 0 or health2 < 0:
        run = False


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= vel1
        
    if keys[pygame.K_d] and x < 450:
        x += vel1
    if keys[pygame.K_w] and y > 0:
        y -= vel1
    if keys[pygame.K_s] and y < 450:
        y += vel1
    if keys[pygame.K_UP] and ay > 0:
        ay -= vel2
    if keys[pygame.K_DOWN] and ay < 450:
        ay += vel2
    if keys[pygame.K_LEFT] and ax > 0:
        ax -= vel2
    if keys[pygame.K_RIGHT] and ax < 450:
        ax += vel2
    if keys[pygame.K_z]:
        color3 = 0
        health2 -= 1
    #    a2 = 0
        
       # health2 = health2 - 50
    if keys[pygame.K_q] and color3 == 0:
        color3 = 255
        exp = 1
        #pygame.draw.circle(win, (0,0,255), (255,255), 25)
        #pygame.time.delay(100)

    if keys[pygame.K_o]:
        ult = 1
        a2 = 40
        vel2 = 1
    #    health1 -= 5
    if keys[pygame.K_p]:
        a2 = 10
        healmode = 1
        if ult == 1:
            ult = 0
            vel2 = 10


    
    win.fill((0,0,0))
    #hitbox1 = (x + 25, x + 25, 50, 50)
    #hitbox2 = (ax + 25, x + 25, 50, 50)
    #hitbox3 = (x + 25, 0, 5, 500)
    #hitbox4 = (0, ay + 25, 500, 5)
    #pygame.draw.rect(win, (255,0,0), (10, 10, 200, 10))
    #pygame.draw.rect(win, (255,0,0), (290, 10, 200, 10))
    pygame.draw.rect(win, (color1, color2, color3), hitbox3)
    pygame.draw.rect(win, (255,0,0), hitbox4)
    if ult == 1:
        pygame.draw.rect(win, (255,255,255), (0,ay+20,500,15))
        pygame.draw.rect(win, (255,255,0), (0,ay+15,500,5    ))
        pygame.draw.rect(win, (255,255,0), (0,ay+30,500,5    ))
        pygame.draw.rect(win, (255,127,0), (0,ay+35,500,5))
        pygame.draw.rect(win, (255,127,0), (0,ay+10,500,5))
        pygame.draw.rect(win, (255,0,0), (0,ay+5,500,5))
        pygame.draw.rect(win, (255,0,0), (0,ay+40,500,5))



     #   pygame.draw.rect(win, (255,0,0), hitbox5)
    pygame.draw.rect(win, (color1,color2,color3), (x, y, width, height))


  #  if color3 != 0:
   #     win.blit(pengsoo, (x-10,y-10))

    pygame.draw.rect(win, (255,0,0), (ax, ay, width, height))

    #pygame.draw.rect(win, (0,255,0), (10, 10, health1, 10))
    
    pygame.draw.rect(win, (255,0,0), (10, 10, 200, 10))
 
    if health1 > 0:
        pygame.draw.rect(win, (0,255,0), (10, 10, health2, 10))
    #pygame.draw.rect(win, (0,255,0), (290, 10, health2, 10))

    pygame.draw.rect(win, (255,0,0), (290, 10, 200, 10))

    if health2 > 0:
        pygame.draw.rect(win, (0,255,0), (290, 10, health1, 10))
        


    if exp == 1:
        #pygame.draw.rect(win, (0,0,255), (x-125,y-125, 300, 300))
        #pygame.draw.rect(win, (150,150,255), (x-100, y-100, 250, 250))
        #pygame.draw.rect(win, (255,255,255), (x-50, y-50, 150, 150))

        pygame.draw.circle(win, (0,0,255), (x+25,y+25), (150))
        pygame.draw.circle(win, (150, 150, 255), (x +25,y+25), (125))
        pygame.draw.circle(win, (255, 255, 255), (x + 25, y +25), (75))
        win.blit(pengsoo, (x-10, y-10))
        #pygame.time.delay(100)


        #if ax >= x + 150
         #   print("BOOM")
    #    time.sleep(3)
   #     exp = 0


    pygame.display.update()
 #   time.sleep(0.03)

if health1 > health2:
    print("Player2, You win")
elif health1 == health2:
    print("Tie")
else:
    print("Player1, you win")

#print( "Player1, your score is:",health1)

#print("Player2, your score is:",health2)
#if health2 >= 0:
 #   win.fill((0,255,0))
#if health1 >= 0:
  #  win.fill((255,0,0))
pygame.display.update()
#pygame.time.delay(500)
pygame.quit()
