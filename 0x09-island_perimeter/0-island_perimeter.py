#!/usr/bin/python3
def island_perimeter(grid):
	row = len(grid)
	col = len(grid[0])
	perimeter = 0
		# Loop through row
	for i in range(row):
		# Loop through each column
        for j in range(col):
            # If the cell is land
            if grid[i][j] == 1:
                # Initialize a variable to count the water neighbors
                water = 0
                # Check the neighbor above
                if i == 0 or grid[i-1][j] == 0:
                    water += 1
                # Check the neighbor below
                if i == m-1 or grid[i+1][j] == 0:
                    water += 1
                # Check the neighbor to the left
                if j == 0 or grid[i][j-1] == 0:
                    water += 1
                # Check the neighbor to the right
                if j == n-1 or grid[i][j+1] == 0:
                    water += 1
                # Add the water count to the perimeter
                perimeter += water
    # Return the perimeter as the answer
    return perimeter
