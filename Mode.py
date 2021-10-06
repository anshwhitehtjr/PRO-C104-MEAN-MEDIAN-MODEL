import csv
from collections import Counter

with open("HW.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# print(file_data)
file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_width = file_data[i][2]
    new_data.append(float(n_width))

data = Counter(new_data)
mode_data_range = {
    '80-90': 0,
    '90-100': 0,
    '100-150': 0,
    '150-170': 0,
}

for width, occurence in data.items():
    if 80 < float(width) < 90:
        mode_data_range['80-90'] += occurence

    elif 90 < float(width) < 100:
        mode_data_range['90-100'] += occurence

    elif 100 < float(width) < 150:
        mode_data_range['100-150'] += occurence

    elif 150 < float(width) < 170:
        mode_data_range['150-170'] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in mode_data_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [
            int(range.split('-')[0]), int(range.split('-')[1])], occurence

print(mode_data_range.items())
mode = float((mode_range[0] + mode_range[1])/2)
print(f'mode is {mode}')
