import toneArrayGenerator
from collections import defaultdict
from xml.dom import minidom
from xml.etree import ElementTree
import music21


def extract_chord_list(part):

	chord_list = defaultdict(dict)

	chord_sequence = extract_chord_sequence(part)
	for cs in chord_sequence:
		if chord_list.get(cs) is None:
			chord_list[cs] = 1
		else: 
			chord_list[cs] += 1

	return chord_list

def extract_chord_sequence(part):

	chord_transcripts = extract_chord_transcripts(part)
	chord_sequence = []

	#print(str(chord_transcripts))

	chord_transcripts = filter(None ,chord_transcripts)

	for i, ct in enumerate(chord_transcripts):
		chord_sequence.append(interpret_chord(ct))

	return chord_sequence

def extract_chord_transcripts(part):

	notes = part.findall(".//note")

	chord_range_list = generate_chord_range_list(notes)
	all_chords_arr = []

	#print(str(chord_range_list))


	for i, r in enumerate(chord_range_list):
		all_chords_arr.append(create_one_chord(chord_range_list.get(r), notes))

	return all_chords_arr

def generate_chord_range_list(notes):

	chord_range_list = {}

	range_start = 0
	range_end = 0

	for i, n in enumerate(notes):
		if n.find("chord") is None:
			continue
		elif notes[i-1].find("chord") is None:
			range_start = (i-1)
			continue
		elif (i) == (len(notes)-1):
			range_end = (i)

			range_tuple = (range_start, range_end)
			chord_range_list[range_start] = range_tuple

			return chord_range_list
		elif notes[i+1].find("chord") is None:
			range_end = (i)

			range_tuple = (range_start, range_end)
			chord_range_list[range_start] = range_tuple

			range_start = 0
			range_end = 0
			continue
		else:
			continue

	return chord_range_list

#generate a dict of the tonal and technical information of one note
def put_note_to_chord_array(note):

	#print(prettify(note))

	single_tone_dict = {}
	altervalue = 0

	if note.find("rest") != None:
		return chorddict

	pitch = note.find("pitch/step").text

	if note.find("pitch/alter") != None:
		altervalue = int(note.find("pitch/alter").text)

	string = note.find("notations/technical/string").text
	fret = note.find("notations/technical/fret").text

	if altervalue != 0:
		pitch = toneArrayGenerator.manage_alter_value(pitch, altervalue)

	# build a dictionary with pitch, string and fret of a specific note
	single_tone_dict['p'] = pitch
	single_tone_dict['s'] = string
	single_tone_dict['f'] = fret

	# put the dictionary of a single note into the dictionary of the whole chord
	return single_tone_dict

#generate an array of one chord
def create_one_chord(range_tuple, notes):
		chord = []
		i = 0

		count = range_tuple[0]
		while count <= range_tuple[1]:
			note = notes[count]
			if note.find('unpitched') != None:
				count +=1
				i+= 1
				continue
			elif note.find("notations/technical/string") is None:
				count +=1
				i+= 1
				continue
			else:
				chord.append(put_note_to_chord_array(note))
				count += 1
				i += 1
		if chord == []:
			return None
		else:
			return chord

#display the elementtree for debugging
def prettify(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

#searches for the closest value to the righten side of an array and returns its index
def find_first_value_in_array(arr):
	for i, v in enumerate(arr):
		if arr[len(arr)-i] is None:
			continue
		else:
			return (len(arr)-i)
	return "array seems to be empty: " + str(arr)

#does pattern matching over given chord with pitch and technical information
# and returns the specific chord name

# outsourced to the music21 package!
def interpret_chord(chord):

	hand_pattern = [None, None, None, None, None, None]
	normalized_hand_pattern = [None, None, None, None, None, None]
	tone_string = ""

	# safe string and fret information in the hand_pattern
	for tone in chord:
		#hand_pattern[(chord.get('s')-1)] = chord.get('f')
		#print(str(chord))
		tone_string += tone.get('p') + " "

	# for i,  v in enumerate(hand_pattern):
	# 	normalized_hand_pattern()
	#print(str(chord))
	music21chord = music21.chord.Chord(tone_string)

	return music21chord.pitchedCommonName


