import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) #튜플 형식으로 해야함 화면크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/qmdl5/PycharmProjects/pythonProject/유튜브 파이썬 프로젝트/pygame_basic/background.png")
# 탈출문자때문에 \ 를 \\ 또는 / 로 바꾸어줘야함

# 이벤트 루프(창을 꺼지지않기 위해 설정)
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #사용자의 입력을 감지하는 코드
        if event.type == pygame.QUIT: #파이게임 창을 껐을때의 이벤트
            running = False #게임이 진행중이아님

    # screen.fill((0,0,255)) #rgb 값을 채워넣는것
    screen.blit(background, (0, 0))  # 백그라운드 파일, 좌표(x,y) #blit 은 실제로 그리는것
    #매 프레임마다 디스플레이를 그려야함
    pygame.display.update() #게임화면을 다시 그리기(필수호출)

# pygame 종료
pygame.quit()