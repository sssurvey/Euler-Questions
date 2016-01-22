#python problem 15

#grid = [[0 for i in range(20)] for i in range(20)]

grid =[]

for row in range(20):
	grid.append([])
	for column in range(20):
		grid[row].append('|x|')

def printGrid(grid):
	for row in grid:
		print ' '.join(row)

'''-----------------------------------------------------------'''
printGrid(grid)
