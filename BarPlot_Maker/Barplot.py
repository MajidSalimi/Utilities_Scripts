
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rows_per_category = 3
# Read the dataset from CSV
data = pd.read_csv('Input.csv')  # Replace 'dataset.csv' with the actual filename

# Plotting a bar plot for each column in the same plot
colors = ['green', 'indigo', 'orange', 'gray', 'salmon', 'maroon', 'blue' , 'olive', 'brown']  # Define the colors for each column

# Get the number of columns and the number of data points
num_columns = len(data.columns)
num_data_points = len(data.index)

# Calculate the width for each bar
bar_width = 0.8 / num_columns

# Set the x-axis positions for each bar
x = np.arange(num_data_points)

# Plot each column
plt.figure()

for i, column in enumerate(data.columns):
    values = data[column].tolist()
    x_pos = x + i * bar_width
    plt.bar(x_pos, values, width=bar_width, color=colors[i], label=column)

# Adding labels and title
# plt.xlabel('Runs')
plt.ylabel('Latency (s)')
# plt.title('Bar Plot - All Columns')

# Set the x-axis tick positions and labels
plt.xticks(x + (num_columns - 1) * bar_width / 2, data.index)

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
