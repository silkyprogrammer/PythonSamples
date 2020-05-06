"""
Goal of this script was to,
1. Read a file containing almost 200 lines
2. Each line had a format like "ABCD":"2020-05-06T05:30:18.759Z",
3. We have change this to a format equivalent to ABCD, 2020-05-06
"""

# Read the file
f = open("/somepath/file.txt","r")
lines = f.readlines()
values = []
for line in lines:
    data = line.replace('"',"")
    split = data.split(":")
    values.append(split)

for i in range(len(values)):
    print(values[i][0],",",values[i][1][:-3])
