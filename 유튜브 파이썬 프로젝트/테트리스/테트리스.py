import pygame
############################################################
# 기본 초기화 (반드시 해야하는 것들)
pygame.init()  # 必須条件、リセット

# 화면 크기 설정
screen_width = 480  # 가로 크기　横のサイズ
screen_height = 640  # 세로 크기 밑으로 가면 갈수록 올라감 음수 존재 x　縦のサイズ
screen = pygame.display.set_mode((screen_width, screen_height))  #　画面のサイズ 튜플 형식으로 해야함 화면크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("tetris")  # 名前　게임 이름

# FPS 값
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도 폰트 등)

running = True
while running:
    dt = clock.tick(30) #dt 델타 라고 함. 프레임 수를 설정


    # 2. 이벤트 처리 ( 키보드 , 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌처리

    # 5. 화면에 그리기

    pygame.display.update()

# pygame 종료
pygame.quit()

