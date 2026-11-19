class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_count, col_count, counter = len(grid), len(grid[0]), 0
        negative_count = 0
        while True:
            if grid[counter][col_count - 1] < 0:
                negative_count += row_count - counter
                col_count -= 1
            else:
                counter += 1

            if counter == row_count or col_count == 0:
                break
        return negative_count
