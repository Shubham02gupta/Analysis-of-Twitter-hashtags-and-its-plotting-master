import csv
i=0
list1 = []
with open("/Users/swapnilpote/Downloads/flare.csv", "r") as f1:
      reader = csv.reader(f1)
      for row in reader:
          i=i+1
          list1.append(row)

print(i)

for count in range(i-1,i-11,-1):
   print(list1[count])
