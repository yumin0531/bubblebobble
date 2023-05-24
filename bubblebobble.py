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
player_rect = pygame.Rect((screen_width-75)/22.5, screen_height-150, 75, 75)

walkRight = pygame.image.load('playerright.png')
walkRight = pygame.transform.scale(walkRight, (75,75))   
walkLeft = pygame.image.load('playerleft.png')
walkLeft = pygame.transform.scale(walkLeft, (75,75))
openmouthRight = pygame.image.load('playermouthright.png')
openmouthRight = pygame.transform.scale(openmouthRight, (75,75))
openmouthLeft = pygame.image.load('playermouthleft.png')
openmouthLeft = pygame.transform.scale(openmouthLeft, (75,75))  

player_sheet = pygame.transform.scale(pygame.image.load('player.png'), (273 * 4, 140 * 4))
player_sheet_flipped = pygame.transform.flip(player_sheet, True, False)

left = False
right = False

#게임 속도 조절
clock = pygame.time.Clock()
game_speed = 0.4

#점프를 위한 중력
y_vel = 0

def scale_rect(rect):
    x, y, w, h = rect
    return Rect(x * 4, y * 4, w * 4, h * 4)

def flip_rectangle_horizontally(rect, sheet_size):
    x, y, w, h = rect
    return Rect(sheet_size[0] - x - w, y, w, h)

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
    if keyInput[K_LEFT] and player_rect.left >=0:
        player_rect.left -= game_speed * dt
        left = True
        right = False
    if keyInput[K_RIGHT] and player_rect.right <= screen_width:
        player_rect.right += game_speed * dt
        left = False
        right = True

    if right:
        if keyInput[K_SPACE]:
            screen.blit(player_sheet, player_rect, scale_rect(Rect(2, 70, 16, 16)))
        else:
            screen.blit(player_sheet, player_rect, scale_rect(Rect(2, 35, 16, 16)))
    elif left:
        if keyInput[K_SPACE]:
            screen.blit(player_sheet_flipped, player_rect, flip_rectangle_horizontally(scale_rect(Rect(2, 70, 16, 16)), (273 * 4, 140 * 4)))
        else:
            screen.blit(player_sheet_flipped, player_rect, flip_rectangle_horizontally(scale_rect(Rect(2, 35, 16, 16)), (273 * 4, 140 * 4)))
    else:
        screen.blit(player_sheet, player_rect, scale_rect(Rect(2, 35, 16, 16)))
    
    
    #중력 엔진 만들기
    player_rect.top += y_vel
    y_vel +=1

    if player_rect.bottom >= 675:
        y_vel = 0
        if keyInput[K_UP]:
            y_vel = -15


    pygame.display.update()


pygame.quit()