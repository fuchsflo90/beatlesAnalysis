import toneArrayGenerator

def extract_chord_list(part):

def extract_chord_sequence(part):
	chords = part.findall(".//note[chord]")

def extract_chord_transcripts(part):

	notes = part.findall(".//note")

	all_chords_dict = {}
	chord_range_list = {}

	range_start = 0
	range_end = 0

	for i, note in enumerate(notes):

		if note.find("chord") is None:
			break
		elif notes[i-1].find("chord") is None:
			range_start = (i-1)
			break
		elif notes[i+1].find("chord") is None:
			range_end = (i+1)

			range_tuple = (range_start, range_end)
			chord_range_list[rangestart] = range_tuple

			range_start = 0
			range_end = 0
			break
		else:
			break

	for r in chord_range_list:
		

	for i, note in enumerate(notes):

		if note.find("chord") is None:
			break

		else:
			chord_dict = {}
			previous = note.getprevious()

			if previous.find("chord") is None:
				chord_dict = put_note_to_chord_dict(previous, (i-1), chord_dict)
			else:
				break

			chord_dict = put_note_to_chord_dict(note, i, chord_dict)




def put_note_to_chord_dict(note, index, chorddict):

	single_chord_dict = {}

	pitch = note.find("step").text
	altervalue = note.find("alter").text
	string = note.find("string").text
	fret = note.find("fret").text

	if altervalue != None:
		pitch = toneArrayGenerator.manage_alter_value(pitch, altervalue)

		# build a dictionary with pitch, string and fret of a specific note
	single_chord_dict['p'] = pitch
	single_chord_dict['s'] = string
	single_chord_dict['f'] = fret

		# put the dictionary of a single note into the dictionary of the whole chord
	chorddict[index] = single_chord_dict
	return chorddict

def interpret_chord(tone_list):
