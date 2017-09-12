from subprocess import Popen, PIPE

#example of feeding a string to oligotm, and reading the stdout

string = 'accttg'

process = Popen(["oligotm", string], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()

print string, output.strip()
