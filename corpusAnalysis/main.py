import os
from xml.etree import ElementTree
from operator import itemgetter
import keyDetector
import toneArrayGenerator

# select the folder to use
foldername = "01_Please Please Me"

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

	#type_list = dict({"whole":0, "half":0, "quarter":0, "eighth":0, "16th":0, "32nd":0, "64th":0})
	#all_type_list = dict({"whole":0, "half":0, "quarter":0, "eighth":0, "16th":0, "32nd":0, "64th":0})

	# stores the partnumber of the baseline
	#baseline_partnumber = ""
	#baseline_partnumber = get_baseline_partnumber(song)

	#notes = song.findall(".//part[@id='" + baseline_partnumber + "']/measure/note[pitch]")
	#notes = song.findall(".//note[pitch]")
	#all_types = song.findall('.//type')
	baseline_partid = init_baseline_partid(song)
	base_part = song.find("part[@id='" + baseline_partid + "']")

	tone_array_extended = toneArrayGenerator.generate_tone_array(song)
	tone_array_short = tone_array_extended[1:8]

	print("____" + titleList[i] + "____")
	#print(type_list)
	#print(tone_list)
	#print("inklusive percussion: " + str(all_type_list))
	print(str(tone_array_short))
	#print("####### DOT COUNT ####### ----- " + str(dot_count))
	key_vector = keyDetector.build_tone_vector(tone_array_short)
	key = keyDetector.find_key(key_vector, tone_array_short[0][0])
	print("############# DER VECTOR WURDE FOLGENDER TONART ZUGEORDNET: " + key + "!!!")
	print("")
	print("------------------------------------------")
	print("ONLY WORK WITH BASELINE!!!")
	print("#### Baseline befindet sich unter Part: " + baseline_partid)
	btone_array_extended = toneArrayGenerator.generate_tone_array(base_part)
	btone_array_short = btone_array_extended[1:8]
	print(str(btone_array_short))
	bkey_vector = keyDetector.build_tone_vector(btone_array_short)
	bkey = keyDetector.find_key(bkey_vector, btone_array_short[0][0])
	print("############# DER VECTOR WURDE FOLGENDER TONART ZUGEORDNET: " + bkey + "!!!")
	print("")


