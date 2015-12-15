import re
textfile = open('regex_sum_214714.txt', 'r')
filetext = textfile.read()
textfile.close()
data = re.findall('[0-9]+', filetext)
sum = 0
for n in data:
	n = float(n)
	sum += n
print sum