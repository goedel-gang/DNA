import argparse, sys
from subprocess import Popen, PIPE

'''sieves dna barcodes based on their melting temperature calculated by oligotm'''

#parse command line arguments minimum temperature (defaults to -infinity), maximum temperature (defaults to infinity) and option v for verbose, to print temperatures
parser = argparse.ArgumentParser(description='get minimum and maximum temperatures')
parser.add_argument('--min', dest='min_val', type=float, default=-float('inf'), help='minimum melting temperature')
parser.add_argument('--max', dest='max_val', type=float, default= float('inf'), help='maximum melting temperature')
parser.add_argument('-v', dest ='vb', action='store_const', const=True, default=False, help='set the program to print temperatures')

args = parser.parse_args()

#go through stdin
for line in sys.stdin:
	line = line.strip()

	#get melting temperature of code from oligotm
	oligotm = Popen(["oligotm", line], stdout=PIPE)
	temp = oligotm.communicate()[0].strip()
	exit_code = oligotm.wait()

	#if the temperature is in the range, print it
	if args.min_val < float(temp) < args.max_val:
		print line,

		#if -v option is set, print temperature
		if args.vb:
			print temp
		else:
			print
