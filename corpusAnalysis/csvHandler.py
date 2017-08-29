import csv
import sys

#writer = open(folder + '.csv','w')
writer = open('output/' + sys.argv[1] + '.csv','w')
writer.write("song_title, key, i, i#, ii, ii#, iii, iv, iv#, v, v#, vi, vi#, vii\n")

def close():
	writer.close()

def writeCSV(arr):

	for i, element in enumerate(arr):
		if i == (len(arr)-1):
			writer.write(element)
		else:
			writer.write(element + ",")

	writer.write("\n")

def write_album_csv(song_title, key, normalized_tone_array):
	writer.write(song_title + "," + key + ",")

	for i, step in enumerate(normalized_tone_array):
		if i == (len(normalized_tone_array)-1):
			writer.write(str(step[1]))
		else:
			writer.write(str(step[1]) + ",")

	writer.write("\n")