def initialize_cube(dims, base):
	if dims == 0:
		return False

	else:
		return [initialize_cube(dims - 1, base) for _ in range(base)]

class Cube(object):
	def __init__(self, dims, base):
		self.dims = dims
		self.base = base
		self.contents = initialize_cube(dims, base)

	def __str__(self):
		return str(self.contents)

	def __repr__(self):
		return str(self)

	def getcol(self, coords):
		if len(coords) != dims - 1:
			raise ValueError('a column in a cube of dimension {0} should be indicated by {1} coordinates, rather than {2}'.format(dims, dims - 1, coords))

			else:
				

board = Cube(6, 4)

def is_valid(newcoords):
	if any(
