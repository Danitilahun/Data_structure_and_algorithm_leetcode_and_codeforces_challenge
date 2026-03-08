from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        rows = len(grid)
        cols = len(grid[0])
        minute = 0

        twos_position = deque([])
        ones_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    twos_position.append((row, col,0))
                
                if grid[row][col] == 1:
                    ones_count+=1

        positions = [(-1, 0),(1,0), (0,-1), (0,1)]

        def bfs(queue):
            nonlocal minute , ones_count

            while queue:

                row, col , level = queue.popleft()
                minute = level

                for position in positions:
                    r,c = position

                    if row + r >= 0 and row + r < rows and col + c >= 0 and col + c < cols  and grid[row + r][col + c] == 1:
                        ones_count -= 1
                        grid[row + r][col + c] = 2
                        twos_position.append((row + r, col + c, level + 1))

        bfs(twos_position)

        return minute if ones_count == 0 else -1 