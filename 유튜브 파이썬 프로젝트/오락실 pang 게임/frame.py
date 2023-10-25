import pygame
import random
############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()  # 必須条件、リセット
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트,크기)
total_time = 99
start_ticks = pygame.time.get_ticks() # 현재 tick을 받아오기
# 화면 크기 설정
screen_width = 640  # 가로 크기　横のサイズ
screen_height = 480  # 세로 크기 밑으로 가면 갈수록 올라감 음수 존재 x　縦のサイズ
screen = pygame.display.set_mode((screen_width, screen_height))  #　画面のサイズ 튜플 형식으로 해야함 화면크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game")  # 名前　게임 이름

# FPS 값
clock = pygame.time.Clock()
############################################################
# 초 재기
start_ticks = pygame.time.get_ticks() # 현재 tick을 받아오기

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도 폰트 등)
#後ろ仮面
background = pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\background.png")
stage = pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\stage.png")
stage_size = stage.get_rect().size
#キャラ
character = pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\character.png")
character_size = character.get_rect().size
character_x_pos = (screen_width /2) - (character_size[0] /2)
character_y_pos = screen_height - character_size[1]
character_speed = 5
#무기
weapon = pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_speed =10
#여러발 가능
weapons =[]



#ball
ball_images=[
    pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\ball1.png"),
    pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\ball2.png"),
    pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\ball3.png"),
    pygame.image.load("C:\\Users\\qmdl5\\PycharmProjects\\pythonProject\\유튜브 파이썬 프로젝트\\오락실 pang 게임\\ball4.png")
    ]
#공크기에 따른 최초 스피드
ball_speed_y = [-18, -15 , -12, -9]
#공들
balls = []
#최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, #공 x
    "pos_y" : 50, #공 y
    "img_idx" :0,
    "to_x":3, #공 x 축 이동방향
    "to_y":-6, #공 y축 이동방향
    "init_spd_y": ball_speed_y[0] #y최초 속도
})
ball_speed_x = 15
w_to_y= 0
to_x = 0
character_speed = 0.6

running = True
while running:
    dt = clock.tick(30) #dt 델타 라고 함. 프레임 수를 설정



    # 2. 이벤트 처리 ( 키보드 , 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_size[0]/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
                #웨폰즈에 [[1,2]] 형태로 저장되니까
                #weapons = [[w[0],w[1]-weapon_speed] for w in weapons
                #하면 웨폰즈는 = [[1,2 - weapon_speed]]가되는겨
        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

        # if event.type == pygame.KEYDOWN:
        #     if event.type == pygame.K_SPACE:




    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_size[0]:
        character_x_pos=screen_width-character_size[0]

    #무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    #천장에 닿은 무기 없애기
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls): #balls 에 있는 몇번째 인덱스 값인지, 그 인덱스에 해당하는 값을 로드하는 것.
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_size()
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        #가로벽에 닿았을때 공 이동위치 변경
        if ball_pos_x < 0 or ball_pos_x  > screen_width- ball_pos_x:
            ball_val["to_x"] = ball_val["to_x"] * -1 #반대로 튀게 만드는 것이다.

        if ball_pos_y >= screen_height - stage_size[1]-ball_height:
            #스테이지에 튕겨서 올라가는 것
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5 #포물선을 그리는것이다. 속도를 조금씩 줄였다가 ( - 값에서 0 으로 , 0에서 -로 점점 빠르게내려오면서 가속도가 붙는거임

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos  # 실시간 캐릭터 위치를 업데이트하기위한 것
    character_rect.top = character_y_pos

    weapon_rect = weapon.get_rect()

    # 5. 화면에 그리기

    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:  # 스페이스바를 눌러서 저장한 위치를 웨폰에 저장
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))  # 그걸 blit 하는 것

    for idx, val in enumerate(balls):
        ball_pos_x=val["pos_x"]
        ball_pos_y=val["pos_y"]
        ball_img_idx=val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))
    screen.blit(stage, (0, screen_height - stage_size[1]))
    screen.blit(character, (character_x_pos, character_y_pos-stage_size[1]))






    pygame.display.update()
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과 시간(ms)를 초(s)로 환산
    # render(출력할 글자, True, 글자 색상)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
# pygame 종료
pygame.quit()

