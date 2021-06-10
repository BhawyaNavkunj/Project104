import csv
from collections import Counter

with open("data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

data_for_mean = []
data_for_median = []
for i in range(len(file_data)):
    num = file_data[i][2]
    data_for_mean.append(float(num))
    data_for_median.append(float(num))

n = len(data_for_mean)
data_for_median.sort()

def calculate_mean():
    total = 0
    for i in data_for_mean:
        total += i
    mean = total/n
    print("Mean : " + str(mean))

def calculate_median():
    if n % 2 == 0:
        median1 = float(data_for_median[n//2])
        median2 = float(data_for_median[n//2-1])
        median = (median1 + median2)/2
    else:
        median = float(data_for_median[n//2])
    print("Median : " + str(median))

def calculate_mode():
    data_for_mode = Counter(data_for_median)
    data_for_range = {
        "75-85":0,
        "85-95":0,
        "95-105":0,
        "105-115":0,
        "115-125":0,
        "125-135":0,
        "135-145":0,
        "145-155":0,
        "155-165":0,
        "165-175":0
    }

    for height,occurence in data_for_mode.items():
        if 75<float(height)<85:
            data_for_range["75-85"] += occurence
        elif 85<float(height)<95:
            data_for_range["85-95"] += occurence
        elif 95<float(height)<105:
            data_for_range["95-105"] += occurence
        if 105<float(height)<115:
            data_for_range["105-115"] += occurence
        elif 115<float(height)<125:
            data_for_range["115-125"] += occurence
        elif 125<float(height)<135:
            data_for_range["125-135"] += occurence
        if 135<float(height)<145:
            data_for_range["135-145"] += occurence
        elif 145<float(height)<155:
            data_for_range["145-155"] += occurence
        elif 155<float(height)<165:
            data_for_range["155-165"] += occurence
        elif 165<float(height)<175:
            data_for_range["165-175"] += occurence

    mode_range,mode_occurence = 0,0
    for range,occurence in data_for_range.items():
        if occurence > mode_occurence:
            mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

    mode = float((mode_range[0]+mode_range[1])/2)
    print("Mode : " + str(mode))

calculate_mean()
calculate_median()
calculate_mode()


