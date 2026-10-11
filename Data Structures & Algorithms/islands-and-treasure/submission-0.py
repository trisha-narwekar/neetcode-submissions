class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # queue
        queue = deque()
        # visited set
        visited = set()
        # directions
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # loop through rows
        for row in range(len(grid)):
            # loop through the columns
            for col in range(len(grid[0])):
                # if treasure chest and if not visited yet
                if grid[row][col] == 0 and (row, col) not in visited:
                    # add to the queue
                    queue.append((row, col))
                    # add to the visited set
                    visited.add((row, col))
        # while queue
        while queue:
            r, c = queue.popleft()
            # loop through directions
            for x, y in directions:
                # new_row, new_col
                new_row = r + x
                new_col = c + y
                # check if new_row, new_col in bounds
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    # check if not water cell and not visited
                    if grid[new_row][new_col] == 2147483647 and (new_row, new_col) not in visited:
                        # add to queue and add to visited
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        # ++ to grid[row][col]
                        grid[new_row][new_col] = grid[r][c] + 1

