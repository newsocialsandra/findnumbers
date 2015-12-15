import re
filename = raw_input("Enter the file name: ")
textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()
data = re.findall('[0-9]+', filetext)
sum = 0
for n in data:
	n = float(n)
	sum += n
print "The sum of the numbers in the file is", sum