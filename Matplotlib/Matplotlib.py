# Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension
#  NumPy. It provides an object-oriented API for embedding plots into applications using 
# general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural "pylab" interface
#  based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, 
# though its use is discouraged. SciPy makes use of Matplotlib for plotting.
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
# It provides a wide range of plotting capabilities, including line plots, scatter plots, bar charts,
#  histograms, and more. Matplotlib is highly customizable, allowing users to create complex and 
# visually appealing plots with ease. It is widely used in data analysis, scientific research, 
# and machine learning for visualizing data and results.
# https://matplotlib.org/stable/gallery/index.html

import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100) # Generate 100 points between 0 and 10
y = np.sin(x)

# Create a line plot
plt.figure(1)
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')

# Create a scatter plot
plt.figure(2)
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave Scatter Plot')

# Create a bar chart
plt.figure(3)
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 20]
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')

# Create a histogram
plt.figure(4)
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Create a pie chart
plt.figure(5)
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart Example')

# Create a box plot
plt.figure(6)
data = [np.random.randn(100) for _ in range(4)] 
plt.boxplot(data)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot Example')

# Create a heatmap
plt.figure(7)
data = np.random.rand(10, 10)
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap Example')

# Create a 3D plot
from mpl_toolkits.mplot3d import Axes3D
plt.figure(8)
fig = plt.figure(8)
ax = fig.add_subplot(111, projection='3d')
# Create meshgrid for x and y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
ax.plot_surface(x, y, z, cmap='viridis')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Plot Example')

# Show all plots at once
#plt.show()

# Create a subplot
# Subplots allow you to create multiple plots in a single figure, arranged in a grid.
# The plt.subplots() function is used to create a figure and a set of subplots. 
# It returns a figure object and an array of axes objects that can be used to plot on each subplot.
# In the example below, we create a 2x2 grid of subplots and plot different types of charts on each subplot.
#plt.figure(9)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot')
axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Scatter Plot')
axs[1, 0].bar(categories, values)
axs[1, 0].set_title('Bar Chart')
axs[1, 1].hist(data, bins=30)
axs[1, 1].set_title('Histogram')
# Adjust layout and show the plot
plt.tight_layout()
#plt.show()

# Save a plot to a file
# plt.figure(10)
# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sine Wave')
# plt.savefig('sine_wave.png')

print("\n================ Matplotlib: Object Oriented Method ==================\n")
# Object-Oriented Method
# The object-oriented method in Matplotlib allows for more control and customization over the plots.
# Instead of using the state-based interface (like plt.plot()), you create figure and axes objects and call methods on them.
# This approach is more flexible and is recommended for complex plots or when you want to create multiple plots in the same figure.
# In the example below, we create a figure and an axes object, and then use the axes object to plot a line chart.
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sine Wave (Object-Oriented Method)')
#plt.show()

x = np.arange(0, 10, 0.5)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y, color='red', marker='o', linestyle='--')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Cosine Wave with Custom Style')
#plt.show()

x = np.linspace(-10,10,20)
fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(10, 5))

axes[0].plot(x, x**2 - x, x, x**3)
axes[0].set_title("Polynomial Functions")

axes[1].plot(x, x**2 + 1.5, x, x**4+ x**3-x**2+1)
axes[1].set_title("Polynomial Functions")

axes[2].plot(x, x*2+0.5, x, x**3)
axes[2].set_ylim([0, 30])
axes[2].set_xlim([0, 10])
axes[2].set_title("Polynomial Functions")
#plt.show()



# Matplotlib also supports various styles and themes that can be applied to the plots to enhance their appearance.
# You can use the plt.style.use() function to apply a specific style to your plots.
# Example of using a style
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis') 
ax.set_title('Sine Wave with ggplot Style')
plt.show()

