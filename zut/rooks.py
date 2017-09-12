import time

def board_print():
	for i in board:
		for j in i:
			if j:
				print 'R',
			else:
				print '.',
		print
	print

board = [[False for _ in range(8)] for _ in range(8)]
sols = 0
steps = 0

def is_valid(newx, newy):
	if any(board[newx]):
		return False

	if any([i[newy] for i in board]):
		return False

	return True

def rook(x, y):
	global sols, board, steps

	steps += 1

	if is_valid(x, y):
		board[x][y] = True
		
#		board_print()
#		raw_input()
#		print x, y

		if x == 7:
			sols += 1

			board_print()

			board[x][y] = False

		else:
			for i in range(8):
				rook(x + 1, i)

			board[x][y] = False

for y in range(8):
	rook(0, y)

print sols
print steps
