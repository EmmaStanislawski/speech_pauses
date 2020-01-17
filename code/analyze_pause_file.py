import sys
import numpy as np
import glob


def read_pauses_file(file_name):

	#opening a file and reading the data
	with open(file_name, 'r') as f:
		data = f.readlines()

	num_data_lines = len(data)

	#picking all lines and calculating number of data points
	num_lines = len(data)
	pauses_len = [] 

	file_start_time = None
	file_end_time = None

	#splitting rows into columns
	for curr_row_idx, curr_row in enumerate(data):
		curr_row = curr_row.strip('\n')
		items_in_row = curr_row.split('\t')
		#items_in_row = curr_row.split(',')
		print items_in_row

		if curr_row_idx == 1:
			file_start_time = float(items_in_row[0])

		if curr_row_idx == (num_data_lines-1):
			file_end_time= float(items_in_row[3])

		#only considering silences
		if items_in_row[2] == 'silent':
			#calculating pause length
			start_time_pause = float(items_in_row[0])
			#start_time_pause = float(items_in_row[1])
			end_time_pause = float(items_in_row[3])
			curr_pause_len = end_time_pause - start_time_pause

			# only considering silences >.25
			if curr_pause_len > 0.25:
				pauses_len.append(curr_pause_len)

	assert file_start_time is not None
	assert file_end_time is not None
	assert file_end_time >= file_start_time
	total_duration = file_end_time-file_start_time
	sum_pauses = sum(pauses_len)
	fraction_pauses_duration = float(sum_pauses)/total_duration
	print(file_start_time, file_end_time, sum_pauses, fraction_pauses_duration)

	#making a column for pause length
	# print(pauses_len)
	pauses_len = np.array(pauses_len) 

	# computing mean and standard deviation
	mean = pauses_len.mean()
	std = pauses_len.std()

	return mean, std, fraction_pauses_duration


def process_all_files_in_dir(dir_path):
	print 'dir_path', dir_path
	list_of_files = glob.glob(dir_path)
	print list_of_files

	f_out = open('./out.csv', 'w')
	f_out.write('subject_id,mean,std,fraction_pauses_duration\n')

	for curr_file_path in list_of_files:
		print '..............'
		print curr_file_path
		file_id = curr_file_path.replace('/', '_')
		#file_id = curr_file_path[-7:-4]
		print file_id
		mean, std, fraction_pauses_duration = read_pauses_file(curr_file_path)

		print(
			'Id: {} Mean: {}, Std: {}, FractionPauses'.format(file_id, mean, std, fraction_pauses_duration)
		)

		curr_record_str = '{},{},{},{}\n'.format(file_id, mean, std, fraction_pauses_duration)
		f_out.write(curr_record_str)
	f_out.close()


if __name__ == '__main__':
	dir_path = sys.argv[1]
	print dir_path
	process_all_files_in_dir(dir_path)
