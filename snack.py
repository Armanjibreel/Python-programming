import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Ball properties
ball_radius = 15
ball_x, ball_y = width // 2, height // 2
ball_dx, ball_dy = 4, 4  # Ball speed

# Paddle properties
paddle_width, paddle_height = 100, 15
paddle_x = (width - paddle_width) // 2
paddle_y = height - 30
paddle_speed = 8

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Score
score = 0
font = pygame.font.SysFont("comicsansms", 30)

def display_score():
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= width - ball_radius:
        ball_dx *= -1
    if ball_y <= 0:
        ball_dy *= -1

    # Ball collision with paddle
    if paddle_y < ball_y + ball_radius < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
        ball_dy *= -1
        score += 1

    # Ball falls off bottom
    if ball_y > height:
        print(f"Game Over! Your score: {score}")
        running = False

    # Draw paddle
    pygame.draw.rect(screen, blue, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    # Display score
    display_score()

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
