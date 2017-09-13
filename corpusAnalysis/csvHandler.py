import csv
import sys

#writer = open(folder + '.csv','w')
writer = open('output/' + sys.argv[1] + '.csv','w')
writer.write("song_title; number_of_parts; key; key_change_info; metrics; i; i#; ii; ii#; iii; iv; iv#; v; v#; vi; vi#; vii; chord_i; chord_i#; chord_ii; chord_ii#; chord_iii; chord_iv; chord_iv#; chord_v; chord_v#; chord_vi; chord_vi#; chord_vii\n")

def close():
	writer.close()

def writeCSV(arr):

	for i, element in enumerate(arr):
		if i == (len(arr)-1):
			writer.write(element)
		else:
			writer.write(element + ",")

	writer.write("\n")

def write_album_csv(song_title, number_of_parts, key, key_change_info, metrics, normalized_tone_array, normalized_chord_array):

	# cut the file ending (.xml)
	song_title = song_title[0:(len(song_title)-4)]
	song_title = song_title.lower()
	song_title = song_title.replace(' ', '_')

	writer.write(song_title + ";" + str(number_of_parts) + ";" + key + ";" + str(key_change_info) + ";" + str(metrics) + ";")

	for i, step in enumerate(normalized_tone_array):
		if i == (len(normalized_tone_array)-1):
			writer.write(str(step[1]) + ";")
		else:
			writer.write(str(step[1]) + ";")

	for i, cs in enumerate(normalized_chord_array):
		if i == (len(normalized_chord_array)-1):
			writer.write(str(cs[1]) + str(cs[2]))
		else:
			writer.write(str(cs[1]) + str(cs[2]) + ";")

	writer.write("\n")