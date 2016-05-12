import csv

from itertools import zip_longest
test_list = [
    {'item1':3, 'item2':3, 'item3':5},
    {'item1':2, 'item2':6, 'item3':3},
    {'item1':18, 'item2':12, 'item3':1} ]

redone_dict = {}

for dic in test_list:
    for key in dic:
        if key not in redone_dict:
            redone_dict[key] = []
        redone_dict[key].append(dic[key])

print(redone_dict)
keys = sorted(redone_dict.keys())


# store json data dict keys



try:
    with open('info.csv', 'w', newline='') as output_file:
        dict_writer = csv.writer(output_file, delimiter=",", quotechar='|',quoting=csv.QUOTE_MINIMAL)
        dict_writer.writerow(keys)
        vals=zip(*[redone_dict[key] for key in keys])

        dict_writer.writerows(vals)

        #dict_writer.writerows(zip(*redone_dict.values()))

except Exception as mess:

    print(mess)







