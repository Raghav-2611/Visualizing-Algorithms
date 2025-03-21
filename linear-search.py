import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Linear Search Visualization")

def draw_array(arr, colors):
    screen.fill(BLACK)
    for i in range(len(arr)):
        pygame.draw.rect(screen, colors[i], (i * BAR_WIDTH, HEIGHT - arr[i], BAR_WIDTH, arr[i]))
    pygame.display.update()

def linear_search(arr, target):
    for i in range(len(arr)):
        draw_array(arr, [(GREEN if x == i else WHITE) for x in range(len(arr))])
        time.sleep(0.05)
        if arr[i] == target:
            draw_array(arr, [(RED if x == i else WHITE) for x in range(len(arr))])
            time.sleep(1)
            return i
    return -1

def main():
    arr = [random.randint(10, HEIGHT - 50) for _ in range(WIDTH // BAR_WIDTH)]
    target = random.choice(arr)
    
    draw_array(arr, [WHITE] * len(arr))
    time.sleep(1)
    
    print("Performing Linear Search...")
    linear_search(arr, target)
    time.sleep(2)
    
    pygame.quit()

if __name__ == "__main__":
    main()
