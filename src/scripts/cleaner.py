import sys

input_file = sys.argv[1]
new_input_file = "new_tmp_output.txt"
new_lines = []
with open(input_file, "r") as f:
	for line in f:
		if (line[0] == 'O'):
			new_lines.append('O')
		else:
			new_lines.append(line[:-1])
#print new_lines

with open(new_input_file, "w") as f:
	for el in new_lines:
		f.write(el + "\n")