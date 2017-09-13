from operator import itemgetter
import toneArrayGenerator

#search the beat in a song and return it, clear pickup metrics
#the check for pickup metrics works by checking if the metric is active for more than one measure
def init_beat(song):
	beat_helper_dict = dict({"2/2":0, "8/4":0, "6/4":0, "5/4":0, "4/4":0, "3/4":0, "2/4":0, "1/4":0,"12/8":0, "10/8":0, "9/8":0, "8/8":0, "7/8":0, "6/8":0, "5/8":0, "4/8":0, "3/8":0, "1/8":0, "12/16":0})
	measures = song.findall(".//measure")
	measure_helper_array = []
	measure_array = []
	times_array = []

	for i, m in enumerate(measures):
		if m.find('attributes/time') != None:
			measure_helper_array.append(m)

	#print('measure helper array mit auftakten: ' + str(measure_helper_array))

	for i, m in enumerate(measure_helper_array):
		if (i == len(measure_helper_array)-1):
			measure_array.append(m.find('attributes/time'))
			continue
		if ((int(m.attrib['number']) + 1) == int(measures[i+1].attrib['number'])):
			continue
		else: measure_array.append(m.find('attributes/time'))

	#print('cleared measure_array ::::::::::::::::::: ' + str(measure_array))

	for i, m in enumerate(measure_array):
		beats = ""
		beats_type = ""

		beats = m.find("beats").text
		beats_type = m.find("beat-type").text

		beat_string = beats + "/" + beats_type
		beat_helper_dict[beat_string] += 1

	times_array = toneArrayGenerator.convert_dict_to_array(beat_helper_dict)
	sorted_times_array = sorted(times_array, key=itemgetter(1), reverse=True)
	cleared_sorted_times_array = []

	for met_tuple in sorted_times_array:
		if (met_tuple[1] > 0):
			cleared_sorted_times_array.append(met_tuple)
			continue
		else:
			continue

	return cleared_sorted_times_array
