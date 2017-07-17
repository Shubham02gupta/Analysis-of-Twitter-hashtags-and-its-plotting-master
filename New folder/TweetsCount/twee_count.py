from csv import reader

with open("/Users/swapnilpote/Downloads/flare.csv") as f:
    data = list(reader(f))

tweet = []
for i in range(len(data) - 1, len(data) - 11, -1):
    tweet.append(data[i])

# Matplotlib
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = list(range(1,11))
y = []

for i in tweet:
    y.append(int(i[1]))


plt.bar(x, y, align='center')

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
