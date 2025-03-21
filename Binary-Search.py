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
pygame.display.set_caption("Binary Search Visualization")

def draw_array(arr, colors):
    screen.fill(BLACK)
    for i in range(len(arr)):
        pygame.draw.rect(screen, colors[i], (i * BAR_WIDTH, HEIGHT - arr[i], BAR_WIDTH, arr[i]))
    pygame.display.update()

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        draw_array(arr, [(GREEN if x == mid else WHITE) for x in range(len(arr))])
        time.sleep(0.2)
        if arr[mid] == target:
            draw_array(arr, [(RED if x == mid else WHITE) for x in range(len(arr))])
            time.sleep(1)
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    arr = [random.randint(10, HEIGHT - 50) for _ in range(WIDTH // BAR_WIDTH)]
    arr.sort()  # For binary search
    target = random.choice(arr)
    
    draw_array(arr, [WHITE] * len(arr))
    time.sleep(1)
    
    print("Performing Binary Search...")
    binary_search(arr, target)
    time.sleep(2)
    
    pygame.quit()

if __name__ == "__main__":
    main()
