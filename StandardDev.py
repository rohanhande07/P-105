import csv
import math

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    total = 0
    n = len(data)

    for x in data:
        total += int(x)
    
    mean = total/n
    return mean

squaredList = []

for number in data:
    a = int(number) - mean(data)
    #double multiplication sign for squaring
    a = a**2
    squaredList.append(a)

sum = 0

for n in squaredList:
    sum = sum + n

result = sum/(len(data)-1)

sd = math.sqrt(result)

print(sd)