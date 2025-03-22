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
pygame.display.set_caption("Insertion Sort Visualization")

def draw_array(arr, colors):
    screen.fill(BLACK)
    for i in range(len(arr)):
        pygame.draw.rect(screen, colors[i], (i * BAR_WIDTH, HEIGHT - arr[i], BAR_WIDTH, arr[i]))
    pygame.display.update()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            draw_array(arr, [(GREEN if x == j + 1 else WHITE) for x in range(len(arr))])
            time.sleep(0.05)
        
        arr[j + 1] = key
        draw_array(arr, [(RED if x == j + 1 else WHITE) for x in range(len(arr))])
        time.sleep(0.1)

def main():
    arr = [random.randint(10, HEIGHT - 50) for _ in range(WIDTH // BAR_WIDTH)]
    draw_array(arr, [WHITE] * len(arr))
    time.sleep(1)
    
    print("Performing Insertion Sort...")
    insertion_sort(arr)
    draw_array(arr, [GREEN] * len(arr))
    time.sleep(2)
    
    pygame.quit()

if __name__ == "__main__":
    main()
