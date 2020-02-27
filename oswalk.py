# recursive walk in directory
import os
for root, dirs, files in os.walk(os.getcwd()):
    print(files)


# filesize of all files in a dir(recursive)
import os
for filename in os.listdir("D:\\Personal\\project"):
    filepath = os.path.join("D:\\Personal\\project", filename)
    if os.path.isfile(filepath):
        print(filename, os.path.getsize(filepath))
        
os.path.isfile(path)
os.path.exists(path)
os.path.isdir(path)

## print first n lines of a file
# Method 1:
with open("fileName", "r") as f:
    counter = 0
    for line in f:
        print line
        counter += 1
        if counter == N: break

# Method 2:
with open("fileName", "r") as f:
    for i in xrange(N):
        line = f.next()
        print line
        
# read csv
>>> import csv
>>> exampleFile = open('example.csv')
>>> exampleReader = csv.reader(exampleFile)
>>> for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
        
# write csv
 import csv
➊ >>> outputFile = open('output.csv', 'w', newline='')
➋ >>> outputWriter = csv.writer(outputFile)
   >>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
   21
   >>> outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
   32
   >>> outputWriter.writerow([1, 2, 3.141592, 4])
   16
   >>> outputFile.close()
   
   csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
   
   # Read the CSV file in (skipping first row).
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue    # skip first row
    csvRows.append(row)
csvFileObj.close()
