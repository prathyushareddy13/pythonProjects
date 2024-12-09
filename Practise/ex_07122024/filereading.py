"""f = open('prat.txt','w')
f.write("This is a practise program for file reading. ")
f.close()"""

"""f = open('prat.txt', 'a')
f.write("Reading: Using 'r' mode to read from an existing file. Writing: Employing 'w' mode to write to a file, which may create a new file or overwrite an existing one.")
f.close()"""

"""f= open('prat.txt')
print(f.read(5))
f.seek(20)
print(f.read(10))

f.seek(0)
for line in f:
    print(line)"""
f = open('prat.txt')
#first = f.readline() # always reads the first line
full = f.readlines() # reads the complete file
#print(first)
print(full)




