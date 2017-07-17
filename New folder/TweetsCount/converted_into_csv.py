import csv

f = open("/Users/swapnilpote/Code/Python/TweetsCount/tweets_count.csv")

for row in csv.reader(f):
   n_str = row[0].split("\t")
   hashtag = n_str[0]
   count = n_str[1]

   with open("/Users/swapnilpote/Code/Python/TweetsCount/tw.csv", "a") as f1:
      f1.write(hashtag + "," + count + '\n')
