import re
filename = raw_input("Enter the file name: ")
textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()
data = re.findall('[0-9]+', filetext)
sum_of_numbers = 0
for n in data:
	n = float(n)
	sum_of_numbers += n
print "The sum of the numbers in the file is", sum_of_numbers