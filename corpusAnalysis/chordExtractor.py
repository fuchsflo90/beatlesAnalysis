import toneArrayGenerator
from collections import defaultdict
from xml.dom import minidom
from xml.etree import ElementTree


def extract_chord_list(part):

	chord_list = defaultdict(list)

	chord_sequence = extract_chord_sequence(part)

	for cs in chord_sequence:
		if chord_list.get(cs) is None:
			chord_list[cs] = 0
			print(str(chord_sequence))
			print("wert wird in dict geladen....")
		else: 
			chord_list[cs] += 1
			print("wert in dict wird erhoeht...")

	return chord_list

def extract_chord_sequence(part):

	chord_transcripts = extract_chord_transcripts(part)
	chord_sequence = [len(chord_transcripts)]

	for i, ct in enumerate(chord_transcripts):
		chord_squence[i] = interpret_chord(ct)

	return chord_sequence

def extract_chord_transcripts(part):

	notes = part.findall(".//note")

	all_chords_dict = {}
	chord_range_list = generate_chord_range_list(notes)

	#print(str(chord_range_list))

	for r in chord_range_list:
		# needs to be done because in the loop r is only the key inside the dict, we need the value instead
		current_range_tuple = chord_range_list.get(r)
		count = current_range_tuple[0]
		while count <= current_range_tuple[1]:
			all_chords_dict = put_note_to_chord_dict(notes[count], count, all_chords_dict)
			count += 1

	return all_chords_dict

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

def put_note_to_chord_dict(note, index, chorddict):

	print(prettify(note))

	single_chord_dict = {}
	entry = {}
	altervalue = 0

	if note.find("rest") != None:
		return chorddict

	pitch = note.find("pitch/step").text

	if note.find("alter") != None:
		altervalue = note.find("alter").text

	string = note.find("notations/technical/string").text
	fret = note.find("notations/technical/fret").text

	if altervalue != 0:
		pitch = toneArrayGenerator.manage_alter_value(pitch, altervalue)

	# build a dictionary with pitch, string and fret of a specific note
	single_chord_dict['p'] = pitch
	single_chord_dict['s'] = string
	single_chord_dict['f'] = fret

	# put the dictionary of a single note into the dictionary of the whole chord
	entry = {chorddict[index], single_chord_dict}
	chorddict[index] = entry
	return chorddict

def interpret_chord(tone_list):
	return ["a", "b", "C", "d", "a", "a", "e", "f", "g", "f#", "a", "e", "e"]

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

