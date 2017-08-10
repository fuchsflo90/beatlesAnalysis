from operator import itemgetter


tone_list = dict({"C":0, "C#":0, "D":0, "D#":0, "E":0, "F":0, "F#":0, "G":0, "G#":0, "A":0, "A#":0, "B":0, "count":0})
tone_array = []

# gets as input a part of a musicxml file and gives back an array of the tone material
def generate_tone_array(song):

	tone_list = dict({"C":0, "C#":0, "D":0, "D#":0, "E":0, "F":0, "F#":0, "G":0, "G#":0, "A":0, "A#":0, "B":0, "count":0})
	tone_array = []

	notes = song.findall(".//note[pitch]")

	for n in notes:

		dot_boolean = False

		if (n.find('pitch') == None):
			print(" pitch __ NONETYPEEE!!!!!!")
			break
		pitch = n.find('pitch')

		if(n.find('type') == None):
			print("NONETYPEEE!!!!!!")

		dot_boolean = (n.find('dot') != None)

		note_type = get_duration_as_value(n.find('type').text, dot_boolean)

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
		
		put_in_dict(actualstep, note_type, tone_list)

	tone_array = convert_dict_to_array(tone_list)
	sorted_tone_array = sorted(tone_array, key=itemgetter(1), reverse=True)
	
	return sorted_tone_array

# manages the value of a specific note in the tone_list
def put_in_dict(a, note_type, tone_list):
	tone_list[a] += note_type
	tone_list["count"] += 1

# gets a note and an altervalue and returns the normalized note
# a:= note, b:= alter value
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

# calculate a note duration and give back the value
# multiplies the values by 1.5 if the note is dotted
def get_duration_as_value(a, dot_bool):
	if a == "whole":
		return ((1*1.5) if dot_bool else 1)
	elif a == "half":
		return ((0.5*1.5) if dot_bool else 0.5)
	elif a == "quarter":
		return ((0.25*1.5) if dot_bool else 0.25)
	elif a == "eighth":
		return ((0.125*1.5) if dot_bool else 0.125)
	elif a == "16th":
		return ((0.0625*1.5) if dot_bool else 0.0625)
	elif a == "32nd":
		return ((0.03125*1.5) if dot_bool else 0.03125)
	elif a == "64th":
		return ((0.015625*1.5) if dot_bool else 0.015625)

## convert a dictionary to an array
def convert_dict_to_array (dictionary):

	array = []
	for k, v in dictionary.items():
		array.append((k, v))

	return array