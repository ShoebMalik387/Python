import matplotlib.pyplot as plt

w = [5,7,-2]

c = ["red","blue","green"]

plt.bar(w, c, color = c, width = w)

plt.xlabel ('name of students')
plt.ylabel ('marks')
plt.title ('marks vs name')
plt.show ()