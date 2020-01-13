import sys
import numpy as np
import glob


def read_pauses_file(file_name):

	#opening a file and reading the data
	with open(file_name, 'r') as f:
		data = f.readlines()

	#picking all lines and calculating number of data points
	num_lines = len(data)
	pauses_len = [] 

	#splitting rows into columns
	for curr_row in data:
		curr_row = curr_row.strip('\n')
		# items_in_row = curr_row.split('\t')
		items_in_row = curr_row.split(',')
		# print items_in_row

		#only considering silences
		if items_in_row[2] == 'silent':

			#calculating pause length
			# start_time_pause = float(items_in_row[0])
			start_time_pause = float(items_in_row[1])
			end_time_pause = float(items_in_row[3])
			curr_pause_len = end_time_pause - start_time_pause

			# only considering silences >.25
			if curr_pause_len > 0.25:
				pauses_len.append(curr_pause_len)

	#making a column for pause length
	# print(pauses_len)
	pauses_len = np.array(pauses_len) 

	# computing mean and standard deviation
	mean = pauses_len.mean()
	std = pauses_len.std()

	return mean, std


def process_all_files_in_dir(dir_path):
	print 'dir_path', dir_path
	list_of_files = glob.glob(dir_path)
	print list_of_files

	f_out = open('./out.csv', 'w')
	f_out.write('subject_id,mean,std\n')

	for curr_file_path in list_of_files:
		print '..............'
		print curr_file_path
		file_id = curr_file_path[-7:-4]
		print file_id
		mean, std = read_pauses_file(curr_file_path)

		print(
			'Id: {} Mean: {}, Std: {}'.format(file_id, mean, std)
		)

		curr_record_str = '{},{},{}\n'.format(file_id, mean, std)
		f_out.write(curr_record_str)
	f_out.close()


if __name__ == '__main__':
	dir_path = sys.argv[1]
	print dir_path
	process_all_files_in_dir(dir_path)
