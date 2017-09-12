import sys, copy

class CeilError(Exception):
	pass

class CoOrd(object):
	def __init__(self, i):
		if i >= 4096:
			raise CeilError

		self.i = i

	def inc(self):

		return CoOrd(self.i + 1)

	def getCoOrds(self):
		ti = self.i

		for exp in range(5, -1, -1):
			yield ti // 4 ** exp
			ti -= 4 ** exp * (ti // 4 ** exp)

	def __str__(self):
		return 'coord{0}'.format(list(self.getCoOrds()))

	def __repr__(self):
		return str(list(self.getCoOrds()))

space = [[False for _ in range(4)] for _ in range(6)]

most = 0
arr = []

currCoOrd = CoOrd(0)

coords = []

while True:
	try:
		currCoOrd = currCoOrd.inc()

	except CeilError:
		try:
			currCoOrd = coords.pop(-1)
			space = [[False for _ in range(4)] for _ in range(6)]

			for c in coords:

				i = 0

				for j in c.getCoOrds():
					space[i][j] = True
					i += 1

		except IndexError:
			break

	print
	print currCoOrd
	print space
	print coords

	collisions = 0
	i = 0

	for j in currCoOrd.getCoOrds():
		if space[i][j]:
			collisions += 1

		i += 1

	if collisions > 2:
		print '##FAULTY FAULTY'
		continue

	i = 0

	for j in currCoOrd.getCoOrds():
		space[i][j] = True
		i += 1

	coords.append(currCoOrd)

	if len(coords) > most:
		print len(coords), most
		print coords
		most = len(coords)
		arr = coords[:]

print arr
