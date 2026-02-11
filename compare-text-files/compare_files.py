import sys
from itertools import zip_longest

file1_path = "file1.txt"
file2_path = "file2.txt"

if len(sys.argv) >= 3:
	file1_path = sys.argv[1]
	file2_path = sys.argv[2]

difference_found = False

with open(file1_path, "r", encoding="utf-8") as f1, open(file2_path, "r", encoding="utf-8") as f2:
	for line_no, (line1, line2) in enumerate(zip_longest(f1, f2), start=1):
		if line1 != line2:
			difference_found = True
			print(f"Line {line_no}:")
			print(f" File1: {line1.rstrip() if line1 else '<no line>'}")
			print(f" File2: {line2.rstrip() if line2 else '<no line>'}")

if not difference_found:
	print("All lines are identical.")
