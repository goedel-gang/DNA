import sys
from subprocess import Popen, PIPE

'''checks if stdin matches the output of gen_hadamard - used to check of a list of all the codes in order has been correctly decoded'''

proc = Popen(['python', 'gen_hadamard.py', sys.argv[1]], stdout=PIPE)
out = proc.communicate()[0]
proc.wait()

print out == sys.stdin.read()
