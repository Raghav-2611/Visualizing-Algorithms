import pygame
import heapq
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra's Algorithm Visualization")

def draw_grid(grid, path=[]):
    screen.fill(WHITE)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            color = BLACK if grid[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, (200, 200, 200), (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
    
    for node in path:
        pygame.draw.rect(screen, GREEN, (node[1] * GRID_SIZE, node[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.display.update()

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0
    pq = [(0, start)]
    prev = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while pq:
        dist, (r, c) = heapq.heappop(pq)
        if (r, c) == end:
            path = []
            while (r, c) in prev:
                path.append((r, c))
                r, c = prev[(r, c)]
            path.reverse()
            return path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_dist = dist + 1
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, (nr, nc)))
                    prev[(nr, nc)] = (r, c)
        
        draw_grid(grid, prev.keys())
        pygame.time.delay(50)
    return []

def main():
    grid = [[random.choice([0, 0, 0, 1]) for _ in range(WIDTH // GRID_SIZE)] for _ in range(HEIGHT // GRID_SIZE)]
    start, end = (0, 0), (HEIGHT // GRID_SIZE - 1, WIDTH // GRID_SIZE - 1)
    grid[start[0]][start[1]] = grid[end[0]][end[1]] = 0
    draw_grid(grid)
    path = dijkstra(grid, start, end)
    draw_grid(grid, path)
    pygame.time.delay(3000)
    pygame.quit()

if __name__ == "__main__":
    main()
