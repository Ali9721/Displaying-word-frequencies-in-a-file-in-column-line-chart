# Define 'countWord' function, fileName is a parameter.
# count repetition of each word and back it as function.
def countWord(fileName):
    myFile = open(fileName, 'r')
    counts = dict()
    words =  myFile.read().split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word]  = 1
    return counts

# Call 'countWord' & count repetition of each word's file and put it in function & show it with calling 'print'
data = countWord(input('Enter file name: '))
print(data)

# Add 'pyplot' package to use matplotlib to make plot.
import matplotlib.pyplot as plt

# Divide keys of data's dictionary with 'keys' method & put in names' list.
names = list(data.keys())

# Divide keys of data's dictionary with 'values' method & put in values' list.
values = list(data.values())

# Show  frequencies of each word in column line chart with values and name's labeling.
plt.bar(range(len(data)), values, tick_label=names)
plt.show()
