import matplotlib.pyplot as plt

word_file = "../words_distribution.txt"
IOB_file = "../IOB_distribution.txt"

# Import data as a list of numbers
with open(word_file, "r") as textFile:
    data = textFile.split("\t")          # split based on spaces
    data = [float(point) for point in data] # convert strings to floats

# Plot as a time series plot
plt.plot(data)
plt.show()