import pygame, sys
from pygame.locals import *

#pygame 초기화
pygame.init()

#창 크기 설정
screen_width = 1200
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))


#창 설정
display_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bubble Bobble")


#주인공 객체 생성
player = pygame.Rect((screen_width-75)/22.5, screen_height-150, 75, 75)
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img, (75,75))        


#게임 속도 조절
clock = pygame.time.Clock()
game_speed = 0.4

#점프를 위한 중력
y_vel = 0

#게임이 실행중일때
play = True
while play:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            sys.exit()

    screen.fill((0, 0, 0))

    keyInput = pygame.key.get_pressed()
    if keyInput[K_LEFT] and player.left >=0:
        player.left -= game_speed * dt
    if keyInput[K_RIGHT] and player.right <= screen_width:
        player.right += game_speed * dt
    
    #중력 엔진 만들기
    player.top += y_vel
    y_vel +=1

    if player.bottom >= 675:
        y_vel = 0
        if keyInput[K_UP]:
            y_vel = -15

    screen.blit(player_img, player)

    

    pygame.display.update()



pygame.quit()