import pygame
import random
from pygame.locals import *



record_list=[]

# start program
pygame.init()




def gioco():
    global points
    # create screen
    width=800
    height=600
    screen=pygame.display.set_mode((width,height))

    # update screen
    pygame.display.update()

    # load image background
    background=pygame.image.load('sfondo4.png')
    b1=0
    b2=0

    # load image terrain
    terrain=pygame.image.load('terreno5.png')
    t1=0
    t2=510

    # load player image
    player=pygame.image.load('uccello4.png')
    p1 = 200
    p2 = 350


    # load text game over
    game_over=pygame.image.load('game.png')
    g1=7
    g2=1

    # load tube image
    tube=pygame.image.load('tubo.png')
    tb1=800
    tb2=random.randint(300,400)

    tube2=pygame.image.load('tubo.png')
    tuber=pygame.transform.flip(tube2,False,True)
    
    tb3=1200
    tb4=random.randint(-200,0)
    
    # load text points
    font = pygame.font.SysFont("Arial Black",30)

    # load points
    font3=pygame.font.SysFont("Arial",20)

    # load record points
    font4=pygame.font.SysFont("Arial",20)

    # create record 
    record_list.append(points)
    record=record_list.copy()
    for i in record_list:
        for x in record:
            if i>x:
                record=[i]
    record_=font4.render(f'RECORD:{record}',True,(0,0,0))
    
    
# start game
    points=0
    game=True
    while game:
        points+=11
        txtpoint=font3.render('POINTS: {}'.format(points),True,(0,0,0))
    # management event input
        for event in pygame.event.get():
            # exit event
            if event.type == pygame.QUIT:
                game=False
                quit()
            # keydown event
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.locals.K_UP:
                    p2-=50
                

    # print image in screen

        # print and animation background
        screen.blit(background,(b1,b2))
        b1-=2
        if b1 == -800:
            b1=0


        # print and animation tube
        screen.blit(tube,(tb1,tb2))
        screen.blit(tuber,(tb3,tb4))
        tb1-=50
        tb3-=50
        if tb1==0:
            tb1+=800
            tb2=random.randint(300,350)
        elif tb3==0:
            tb3+=800
            tb4=random.randint(-250,0)
        
        elif tb1 == p1:
            if p2 >= tb2:
                punti.append(points)
                game=False
        elif tb3 == p1:
            if p2 <= tb4+300:
                punti.append(points)
                break
            
        
        # print and animation terrain 
        screen.blit(terrain,(t1,t2))
        t1-=20
        if t1 ==-60:
            t1+=60
    

        # print player in screen
        screen.blit(player,(p1,p2))
        p2+=7
        if p2 == 480:
            screen.blit(game_over,(g1,g2))
            screen.blit(text,(tx1,tx2))
            pygame.display.update()
            punti.append(points)
            game=False


        # print points
        screen.blit(txtpoint,(675,0))

        # print record
        screen.blit(record_,(1,1))


        pygame.display.update()
        pygame.time.delay(50)


points=0
punti=[]
gioco()


def lose():
    global punti
    # create screen
    width=800
    height=600
    screen=pygame.display.set_mode((width,height))

    # update screen
    pygame.display.update()

    # load image background
    background=pygame.image.load('sfondo4.png')
    b1=0
    b2=0

    # load image terrain
    terrain=pygame.image.load('terreno5.png')
    t1=0
    t2=510

    # load player image
    player=pygame.image.load('uccello4.png')
    p1 = 200
    p2 = 350


    # load text game over
    game_over=pygame.image.load('game.png')
    g1=7
    g2=1

    # load tube image
    tube=pygame.image.load('tubo.png')
    tb1=800
    tb2=random.randint(300,400)
    name=True

    # load text continue
    font2=pygame.font.SysFont("Arial Black",20)

    # load textpoints
    font=pygame.font.SysFont("Arial",40)

    # load record points
    font4=pygame.font.SysFont("Arial",20)

    # create record 
    record_list.append(points)
    record=record_list.copy()
    for i in record_list:
        for x in record:
            if i>x:
                record=[i]
        record_=font4.render(f'RECORD: {record}',True,(0,0,0))
        screen.blit(record_,(30,30))

    
    while name:
        pointtext=font.render('YOUR SCORE IS: {}'.format(punti),True,(0,0,100))
        continue_=font2.render('PRESS SPACE BUTTON TO CONTINUE',True,(0,0,0))


        screen.blit(background,(b1,b2))
        b1-=2
        if b1 == -800:
            b1=0
        screen.blit(continue_,(200,350)) 
        screen.blit(terrain,(t1,t2))
        t1-=20
        if t1 ==-60:
            t1 += 60
        screen.blit(record_, (15,1))
        screen.blit(game_over,(g1,g2))
        screen.blit(pointtext,(200,300))
        pygame.display.update()
        

        # management extern event

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                name=False
                

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    name=False

lose()

def return_game():
    global p1,p2
    while 1:
        punti.clear()
        gioco()
        lose()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
pygame.display.update()
    
return_game()
quit()
