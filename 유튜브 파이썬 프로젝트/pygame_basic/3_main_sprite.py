import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기 밑으로 가면 갈수록 올라감 음수 존재 x
screen = pygame.display.set_mode((screen_width, screen_height))  # 튜플 형식으로 해야함 화면크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/qmdl5/PycharmProjects/pythonProject/유튜브 파이썬 프로젝트/pygame_basic/background.png")
#탈출문자때문에 \ 를 \\ 또는 / 로 바꾸어줘야함#

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/qmdl5/PycharmProjects/pythonProject/유튜브 파이썬 프로젝트/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 새로크기
character_x_pos = (screen_width / 2) - (character_width/2)# 화면 가로의 절반 크기
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래


# 이벤트 루프(창을 꺼지지않기 위해 설정)
running = True  # 게임이 진행중인가
while running:
    for event in pygame.event.get():  # 사용자의 입력을 감지하는 코드
        if event.type == pygame.QUIT:  # 파이게임 창을 껐을때의 이벤트
            running = False  # 게임이 진행중이아님

    screen.blit(background, (0, 0))  # 백그라운드 파일, 좌표(x,y) #blit 은 실제로 그리는것

    screen.blit(character, (character_x_pos, character_y_pos))
    #기본적으로 그림은 오른쪽 밑으로 그려진다. 그렇기 때문에
    pygame.display.update()  # 게임화면을 다시 그리기(필수호출)

# pygame 종료
pygame.quit()

