from operator import itemgetter
import toneArrayGenerator
# defines how precise the calculantion is, a value of 2 means, the key will be defined
# although there are 2 differences in the compared vectors
# a precision value of 2 seemed to give the best results in a short evaluation
PRECISION = 2

# keys are represented by there position from the key cmajor/aminor
# notes that belong to the specific key are represented by 1

# #-keys
#		[c  c# d  d# e  f  f# g  g# a  a# b]
c = 	[1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
g = 	[1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
d = 	[0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
a = 	[0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]
e = 	[0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
b = 	[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
fis = 	[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
cis = 	[1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
## pentatonic scales
# c = 	[1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
# g = 	[0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]
# d = 	[0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
# a = 	[0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]
# e = 	[0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
# b = 	[0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]
# fis = 	[0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
# cis = 	[0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]

# b-keys
#		[c  c# d  d# e  f  f# g  g# a  a# b]
f = 	[1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
bb = 	[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
eb = 	[1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
ab = 	[1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
db = 	[1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
gb = 	[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
cb = 	[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]
## pentatonic scales
# f = 	[1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0]
# bb = 	[1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
# eb = 	[1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
# ab = 	[1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
# db = 	[0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
# gb = 	[0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
# cb = 	[0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]

## dictionary that stores all the key arrays
key_vector_list = dict({"C":c, "C#": cis, "D": d, "D#": eb, "E": e, "F": f, "F#": fis, "G": g, "G#": ab, "A": a, "A#": bb, "B": b})
## tone array that helps shifting the specific steps
tone_array = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
differences_arr = []

def get_key_change_info(fifths):
	output = []
	if (len(fifths) == 1):
		output.append("None")
		return output
	else:
		for value in fifths:
			output.append(get_key_by_fifths(value[0]))
		# return the output array without the first key because it should be the
		# same as the whole song got in the get_key method
		return output[1:len(output)]

def get_key(vector, longest_tone, fifths):
	if (len(fifths) == 1):
		if (fifths[0][0]) != "0":
			return get_key_by_fifths(fifths[0][0])
		else:
			return find_key(vector, longest_tone)
	else:
		return get_key_by_fifths(fifths[0][0])

def find_key (vector, longest_tone):

	#store the difference values for every vector in a tuple array
	differences_arr = []
	## save major and parallel minor key
	major = (longest_tone)
	## shift in the tone_array 3 steps to the right to get the parallel minor key
	minor = (tone_array[(tone_array.index(longest_tone)+3) % len(tone_array)])

	current_key = ("default", 0)

	major_differences = get_vector_differences(vector, key_vector_list[major])
	minor_differences = get_vector_differences(vector, key_vector_list[minor])

	if(return_lower_value(major_differences, minor_differences) == 0):
		current_key = (major, major_differences)
	elif(return_lower_value(major_differences, minor_differences) == 1):
		current_key = (major, major_differences)
	elif(return_lower_value(major_differences, minor_differences) == 2):
		current_key = (minor, minor_differences)

	## setting the precicion for the calculation...
	if(current_key[1] <= PRECISION):
		print("the key seems to be: " + current_key[0] + ", calculated differences: " + str(current_key[1]))
	else:
		print("longest note -(" + longest_tone + ")- seems not to be the key note!")
		print("calculating the most likely key....")

		differences_arr = build_differences_array(vector)
		sorted_differences_arr = sorted(differences_arr, key=itemgetter(0))
		current_key = (sorted_differences_arr[0][1], sorted_differences_arr[0][0])

	return current_key[0]

# compare two vectors with 0 and 1 and return the differences
def get_vector_differences (vector1, vector2):

	calculated_differences = 0

	if len(vector1) != len(vector2):
		print("vectors have different size!")
		return -1
	else:
		for i, v in enumerate(vector1):
			if (v + vector2[i]) == 1:
				calculated_differences += 1
		return calculated_differences

def find_fifths_in_song (song):

	fifths_list = dict({"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "-1":0, "-2":0, "-3":0, "-4":0, "-5":0, "-6":0, "-7":0})

	fifths = song.findall(".//fifths")

	for f in fifths:
		fifths_list[f.text] += 1

	fifths_array = toneArrayGenerator.convert_dict_to_array(fifths_list)
	sorted_fifths_array = sorted(fifths_array, key=itemgetter(1), reverse=True)

	cleared_sorted_fifths_array = []

	for fifths in sorted_fifths_array:
		if fifths[1] > 0:
			cleared_sorted_fifths_array.append(fifths)
			continue
		else:
			continue

	return cleared_sorted_fifths_array

def get_key_by_fifths (f):
	if f == "0":
		return "C"
	elif f == "1":
		return "G"
	elif f == "2":
		return "D"
	elif f == "3":
		return "A"
	elif f == "4":
		return "E"
	elif f == "5":
		return "B"
	elif f == "6":
		return "F#"
	elif f == "7":
		return "C#"
	elif f == "-1":
		return "F"
	elif f == "-2":
		return "A#"
	elif f == "-3":
		return "D#"
	elif f == "-4":
		return "G#"
	elif f == "-5":
		return "C#"
	elif f == "-6":
		return "F#"
	elif f == "-7":
		return "B"

# shows which of two values is the higher one, if they are equal return 0
def return_lower_value (v1, v2):
	if v1 == v2:
		return 0
	elif v1 < v2:
		return 1
	elif v1 > v2:
		return 2
	else:
		print("values cannot be compared!")

#build an array that stores the differences of a given vector compared to the key vectors
def build_differences_array(vector):
	differences_arr = []
	for i, v in key_vector_list.items():
		differences_arr.append((get_vector_differences(v, vector), i))

	return differences_arr

# build a tone vector from an input array
def build_tone_vector(tone_array):

	print("..... building the tone vector")
	tone_vector = [0,0,0,0,0,0,0,0,0,0,0,0]
	helper_dict = dict({"C": 0, "C#": 0, "D": 0, "D#": 0, "E": 0, "F": 0, "F#": 0, "G": 0, "G#": 0, "A": 0, "A#": 0, "B": 0})
	# iterate through the input array and set the values of the specific tones to 1
	for t in tone_array:
		helper_dict[t[0]] = 1

	# store the values in an array that represents the vector
	tone_vector[0] = helper_dict["C"]
	tone_vector[1] = helper_dict["C#"]
	tone_vector[2] = helper_dict["D"]
	tone_vector[3] = helper_dict["D#"]
	tone_vector[4] = helper_dict["E"]
	tone_vector[5] = helper_dict["F"]
	tone_vector[6] = helper_dict["F#"]
	tone_vector[7] = helper_dict["G"]
	tone_vector[8] = helper_dict["G#"]
	tone_vector[9] = helper_dict["A"]
	tone_vector[10] = helper_dict["A#"]
	tone_vector[11] = helper_dict["B"]

	print("the tone vector is represented as following: .... " + str(tone_vector))
	return tone_vector

# key = find_key([0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1], "A")

