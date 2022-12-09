import pygame
from sympy import fps

pygame.init() #초기화

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Practice")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\82104\\PythonWorkspace\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\82104\\PythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반크기에 해당하는곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아해에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인가?

while running:
  dt = clock.tick(60) #화면의 초당 프레임수 설정
  
  print(f"fps : {str(clock.get_fps())}")
  # eg. 캐릭터가 1초동안 100 이동해야한다
  #   10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동! 10 * 10= 100
  #   20 fps : 1초 동안에 20번 동작 -> 1번에 20만큼 이동! 20 * 5 = 100



  for event in pygame.event.get(): # 어떤이벤트가 발생하엿는가
    if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하엿는가?
      running = False # 게임진행중아님

    if event.type == pygame.KEYDOWN: # 키가 눌러졋는지 확인
      if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽
        to_x -= character_speed
      elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽
        to_x += character_speed
      elif event.key == pygame.K_UP: # 캐릭터를 위
        to_y -= character_speed
      elif event.key == pygame.K_DOWN: # 캐릭터를 아래
        to_y += character_speed

    if event.type == pygame.KEYUP: # 방향키 뗴면 멈춤
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
        to_y = 0

  character_x_pos += to_x * dt
  character_y_pos += to_y * dt 

  # 가로 경계값 처리
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
    character_x_pos = screen_width - character_width

  # 세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height

  # screen.fill((0, 0, 255))  rgb
  screen.blit(background, (0, 0)) # 배경그리기

  screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

  pygame.display.update() # 게임화면 다시그리기


# 게임종료
pygame.quit()