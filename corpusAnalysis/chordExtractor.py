import toneArrayGenerator
from collections import defaultdict
from xml.dom import minidom
from xml.etree import ElementTree
from operator import itemgetter
import music21

def extract_chord_list(part):

	chord_list = defaultdict(dict)
	summed_chord_dict = defaultdict(dict)

	chord_sequence = extract_chord_sequence(part)
	for cs in chord_sequence:
		if chord_list.get(cs[1]) is None:
			chord_list[cs[1]] = cs[0]
		else: 
			chord_list[cs[1]] += cs[0]

	chord_list = toneArrayGenerator.convert_dict_to_array(chord_list)
	sorted_chord_list = sorted(chord_list, key=itemgetter(1), reverse=True)

	summed_chord_dict = sum_chords_by_root(sorted_chord_list, summed_chord_dict)
	summed_chord_list = toneArrayGenerator.convert_dict_to_array(summed_chord_dict)
	#print("OHNE VALUE :   " + str(summed_chord_list))
	summed_chord_list = add_value_to_chord_root(summed_chord_list)

	return summed_chord_list

def sum_chords_by_root(chords_arr, sum_chord_dict):

	for chord in chords_arr:

		root_split = chord[0].split('-', 1)
		value = chord[1]

		root = root_split[0]
		tail = root_split[1]

		if sum_chord_dict.get(root) is None:
			sum_chord_dict[root] = [(tail, value)]
		else:
			sum_chord_dict[root].append((tail, value))

	return sum_chord_dict

# sum up the values of the chord appearences and add it to the root
# return the list as a list of triples (root, value, [appearences])
def add_value_to_chord_root(chord_list):
	helperlist = []
	for root in chord_list:
		value = 0
		appearences = root[1]
		for a in appearences:
			value += a[1]

		helperlist.append((root[0], value, sorted(appearences, key=itemgetter(1), reverse=True)))
		helperlist = sorted(helperlist, key=itemgetter(1), reverse=True)

	return helperlist

def extract_chord_sequence(part):

	chord_transcripts = extract_chord_transcripts(part)
	chord_sequence = []

	#print(str(chord_transcripts))

	chord_transcripts = filter(None ,chord_transcripts)

	for i, ct in enumerate(chord_transcripts):
		chord_sequence.append((ct[0],interpret_chord(ct[1])))

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
	#	elif notes[i-1].find("chord") is None:
	#		range_start = (i-1)
	#		continue
	#	elif (i) == (len(notes)-1):
	#		range_end = (i)
#
#			range_tuple = (range_start, range_end)
#			chord_range_list[range_start] = range_tuple
#
#			return chord_range_list
#		elif notes[i-1].find("chord") is None and notes[i+1].find("chord") is None:
#			range_start = (i-1)
#			range_end = i
#			range_tuple = (range_start, range_end)
#			chord_range_list[range_start] = range_tuple
#
#			range_start = 0
#			range_end = 0
#			continue 
#		elif notes[i+1].find("chord") is None:
#			range_end = (i)
#
#			range_tuple = (range_start, range_end)
#			chord_range_list[range_start] = range_tuple
#
#			range_start = 0
#			range_end = 0
#			continue
#		else:
#			continue
		else:
			if notes[i-1].find("chord") is None:
				range_start = (i-1)

			if (i) == (len(notes)-1):
				range_end = (i)

				range_tuple = (range_start, range_end)
				chord_range_list[range_start] = range_tuple
				return chord_range_list

	#		if notes[i-1].find("chord") is None and notes[i+1].find("chord") is None:
	#			range_start = (i-1)
	#			range_end = i
	#			range_tuple = (range_start, range_end)
	#			chord_range_list[range_start] = range_tuple
#
#				range_start = 0
#				range_end = 0
#				continue
			if notes[i+1].find("chord") is None:
				range_end = (i)

				range_tuple = (range_start, range_end)
				chord_range_list[range_start] = range_tuple

				range_start = 0
				range_end = 0
				
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

		#get the position of the chord in notes
		count = range_tuple[0]

		#get the note duration of the chord
		dot = (notes[count].find('dot') != None)

		#if (dot == True):
			#print("DOTTED CHORD!!!!!! " + str(notes[count].find('type').text))

		duration = toneArrayGenerator.get_duration_as_value(notes[count].find('type').text, dot)

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
			duration_chord_tuple = (duration, chord)
			return duration_chord_tuple

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

# outsourced to the music21 package!
def interpret_chord(chord):

	tone_string = ""

	for tone in chord:

		tone_string += tone.get('p') + " "

	music21chord = music21.chord.Chord(tone_string)
	chordname = music21chord.pitchedCommonName

	#print("TONESTRING:   " + tone_string +  ", " + chordname)

	chordname = filter_chord_name(chordname)

	return chordname

def filter_chord_name(chord_str):

	#define parts of the chord name to delete from string
	strings_to_replace = [' triad', ' interval', ' trichord' , ' chord', 'incomplete ', ' tetramirror']

	new_chord_str = chord_str

	for s in strings_to_replace:
		new_chord_str = new_chord_str.replace(s, '')

	#replace some words just to make the string shorter
	new_chord_str = new_chord_str.replace('seventh', '7')
	new_chord_str = new_chord_str.replace('diminished', 'dim')
	new_chord_str = new_chord_str.replace('augmented', 'aug')
	new_chord_str = new_chord_str.replace('dominant 7', 'dominant-7')
	new_chord_str = new_chord_str.replace('dominant-', '')
	new_chord_str = new_chord_str.replace('major-7', 'maj7')

	return new_chord_str


