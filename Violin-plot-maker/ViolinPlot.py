import matplotlib.pyplot as plt
import numpy as np

collectn_1=[]
collectn_2=[]
collectn_3=[]

with open('input1') as data:
    for line in data:
        collectn_1.append(float(line))

with open('input2') as data:
    for line in data:
        collectn_2.append(float(line))

with open('input3') as data:
    for line in data:
        collectn_3.append(float(line))

## combine these different collections into a list
data_to_plot = [collectn_1, collectn_2, collectn_3]

# Create a figure instance
fig = plt.figure()

# Create an axes instance
ax = fig.add_axes([0.05,0.1,1,1])


# Create the boxplot
bp = ax.violinplot(data_to_plot)

plt.xlim(0, 4)
plt.grid(False)
plt.ylim(1, 2.7)
plt.show()


