import csv

writer = open('output.csv','w')

def close():
	writer.close()

def writeCSV(folder, arr):

	for i, element in enumerate(arr):
		if i == (len(arr)-1):
			writer.write(element)
		else:
			writer.write(element + ", ")

	writer.write("\n")