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
pygame.display.set_caption("Quick Sort Visualization")

def draw_array(arr, colors):
    screen.fill(BLACK)
    for i in range(len(arr)):
        pygame.draw.rect(screen, colors[i], (i * BAR_WIDTH, HEIGHT - arr[i], BAR_WIDTH, arr[i]))
    pygame.display.update()

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        draw_array(arr, [(GREEN if x == j else WHITE) for x in range(len(arr))])
        time.sleep(0.05)
        
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_array(arr, [(RED if x == i or x == j else WHITE) for x in range(len(arr))])
            time.sleep(0.05)
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_array(arr, [(RED if x == i + 1 or x == high else WHITE) for x in range(len(arr))])
    time.sleep(0.05)
    return i + 1

def main():
    arr = [random.randint(10, HEIGHT - 50) for _ in range(WIDTH // BAR_WIDTH)]
    draw_array(arr, [WHITE] * len(arr))
    quick_sort(arr, 0, len(arr) - 1)
    draw_array(arr, [GREEN] * len(arr))
    time.sleep(2)
    pygame.quit()
    

if __name__ == "__main__":
    main()
