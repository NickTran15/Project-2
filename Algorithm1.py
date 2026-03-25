from collections import deque

def short_escape(grid, s1, s2, t1, t2):
    rows = len(grid)
    cols = len(grid[0])
    
    # Possible moves: down, up, right, left
    pMoves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Check invalid start or target
    if grid[s1][s2] == 1 or grid[t1][t2] == 1:
        return -1
    
    # Queue: (x, y, moves)
    q = deque()
    q.append((s1, s2, 0))
    
    # Visited array
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[s1][s2] = True
    
    # BFS
    while q:
        x, y, moves = q.popleft()
        
        # Check if target reached
        if x == t1 and y == t2:
            return moves
        
        # Explore neighbors
        for dx, dy in pMoves:
            nx, ny = x + dx, y + dy
            
            # Check bounds and validity
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, moves + 1))
    
    # If no path found
    return -1

grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

print(short_escape(grid, 0, 0, 3, 3))  # Output: 6