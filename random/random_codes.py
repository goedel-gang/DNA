import sys, random

'''generate a number of random dna barcodes'''

#read number to generate from command line arguments
tries = int(sys.argv[1])

for _ in range(tries):
	for _ in range(6):
		sys.stdout.write('actg'[random.randint(0, 3)])

	print

#python random_codes.py | python validity_sieve.py > codes.txt; wc -l codes.txt; cat codes.txt
#while (($(cat codes.txt | wc -l | sed 's/^ *//g') != 22)) {python random_codes.py 1000 | python validity_sieve.py 2 > codes.txt} 
#echo abc > txtfiles/23test.txt; i=0; while (($(cat txtfiles/23test.txt | wc -l | sed 's/^ *//g') != 23)) {python random_codes.py 1000 | python validity_sieve.py 2 > txtfiles/23test.txt; ((i++))}; echo $i
