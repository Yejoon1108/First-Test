import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) #튜플 형식으로 해야함 화면크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 이벤트 루프(창을 꺼지지않기 위해 설정)
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #사용자의 입력을 감지하는 코드
        if event.type == pygame.QUIT: #파이게임 창을 껐을때의 이벤트
            running = False

# pygame 종료
pygame.quit()