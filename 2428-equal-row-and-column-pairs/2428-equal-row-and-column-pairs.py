class Solution(object):
   def equalPairs(self, grid):
        g = list(map(list, zip(*grid)))  # Transpose the grid
        count = 0

        for row1 in grid:
            for row2 in g:
                if row1 == row2:
                    count += 1

        return count