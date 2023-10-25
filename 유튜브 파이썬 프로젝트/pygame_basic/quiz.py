import pygame
import random
############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()  # 必須条件、リセット

# 화면 크기 설정
screen_width = 480  # 가로 크기　横のサイズ
screen_height = 640  # 세로 크기 밑으로 가면 갈수록 올라감 음수 존재 x　縦のサイズ
screen = pygame.display.set_mode((screen_width, screen_height))  #　画面のサイズ 튜플 형식으로 해야함 화면크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Avoid Miku")  # 名前　게임 이름

# FPS 값
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도 폰트 등)
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트,크기)

background = pygame.image.load("C:/Users/qmdl5/PycharmProjects/pythonProject/유튜브 파이썬 프로젝트/pygame_basic/background.png")
character = pygame.image.load("C:/Users/qmdl5/PycharmProjects/pythonProject/유튜브 파이썬 프로젝트/pygame_basic/character.png")
enemy = pygame.image.load("C:/Users/qmdl5/PycharmProjects/pythonProject/유튜브 파이썬 프로젝트/pygame_basic/enemy.png")

character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x = (screen_width / 2) - (character_width/2) # 중간 시작
character_y = screen_height - character_height
character_speed = 0.6

c_x = 0
c_y = 0

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = 0
enemy_y = 0

running = True
while running:
    dt = clock.tick(30) #dt 델타 라고 함. 프레임 수를 설정
    for event in pygame.event.get():  # 사용자의 입력을 감지하는 코드
        if event.type == pygame.QUIT:  # 파이게임 창을 껐을때의 이벤트
            running = False  # 게임이 진행중이아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                c_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                c_x += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                c_x = 0
    enemy_y += random.randint(20,30)
    if enemy_y > screen_height - enemy_height/2:
        enemy_y = 0
        enemy_x = random.randint(0,screen_width-enemy_width)


    character_x += c_x * dt  # 이동속도를 고정시키는 방법임. 좌표에 fps 을 곱하는거임



    # 3. 게임 캐릭터 위치 정의
    character_x += c_x *dt

    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_width:
        character_x = screen_width - character_width

    character_rect = character.get_rect()
    character_rect.left = character_x # 실시간 캐릭터 위치를 업데이트하기위한 것
    character_rect.top = character_y





    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x
    enemy_rect.top = enemy_y
    # 4. 충돌처리
    if character_rect.colliderect(enemy_rect):  # 사격형 기준으로 ()안의 것과 충돌이 있었는지 함수
        print("충돌했어요")
        running = False
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))  # 백그라운드 파일, 좌표(x,y) #blit 은 실제로 그리는것
    screen.blit(character, (character_x, character_y))  # 기본적으로 그림은 오른쪽 밑으로 그려진다. 그렇기 때문에
    screen.blit(enemy, (enemy_x, enemy_y))  # 적그리기
    # 필수호출
    pygame.display.update()

# pygame 종료
pygame.quit()



