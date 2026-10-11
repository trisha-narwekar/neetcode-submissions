class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # how many islands
        island = 0
        # queue
        queue = deque()
        # visited
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # check if it is a 1 and not been visited
                if grid[row][col] == "1" and (row, col) not in visited:
                    # add to queue
                    queue.append((row, col))
                    # add to visited
                    visited.add((row, col))
                    # add an island to counter
                    island += 1
        
                    # directions
                    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                    # while queue is existing
                    while queue:
                        row, col = queue.popleft()
                        # loop through all the different directions
                        for nr, nc in directions:
                            # mark down new row
                            new_row = row + nr
                            # mark down new col
                            new_col = col + nc
                            # check if the new row and col are in bounds
                            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                                # check if the cell is an island aka 1 and not visited
                                if grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                                    visited.add((new_row, new_col))
                                    queue.append((new_row, new_col))
        return island


