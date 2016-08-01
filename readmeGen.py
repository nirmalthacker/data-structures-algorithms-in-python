'''
Built this README File
'''
import os, sys

NUM_LINES = 3
MARKER = "'''"
README_DUMP = """
Auto Generated README File
--------------------------
Wrangling with a Python\n
\t -- Just a bunch of katas with Python\n
\t -- Algorithms + data structures + whatever else the mind wants to play with\n
\t -- Some recursive code uses rcviz for visualization of a recursive tree - cool stuff! see the rcviz fork.\n
\t -- Some code uses non-standard libraries\n
\n
"""
README_FNAME = "README.md"

rop = open(README_FNAME, 'w')
rop.truncate()
rop.write(README_DUMP)

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	filename, file_extension = os.path.splitext(f)
	if file_extension == ".py":
		lines = []
		fop = open(f)
		for i in range(NUM_LINES):
			lines.append(fop.readline().rstrip())
		if lines[0] == MARKER and lines[-1] == MARKER:
			rop.write(f + " : " + lines[1] + "\n")
			rop.write("\n")

rop.close()