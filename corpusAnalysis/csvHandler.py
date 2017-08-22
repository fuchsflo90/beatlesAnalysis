import csv
import sys

#writer = open(folder + '.csv','w')
writer = open(sys.argv[1] + '.csv','w')

def close():
	writer.close()

def writeCSV(folder, arr):

	for i, element in enumerate(arr):
		if i == (len(arr)-1):
			writer.write(element)
		else:
			writer.write(element + ",")

	writer.write("\n")