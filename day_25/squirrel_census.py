import pandas

data = pandas.read_csv('Squirrel_Data.csv')
# color_list = data['Primary Fur Color'].tolist()

gray_counter = len(data[data['Primary Fur Color'] == 'Grey'])
cin_counter = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_counter = len(data[data['Primary Fur Color'] == 'Black'])
nan_counter = len(data[data['Primary Fur Color'] == 'nan'])

# for x in color_list:
#     if x == 'Gray':
#         gray_counter += 1
#     elif x == 'Cinnamon':
#         cin_counter += 1
#     elif x == 'Black':
#         black_counter += 1
#     else:
#         nan_counter += 1

print(
    f'Nº of Grey squirrels: {gray_counter} \nNº of Cinnamon squirrels: {cin_counter}\nNº of Black squirrels: {black_counter}\nNº of unidentified squirrels:{nan_counter}')
data_dict = {"Fur_Color": ["Grey", "Red", "Black"], "Count": [gray_counter,cin_counter,black_counter]}

dtcsv = pandas.DataFrame(data_dict)
dtcsv.to_csv('Squirrels_by_color.csv')
