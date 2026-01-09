# with open('weather_data.csv') as dtfl:
#     data = dtfl.readlines()
#     print(data)
#
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temp_list = []
#     day_list = []
#     weather_list = []
#     for row in data:
#         temp_list.append(row[1])
#         day_list.append(row[0])
#         weather_list.append(row[2])
#     print(f'\n{temp_list}\n{day_list}\n{weather_list}')

import pandas
data = pandas.read_csv('weather_data.csv')
print(data['temp'])