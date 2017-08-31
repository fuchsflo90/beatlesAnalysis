normalized_tone_list = dict({"C": "I", "C#": "I#", "D": "II", "D#": "II#", "E": "III", "F": "IV", "F#": "IV#", "G": "V", "G#": "V#", "A": "VI", "A#": "VI#", "B": "VII"})
tone_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def normalize_chord_array(key, chord_arr):
	shifted_chord_array = shift_chord_array(key, chord_arr)
	normalized_chord_arr = []

	for c in shifted_chord_array:
		normalized_chord_arr.append((normalized_tone_list.get(c[0]), c[1], c[2]))

	output_chord_array = sort_normalized_chord_arr(normalized_chord_arr)
	return output_chord_array

#create a shifted tone array depending on the key and return the normalized roman step array depending on the key
def normalize_tone_array(key, tone_arr):

	shifted_tone_array = shift_tone_array(key, tone_arr)
	normalized_tone_arr = []

	for t in shifted_tone_array:
		normalized_tone_arr.append((normalized_tone_list.get(t[0]), t[1]))

	output_array = sort_normalized_output(normalized_tone_arr)
	return output_array

#create a tone array that is shifted by the distance between "C" and the key
def shift_tone_array(key, tone_arr):
	tone_distance = get_distance(key, "C")
	#print("TONAL DISTANCE!!! " + str(tone_distance))
	result_tone_array = []

	for i, t in enumerate(tone_arr):
		result_tone_array.append((shift_tone(t[0], tone_distance),t[1]))

	return result_tone_array

#same procedure as shift_tone_array
def shift_chord_array(key, chord_arr):
	tone_distance = get_distance(key, "C")
	result_chord_array = []

	for i, c in enumerate(chord_arr):
		result_chord_array.append((shift_tone(c[0], tone_distance), c[1], c[2]))

	return result_chord_array

#get the distance between a tone and an anchor in the tone_list
def get_distance(tone, anchor):
	distance_right = get_index_of_value(tone, tone_list) - get_index_of_value(anchor, tone_list)
	distance_left = len(tone_list) - distance_right

	return distance_left

#shift a tone in the tone_list
def shift_tone(tone, distance):
	new_index = (get_index_of_value(tone, tone_list) + distance) % len(tone_list)
	new_tone = tone_list[new_index]

	return new_tone

def sort_normalized_output(arr):
	output_arr = []
	helper_dict = dict({"I": 0, "I#": 0, "II": 0, "II#": 0, "III": 0, "IV": 0, "IV#": 0, "V": 0, "V#": 0, "VI": 0, "VI#": 0, "VII": 0})

	for v in arr:
		helper_dict[v[0]] = v[1]

	output_arr.append(("I", helper_dict.get("I")))
	output_arr.append(("I#", helper_dict.get("I#")))
	output_arr.append(("II", helper_dict.get("II")))
	output_arr.append(("II#", helper_dict.get("II#")))
	output_arr.append(("III", helper_dict.get("III")))
	output_arr.append(("IV", helper_dict.get("IV")))
	output_arr.append(("IV#", helper_dict.get("IV#")))
	output_arr.append(("V", helper_dict.get("V")))
	output_arr.append(("V#", helper_dict.get("V#")))
	output_arr.append(("VI", helper_dict.get("VI")))
	output_arr.append(("VI#", helper_dict.get("VI#")))
	output_arr.append(("VII", helper_dict.get("VII")))

	return output_arr

#same procedure as sort_normalized_output
def sort_normalized_chord_arr(arr):
	output_arr = []
	helper_dict = dict({"I": (0, [None]), "I#": (0, [None]), "II": (0, [None]), "II#": (0, [None]), "III": (0, [None]), "IV": (0, [None]), "IV#": (0, [None]), "V": (0, [None]), "V#": (0, [None]), "VI": (0, [None]), "VI#": (0, [None]), "VII": (0, [None])})

	for v in arr:
		helper_dict[v[0]] = (v[1], v[2])

	output_arr.append(("I", helper_dict.get("I")[0], helper_dict.get("I")[1]))
	output_arr.append(("I#", helper_dict.get("I#")[0], helper_dict.get("I#")[1]))
	output_arr.append(("II", helper_dict.get("II")[0], helper_dict.get("II")[1]))
	output_arr.append(("II#", helper_dict.get("II#")[0], helper_dict.get("II#")[1]))
	output_arr.append(("III", helper_dict.get("III")[0], helper_dict.get("III")[1]))
	output_arr.append(("IV", helper_dict.get("IV")[0], helper_dict.get("IV")[1]))
	output_arr.append(("IV#", helper_dict.get("IV#")[0], helper_dict.get("IV#")[1]))
	output_arr.append(("V", helper_dict.get("V")[0], helper_dict.get("V")[1]))
	output_arr.append(("V#", helper_dict.get("V#")[0], helper_dict.get("V#")[1]))
	output_arr.append(("VI", helper_dict.get("VI")[0], helper_dict.get("VI")[1]))
	output_arr.append(("VI#", helper_dict.get("VI#")[0], helper_dict.get("VI#")[1]))
	output_arr.append(("VII", helper_dict.get("VII")[0], helper_dict.get("VII")[1]))

	return output_arr

#get the index of a specific value inside an array
def get_index_of_value(val, arr):
	index = -100
	for i, v in enumerate(arr):
		if v == val:
			index = i
	return index
