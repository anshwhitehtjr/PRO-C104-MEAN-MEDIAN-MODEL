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

number_of_width_data = len(new_data)

new_data.sort()

if number_of_width_data % 2 == 0:
    median1 = float(new_data[number_of_width_data//2])
    median2 = float(new_data[number_of_width_data//2-1])
    median = (median1 + median2)/2
else:
    median = float(new_data[number_of_width_data//2])

print(f"median is {median}")
