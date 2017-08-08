import os
from xml.etree import ElementTree

#file_name = 'Within You Without You.xml'

songs = []
titleList = []

for root, dirs, files in os.walk('data'):
	for file in files:
            if (file.endswith('.xml')):
            	file = os.path.abspath(os.path.join('data', file))
            	song = ElementTree.parse(file)
            	songs.append(song)
            	print("___Parsing file: " + os.path.basename(file))
            	titleList.append(os.path.basename(file))

#full_file = os.path.abspath(os.path.join('data', file_name))

#song = ElementTree.parse(full_file)

instrument_list = {}

#def init_instrument_list:

# erhoeht den zaehler eines bestimmten tons in der tone_list
def put_in_array(a, note_type, tone_list):
	tone_list[a] += note_type
	tone_list["count"] += 1

# uebernimmt einen ton und das vorzeichen und gibt den resultierenden ton zurueck
# a:= ton, b:= vorzeichen
def manage_alter_value(a, b):
	if b == 1:
		if a == "C":
			return "C#"
		elif a == "D":
			return "D#"
		elif a == "E":
			return "F"
		elif a == "F":
			return "F#"
		elif a == "G":
			return "G#"
		elif a == "A":
			return "A#"
		elif a == "B":
			return "C"
	elif b== -1:
		if a == "C":
			return "B"
		elif a == "D":
			return "C#"
		elif a == "E":
			return "D#"
		elif a == "F":
			return "E"
		elif a == "G":
			return "F#"
		elif a == "A":
			return "G#"
		elif a == "B":
			return "A#"

def get_duration_as_value(a):
	type_list[a] += 1
	if a == "whole":
		return 1
	elif a == "half":
		return 0.5
	elif a == "quarter":
		return 0.25
	elif a == "eighth":
		return 0.125
	elif a == "16th":
		return 0.0625
	elif a == "32nd":
		return 0.03125
	elif a == "64th":
		return 0.015625

for i, song in enumerate(songs):

	instrument_list = {}
	tone_list = dict({"C":0, "C#":0, "D":0, "D#":0, "E":0, "F":0, "F#":0, "G":0, "G#":0, "A":0, "A#":0, "B":0, "count":0})
	type_list = dict({"whole":0, "half":0, "quarter":0, "eighth":0, "16th":0, "32nd":0, "64th":0})
	all_type_list = dict({"whole":0, "half":0, "quarter":0, "eighth":0, "16th":0, "32nd":0, "64th":0})

	notes = song.findall('.//note[pitch]')
	all_types = song.findall('.//type')

	for t in all_types:
		all_type_list[t.text] += 1

	for n in notes:
		if (n.find('pitch') == None):
			print(" pitch __ NONETYPEEE!!!!!!")
			break
		pitch = n.find('pitch')
	#pitches = song.findall('.//note/pitch')

	#for p in pitches:
	#	print("__Type-Knoten: " + n.find('type').text)
		if(n.find('type') == None):
			print("NONETYPEEE!!!!!!")

		note_type = get_duration_as_value(n.find('type').text)

		altervalue = 0
		actualstep = ""

		stepnode = pitch.find('step')
		alternode = pitch.find('alter')

		if alternode != None:
			altervalue = int(alternode.text)

		if stepnode != None:
			actualstep = stepnode.text
			if altervalue != 0:
				actualstep = manage_alter_value(actualstep, altervalue)
		
		put_in_array(actualstep, note_type, tone_list)
	print("____" + titleList[i] + "____")
	print(type_list)
	print(tone_list)
	print("inklusive percussion: " + str(all_type_list))
	print("")

