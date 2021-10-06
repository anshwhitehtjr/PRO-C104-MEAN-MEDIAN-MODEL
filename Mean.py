import csv
from os import read

# storing the value of the csv file to f
with open("HW.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_weight = file_data[i][2]
    new_data.append(float(n_weight))

number_of_weight_data = len(new_data)
total = 0

for x in new_data:
    total = total + x

mean = float(total)/int(number_of_weight_data)
print(f"Average is {str(mean)}")
