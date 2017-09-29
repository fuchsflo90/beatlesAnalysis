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
import rhythmManager
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
manual_key_count = 0

for i, song in enumerate(songs):

	key = ""
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

	## manually correct the false keys for a few songs
	if(titleList[i] == "For Your Blue.xml"):
		key = "D"
		manual_key_count += 1
	elif(titleList[i] == "I Me Mine.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "Tomorrow Never Knows.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Cry For A Shadow.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Lady Madonna.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "Old Brown Shoe.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Please Mr Postman.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "When I Get Home.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "Babys In Black.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "No Reply.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Rock And Roll Music.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "Its Only Love.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "The Word.xml"):
		key = "F"
		manual_key_count += 1
	elif(titleList[i] == "Think For Yourself.xml"):
		key = "G"
		manual_key_count += 1
	elif(titleList[i] == "Doctor Robert.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "Love You To.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "She Said She Said.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "Taxman.xml"):
		key = "D"
		manual_key_count += 1
	elif(titleList[i] == "Tomorrow Never Knows.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Yellow Submarine.xml"):
		key = "F#"
		manual_key_count += 1
	elif(titleList[i] == "Being For The Benefit Of Mr Kite.xml"):
		key = "D#"
		manual_key_count += 1
	elif(titleList[i] == "Getting Better.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Sgt Peppers Lonely Hearts Club Band.xml"):
		key = "G"
		manual_key_count += 1
	elif(titleList[i] == "Sgt Peppers Lonely Hearts Club Band Reprise.xml"):
		key = "F"
		manual_key_count += 1
	elif(titleList[i] == "Baby Youre A Rich Man.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Blue Jay Way.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Magical Mystery Tour.xml"):
		key = "E"
		manual_key_count += 1
	elif(titleList[i] == "Your Mother Should Know.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Glass Onion.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Happiness Is A Warm Gun.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Helter Skelter.xml"):
		key = "E"
		manual_key_count += 1
	elif(titleList[i] == "Julia.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Ob-La-Di Ob-La-Da.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "Rocky Raccoon.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "The Continuing Story Of Bungalow Bill.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Why Dont We Do It In The Road.xml"):
		key = "D"
		manual_key_count += 1
	elif(titleList[i] == "Wild Honey Pie.xml"):
		key = "G"
		manual_key_count += 1
	elif(titleList[i] == "All Together Now.xml"):
		key = "G"
		manual_key_count += 1
	elif(titleList[i] == "Hey Bulldog.xml"):
		key = "D"
		manual_key_count += 1
	elif(titleList[i] == "Carry That Weight.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "Come Together.xml"):
		key = "F"
		manual_key_count += 1
	elif(titleList[i] == "Her Majesty.xml"):
		key = "D"
		manual_key_count += 1
	elif(titleList[i] == "Polythene Pam.xml"):
		key = "E"
		manual_key_count += 1
	elif(titleList[i] == "The End.xml"):
		key = "A"
		manual_key_count += 1
	elif(titleList[i] == "I Me Mine.xml"):
		key = "C"
		manual_key_count += 1
	elif(titleList[i] == "One After 909.xml"):
		key = "B"
		manual_key_count += 1
	else:
		key = keyDetector.get_key(key_vector, tone_array_short[0][0], fifths_in_song)

	number_of_parts = partExtractor.get_number_of_parts(song)
	

	print("Der Song wurde folgender Tonart zugeordnet: " + key + "!!!")
	print("fifths in song!!!!!!!!!!! " + str(fifths_in_song))
	#print("##Folgende Vorzeichen wurden gefunden: " + str(fifths_in_song[0:4]))
	
	print("#### percussion befindet sich unter Part: " + str(partExtractor.init_percussion_partids(song)))
	metric_array = rhythmManager.init_beat(partExtractor.get_percussion_part(song)[1])
	print(str(metric_array))
	key_change_info = keyDetector.get_key_change_info(fifths_in_song);
	#print(str(chord_array))
	#print("TONE ARRAY EXTENDED: " + str(tone_array_extended))
	print("")
	#print("TONE ARRAY SHIFTED: " + str(tonalNormalizer.shift_tone_array(key, tone_array_extended[1:len(tone_array_extended)])))
	#print("")

	norm_tone_array = tonalNormalizer.normalize_tone_array(key, tone_array_extended[1:len(tone_array_extended)])
	norm_chord_array = tonalNormalizer.normalize_chord_array(key, chord_array)

	print("NORMALIZED:  " + str(norm_chord_array))
	#print("NORMALIZED ROMAN ARRAY !!!! " + str(norm_tone_array))
	print("")

	csvHandler.write_album_csv(titleList[i], number_of_parts, key, key_change_info, metric_array, norm_tone_array, norm_chord_array)
	csvHandler.write_correlation_csv(titleList[i], norm_tone_array, norm_chord_array)
## should be 46
print("manual key count: " + str(manual_key_count))
csvHandler.close()
