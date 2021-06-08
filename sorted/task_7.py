import os
all_files = os.listdir()
txt_files = list(filter(lambda x: x[-4:] == '.txt', all_files))
dict = {}
for file in txt_files:
    with open(file, encoding='UTF-8') as f:
        data = f.readlines()
        length = len(data)
        dict[file] = [length, data]

sorted_values = sorted(dict.values())
sorted_dict = {}
for i in sorted_values:
    for key in dict.keys():
        if dict[key] == i:
            sorted_dict[key] = dict[key]

for key, value in sorted_dict.items():
    print(key)
    print(value[0])
    for i in value[1]:
        print(i.strip())

