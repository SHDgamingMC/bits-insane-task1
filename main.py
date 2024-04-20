from collections import deque

def calculate_days(matrix):
    n = len(matrix)
    m = len(matrix[0])
    islands = []
    trees = {}

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def bfs(x, y):
        island_cells = set()
        knights = 0
        giants = 0
        q = deque([(x, y)])
        visited[x][y] = True
        while q:
            cx, cy = q.popleft()
            island_cells.add((cx, cy))
            if matrix[cx][cy] == 'K':
                knights += 1
            elif matrix[cx][cy] == 'G':
                giants += 1
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny) and matrix[nx][ny] != '0' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
        islands.append((island_cells, knights, giants))

    def find_islands():
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != '0' and not visited[i][j]:
                    bfs(i, j)

    def initialize_visited():
        return [[False] * m for _ in range(n)]

    def simulate():
        days = 0
        while len(islands) > 1:
            islands.sort(key=lambda x: -(x[1] * 10 + x[2]))
            winning_island = islands[0]
            for island_cells, knights, giants in islands[1:]:
                total_people = knights + giants
                total_apples = sum(trees.get(cell, 0) for cell in island_cells)
                apple_consumption = total_people
                if total_apples < apple_consumption:
                    return float('inf')
            islands = [winning_island]
            days += 1
        return days

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'T':
                trees[(i, j)] = trees.get((i, j), 0) + 300

    visited = initialize_visited()
    find_islands()
    days = simulate()
    return days

# Example usage:
matrix = [
    ['#', 'K', '0', '0', '0', '0'],
    ['#', '0', 'G', 'T', 'T', '0'],
    ['#', '0', '0', '0', '0', '0']
]
print(calculate_days(matrix))  # Output: 2


# Coded By Suvin