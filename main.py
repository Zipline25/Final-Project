"""
Tristan Newey
5/7/2025
This program is my final project.
"""

# initializing
import pygame
import random

pygame.init()
width, height = 600, 450
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Clone")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# images

ball_image = pygame.image.load('images/cat_face.jpg')

# paddle
paddle = pygame.Rect(width // 2 - 60, height - 30, 120, 10)

# ball
ball = pygame.Rect(width // 2 - 10, height // 2, 20, 20)
ball_speed = [4, -4]

# game state
lives = 3
level = 1
running = True
game_over = False


# function to create bricks for a level
def create_bricks():
  bricks = []
  special_bricks_left = 0
  for row in range(5):
    for col in range(8):
      rect = pygame.Rect(col * (width // 8), row * 30 + 40, (width // 8) - 5,
                         30 - 5)
      if random.random(
      ) < 0.2 * level:  # Increase special brick chance with level
        brick_type = "special"
        special_bricks_left += 1
      else:
        brick_type = "normal"
      bricks.append({"rect": rect, "type": brick_type})
  return bricks, special_bricks_left


# start the game with level 1 bricks
bricks, special_bricks_left = create_bricks()

# game Loop
while running:
  screen.fill(black)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # input
  keys = pygame.key.get_pressed()
  if keys[pygame.K_ESCAPE]:
    running = False
  if keys[pygame.K_a] and paddle.left > 0:
    paddle.x -= 8
  if keys[pygame.K_d] and paddle.right < width:
    paddle.x += 8

  if not game_over:
    # move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # wall collisions
    if ball.left <= 0 or ball.right >= width:
      ball_speed[0] *= -1
    if ball.top <= 0:
      ball_speed[1] *= -1

    # bottom collision = lose life or game over
    if ball.bottom >= height:
      lives -= 1
      if lives > 0:
        # reset ball and paddle
        ball.x, ball.y = width // 2 - 10, height // 2
        ball_speed = [4 * random.choice([-1, 1]), -4]
        paddle.x = width // 2 - 60
        pygame.time.wait(1000)
      else:
        game_over = True

    # paddle collision
    if ball.colliderect(paddle):
      ball_speed[1] *= -1

    # brick collisions
    for brick_index, brick in enumerate(bricks):
      if ball.colliderect(brick["rect"]):
        ball_speed[1] *= -1
        # check if special brick is hit
        if brick["type"] == "special":
          special_bricks_left -= 1
        del bricks[brick_index]
        break

    # if all special bricks are hit, go to the next level
    if special_bricks_left == 0:
      level += 1
      bricks, special_bricks_left = create_bricks()  # Create new level bricks

  # draw everything
  pygame.draw.rect(screen, blue, paddle)
  pygame.draw.ellipse(screen, white, ball)

  for brick in bricks:
    if brick["type"] == "special":
      pygame.draw.rect(screen, red, brick["rect"])
    else:
      pygame.draw.rect(screen, green, brick["rect"])

  # draw lives and level info
  lives_text = font.render(f"Lives: {lives}", True, white)
  screen.blit(lives_text, (10, 10))

  level_text = font.render(f"Level: {level}", True, white)
  screen.blit(level_text, (width - 100, 10))

  # win condition
  if not bricks:
    win_text = font.render("YOU WIN!", True, red)
    screen.blit(win_text, (width // 2 - 50, height // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    running = False

  # game Over condition
  if game_over:
    game_over_text = font.render("GAME OVER", True, red)
    screen.blit(game_over_text, (width // 2 - 70, height // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    running = False

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
