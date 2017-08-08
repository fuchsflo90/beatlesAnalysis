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

# b-keys
#		[c  c# d  d# e  f  f# g  g# a  a# b]
f = 	[1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
bb = 	[1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
eb = 	[1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
ab = 	[1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
db = 	[1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
gb = 	[0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1]
cb = 	[0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1]

## dictionary that stores all the key arrays
key_vector_list = dict({"C":c, "C#": cis, "D": d, "D#": eb, "E": e, "F": f, "F#": fis, "G": g, "G#", ab, "A": a, "A#": bb, "B": b})
## tone array that helps shifting the specific steps
tone_array = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
#store the difference values for every vector in a tuple array
differences_arr = []

def find_key (vector, longest_tone):

	## save major and parallel minor key
	major = (longest_tone)
	## shift in the tone_array 3 steps to the right to get the parallel minor key
	minor = (tone_array[tone_array.index(longest_tone)+3])

	current_key = ("default", 0)

	major_differences = get_vector_differences(vector, key_vector_list[major])
	minor_differences = get_vector_differences(vector, key_vector_list[minor])

	if(return_lower_value(major_differences, major_differences) == 0):
		current_key = (major, major_differences)
	elif(return_lower_value(major_differences, major_differences) == 1):
		current_key = (major, major_differences)
	elif(return_lower_value(major_differences, minor_differences) == 2):
		current_key = (minor, minor_differences)

	if(current_key[1] <= 2):
		print("the key seems to be: " + current_key[0] + ", calculated differences: " + current_key[1])
	elif:
		print("longest note seems not to be the key note!")
		print("calculating the most likely key....")

		differences_arr = build_differences_array(vector)



	return current_key[1]

# compare two vectors with 0 and 1 and return the differences
def get_vector_differences (vector1, vector2):

	calculated_differences = 0

	if len(vector1) != len(vector2):
		print("vectors have different size!")
		return -1
	else:
		for i, v in vector1:
			if (v + vector2[i]) == 1:
				calculated_differences += 1
		print("there are _" + calculated_differences + "_ differences between the vectors!")
		return calculated_differences

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
	for i, v in key_vector_list:
		differences_arr.append((i, key_vector_list.key))




