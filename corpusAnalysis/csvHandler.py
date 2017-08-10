import csv

writer = open('output.csv','w')

def close():
	writer.close()

def writeCSV(arr):

	for element in arr:
		writer.write(element + ", ")

	writer.write("\n")