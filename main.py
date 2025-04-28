"""
Tristan Newey
5/7/2025
This program is my final project.
"""

# initializing pygame
import random
import pygame
from pygame.constants import KEYDOWN
pygame.init()

# other variables
clicks = 0

# window dimensions
width = 750
height = 500
screen = pygame.display.set_mode(( width , height ))

# set window title
pygame.display.set_caption("game")

# fps
clock = pygame.time.Clock()
dt = 0
speed = 10

# positioning
button_pos = [ 50 , 50 ]

# sizing
button_size = [ 100 , 100 ]

"""game loop"""
running = True
while running:
  """ Handle events """
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == KEYDOWN:
      if event.key == pygame.K_ESCAPE: # escape key
          running = False
        
    if event.type == pygame.MOUSEBUTTONDOWN:
      if button.collidepoint( event.pos ):
        if clicks < 10:
          random_pos_0 = random.randint( 1 , 500 )
          random_pos_1 = random.randint( 1 , 500 )
          button_pos = [ random_pos_0 , random_pos_1 ]
          clicks = clicks + 1
          print(clicks)
        elif clicks >= 10 and clicks < 20:
          button_size = [ 50 , 50 ]
          random_pos_0 = random.randint( 1 , 500 )
          random_pos_1 = random.randint( 1 , 500 )
          button_pos = [ random_pos_0 , random_pos_1 ]
          clicks = clicks + 1
    

  """ draw to our screen """
  # clear screen
  screen.fill( "black" )

  """ draw game """
  
  button = pygame.draw.rect(screen, 
   "white", 
   pygame.Rect(( button_pos[0] , button_pos[1] ),( button_size[0] , button_size[1] ))
  )
  
  # update screen
  pygame.display.flip()

  #fps
  dt = clock.tick( speed ) / 1000
  
# quit pygame
pygame.quit()