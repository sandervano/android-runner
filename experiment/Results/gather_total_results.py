import csv
import os
directories = ['DOffT_2021.10.28_125532/data/exp/com-google-android-apps-maps/batterystats/',
               'DOnS_2021.11.04_022838/data/exp/com-google-android-apps-maps/batterystats/',
			   'DOnT_2021.10.29_084035/data/exp/com-google-android-apps-maps/batterystats/',
			   'LOffT_2021.10.29_190324/data/exp/com-google-android-apps-maps/batterystats/',
			   'LOnS_2021.11.03_020630/data/exp/com-google-android-apps-maps/batterystats/',
			   'LOnT_2021.10.29_011218/data/exp/com-google-android-apps-maps/batterystats/']

names = ['total_DOffT', 'total_DOnS', 'total_DOnT', 'total_LOffT', 'total_LOnS', 'total_LOnT']

for i in range(len(directories)):
	with open(names[i], mode='w', encoding='UTF8') as total_file:
		total_writer = csv.writer(total_file)
		for filename in os.listdir(directories[i]):
			if filename[0] == 'J':
				with open(directories[i]+filename, mode='r') as csv_file:
					csv_reader = csv.DictReader(csv_file)
					line_count = 0
					for row in csv_reader:
						total_writer.writerow([row['Joule_calculated'].strip()])
