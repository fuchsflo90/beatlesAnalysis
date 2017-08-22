import os
import sys
from xml.etree import ElementTree
from operator import itemgetter
import keyDetector
import toneArrayGenerator
import csvHandler

# select the folder to use
#foldername = "11_Yellow Submarine"
foldername = sys.argv[1]

songs = []
titleList = []
instrument_list = {}

for root, dirs, files in os.walk('../corpus/MusicXML/' + foldername):
	for file in files:
            if (file.endswith('.xml')):
            	file = os.path.abspath(os.path.join('../corpus/MusicXML/' + foldername, file))
            	song = ElementTree.parse(file)
            	songs.append(song)
            	print("___Parsing file: " + os.path.basename(file))
            	titleList.append(os.path.basename(file))

def init_baseline_partid(song):
	part_id = ""
	parts = song.findall(".//part")

	for i, part in enumerate(parts):
		staff_lines = part.find('measure/attributes/staff-details/staff-lines')
		if staff_lines != None and staff_lines.text == '4':
			part_id = part.attrib['id']

	return part_id

for i, song in enumerate(songs):

	fifths_in_song = (keyDetector.find_fifths_in_song(song))

	baseline_partid = init_baseline_partid(song)
	base_part = song.find("part[@id='" + baseline_partid + "']")

	tone_array_extended = toneArrayGenerator.generate_tone_array(song)
	tone_array_short = tone_array_extended[1:8]
	#tone_array_short = tone_array_extended[1:6]

	print("____" + titleList[i] + "____")
	#print(type_list)
	#print(tone_list)
	#print("inklusive percussion: " + str(all_type_list))
	print(str(tone_array_short))
	#print("####### DOT COUNT ####### ----- " + str(dot_count))
	key_vector = keyDetector.build_tone_vector(tone_array_short)
	key = keyDetector.get_key(key_vector, tone_array_short[0][0], fifths_in_song)
	

	print("############# DER VECTOR WURDE FOLGENDER TONART ZUGEORDNET: " + key + "!!!")
	print("##Folgende Vorzeichen wurden gefunden: " + str(fifths_in_song[0:4]))
	
	print("#### Baseline befindet sich unter Part: " + baseline_partid)
	print("")

	csvHandler.writeCSV(foldername, [titleList[i], key, baseline_partid, tone_array_short[0][0], fifths_in_song[0][0]])

csvHandler.close()
