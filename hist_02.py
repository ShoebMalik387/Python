import matplotlib.pyplot as plt

data = [10,20,20,30,30,40,50]

plt.hist (data,bins=4,color='green',edgecolor='black')

plt.xlabel ("interval")

plt.ylabel ("Frequency")

plt.title ("My First Histogram Graph")

plt.show ()