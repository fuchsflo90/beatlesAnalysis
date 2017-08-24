def init_baseline_partid(song):
	part_id = ""
	parts = song.findall(".//part")

	for i, part in enumerate(parts):
		staff_lines = part.find('measure/attributes/staff-details/staff-lines')
		if staff_lines != None and staff_lines.text == '4':
			part_id = part.attrib['id']

	return part_id

def init_percussion_partid(song):
	part_id = ""

	parts = song.findall(".//part")

	for i, part in enumerate(parts):
		clef_sign = part.find('measure/attributes/clef/sign')
		if clef_sign != None and clef_sign.text == 'percussion':
			part_id = part.attrib['id']

	return part_id

def get_song_without_baseline_and_percussion(song):

	parts = song.findall(".//part")

	baseid = init_baseline_partid(song)
	percid = init_percussion_partid(song)

	part_arr = []

	root = song.getroot()

	for child in root:
		if 'id' not in child.attrib:
			continue
		elif child.attrib['id'] == baseid:
			root.remove(child)
		elif child.attrib['id'] == percid:
			root.remove(child)

	# for p in parts:
	# 	if (p.attrib['id'] is baseid) or (p.attrib['id'] is percid):
	# 		continue
	# 	else:
	# 		part_arr.append(p)

	# return part_arr

	return root

