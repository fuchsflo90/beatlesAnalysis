import os
import sys
from xml.etree import ElementTree
from operator import itemgetter
import keyDetector
import toneArrayGenerator
import csvHandler
import partExtractor
import chordExtractor
import music21

# select the folder to use with command line
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

for i, song in enumerate(songs):

	fifths_in_song = (keyDetector.find_fifths_in_song(song))

	baseline_partid = partExtractor.init_baseline_partid(song)
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
	

	print("Der Song wurde folgender Tonart zugeordnet: " + key + "!!!")
	#print("##Folgende Vorzeichen wurden gefunden: " + str(fifths_in_song[0:4]))
	
	#print("#### Baseline befindet sich unter Part: " + baseline_partid)

	print(str(chordExtractor.extract_chord_list(partExtractor.get_song_without_baseline_and_percussion(song))))
	print("")

	#csvHandler.writeCSV(foldername, [titleList[i], key, baseline_partid, tone_array_short[0][0], fifths_in_song[0][0]])

csvHandler.close()
