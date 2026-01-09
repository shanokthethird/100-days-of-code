import pandas
data = pandas.read_csv('weather_data.csv')
print(data)
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(len(temp_list))
#
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data['temp'].mean())
# print(data['temp'].max())

print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday.temp[0]*(9/5)+32)

# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

