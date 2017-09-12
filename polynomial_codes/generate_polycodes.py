import bisect, itertools, sys, random

class Term(object):
	'''A class to store an algebraic term, ax^b'''

	def __init__(self, coeff, power):
		self.coeff = coeff
		self.power = power

	#compares the order of the term, used in the Polynomial class to insert a term into the polynomial
	def __gt__(self, other):
		return self.power > other.power

	def __str__(self):
		return 'Term({0}, {1})'.format(self.coeff, self.power)

	def __repr__(self):
		return str(self)

	#for a more mathematical representation
	def pretty(self):
		return '{0}x^{1}'.format(self.coeff, self.power)

class Polynomial(object):
	'''A class to store an algebraic polynomial - composed of Terms. Basically it's got a bit of a wrapper thing going. It let me more readably do things with polynomials'''

	def __init__(self, terms):
		#list of terms
		self.poly = []

		for i in terms:

			ind = bisect.bisect_left(self.poly, i) - 1

			#if a term with that power already exists, add to it
			try:
				if self.poly[ind + 1].power == i.power:
					self.poly[ind + 1].coeff += i.coeff

				else:
					raise IndexError

			#else, create a new one
			except IndexError:
				self.poly.insert(ind + 1, i)

	#iterate through the component terms
	def __iter__(self):
		return self.poly.__iter__()

	#return number of terms
	def __len__(self):
		return len(self.poly)

	def __mul__(self, other):
		#multiply by a Term
		if isinstance(other, Term):
			return Polynomial([Term(i.coeff * other.coeff, i.power + other.power) for i in self.poly])

		#multiply by another Polynomial, done by adding together the multiplication of self with each Term in the other polynomial
		elif isinstance(other, Polynomial):
			return reduce(lambda a, b: a + b, [self * i for i in other])

		#multiply by a hopefully numeric type or crash and burn spectacularly
		else:
			return Polynomial([Term(i.coeff * other, i.power) for i in self.poly])

	def __add__(self, other):
		#add a Term, in the same fashion as __init__
		if isinstance(other, Term):
			out = self
			
			ind = bisect.bisect_left(out.poly, other) - 1

			try:
				if out.poly[ind + 1].power == other.power:
					out.poly[ind + 1].coeff += other.coeff

				else:
					raise IndexError

			except IndexError:
				out.poly.insert(ind + 1, other)

		#add a polynomial, by adding the individual terms
		elif isinstance(other, Polynomial):
			out = self

			for i in other:
				out += i

		return out
				

	def __str__(self):
		return 'Polynomial({0})'.format(self.poly)

	def __repr__(self):
		return str(self)

	#a more mathematical representation
	def pretty(self):
		return ' + '.join([i.pretty() for i in self])

	#get the value of a coefficient, from the power
	def get_coeff(self, power):
		ind = bisect.bisect_left(self.poly, Term(0, power))

		try:
			if self.poly[ind].power == power:
				return self.poly[ind].coeff

			else:
				raise IndexError

		except IndexError:
			return 0

#print a polynomial as a codeword
def print_code(poly, chars, length):
	for i in range(length):
		sys.stdout.write(str(poly.get_coeff(i) % chars))

	print

#gen = Polynomial([Term(random.randint(0, 4), random.randint(0, 4)) for _ in range(random.randint(4, 6))])

#print gen

gen = Polynomial([Term(1, 2), Term(1, 1), Term(1, 0)])

for i in range(len(gen) + 1):
	for j in itertools.combinations(gen, i):
		print_code(Polynomial(j) * gen, 2, 5)

#		print

#		print '({0})({1}) = ({2})'.format(Polynomial(j).pretty(), gen.pretty(), (Polynomial(j) * gen).pretty())

#		print_code(Polynomial(j) * gen, 4, 6)
