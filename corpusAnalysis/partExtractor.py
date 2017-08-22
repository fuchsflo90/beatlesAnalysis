def init_baseline_partid(song):
	part_id = ""
	parts = song.findall(".//part")

	for i, part in enumerate(parts):
		staff_lines = part.find('measure/attributes/staff-details/staff-lines')
		if staff_lines != None and staff_lines.text == '4':
			part_id = part.attrib['id']

	return part_id