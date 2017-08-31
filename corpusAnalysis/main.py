import os
import sys
from xml.etree import ElementTree
from operator import itemgetter
import keyDetector
import toneArrayGenerator
import csvHandler
import partExtractor
import chordExtractor
import tonalNormalizer
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

	base_parts = []
	fifths_in_song = (keyDetector.find_fifths_in_song(song))

	baseline_partids = partExtractor.init_baseline_partids(song)
	for bpid in baseline_partids:
		base_parts.append(song.find("part[@id='" + bpid + "']"))

	tone_array_extended = toneArrayGenerator.generate_tone_array(song)
	tone_array_short = tone_array_extended[1:8]
	#tone_array_short = tone_array_extended[1:6]
	chord_array = chordExtractor.extract_chord_list(partExtractor.get_song_without_baseline_and_percussion(song))

	print("____" + titleList[i] + "____")
	#print(type_list)
	#print(tone_list)
	#print("inklusive percussion: " + str(all_type_list))
	#print(str(tone_array_short))
	#print("####### DOT COUNT ####### ----- " + str(dot_count))
	key_vector = keyDetector.build_tone_vector(tone_array_short)
	key = keyDetector.get_key(key_vector, tone_array_short[0][0], fifths_in_song)
	number_of_parts = partExtractor.get_number_of_parts(song)
	

	print("Der Song wurde folgender Tonart zugeordnet: " + key + "!!!")
	#print("##Folgende Vorzeichen wurden gefunden: " + str(fifths_in_song[0:4]))
	
	#print("#### Baseline befindet sich unter Part: " + baseline_partid)

	print(str(chord_array))
	#print("TONE ARRAY EXTENDED: " + str(tone_array_extended))
	print("")
	#print("TONE ARRAY SHIFTED: " + str(tonalNormalizer.shift_tone_array(key, tone_array_extended[1:len(tone_array_extended)])))
	#print("")
	norm_tone_array = tonalNormalizer.normalize_tone_array(key, tone_array_extended[1:len(tone_array_extended)])
	norm_chord_array = tonalNormalizer.normalize_chord_array(key, chord_array)

	print("NORMALIZED:  " + str(norm_chord_array))
	#print("NORMALIZED ROMAN ARRAY !!!! " + str(norm_tone_array))
	print("")

	csvHandler.write_album_csv(titleList[i], number_of_parts, key, norm_tone_array, norm_chord_array)

csvHandler.close()
