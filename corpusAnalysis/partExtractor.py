import toneArrayGenerator

def get_number_of_parts(song):
	parts = song.findall(".//part")
	return len(parts)

def init_baseline_partids(song):
	part_ids = []
	parts = song.findall(".//part")

	for i, part in enumerate(parts):
		staff_lines = part.find('measure/attributes/staff-details/staff-lines')
		if staff_lines != None and staff_lines.text == '4':
			part_ids.append(part.attrib['id'])

	return part_ids

def init_percussion_partids(song):
	part_ids = []

	parts = song.findall(".//part")

	for i, part in enumerate(parts):
		clef_sign = part.find('measure/attributes/clef/sign')
		if clef_sign != None and clef_sign.text == 'percussion':
			part_ids.append(part.attrib['id'])

	return part_ids

#search for a percussion part inside a song and return the first one that is found
#return tuple of (percussion_part_id, percussion_part)
#returns first part of the song instead if no percussion part can be identified
def get_percussion_part(song):
	parts = song.findall(".//part")

	percids = init_percussion_partids(song)

	if(len(percids) != 0):
		root = song.getroot()

		for child in root:
			if 'id' not in child.attrib:
				continue
			elif child.attrib['id'] in percids:
				print('returning precussion part .... ' + child.attrib['id'])
				return (child.attrib['id'] ,child)
			else:
				continue
	else:
		return get_first_part(song)

def get_first_part(song):
	parts = song.findall(".//part")
	return ("FP", parts[0])

def get_song_without_baseline_and_percussion(song):

	parts = song.findall(".//part")

	baseids = init_baseline_partids(song)
	percids = init_percussion_partids(song)

	root = song.getroot()

	for child in root:
		if 'id' not in child.attrib:
			continue
		elif child.attrib['id'] in baseids:
			root.remove(child)
		elif child.attrib['id'] in percids:
			root.remove(child)

	return root

