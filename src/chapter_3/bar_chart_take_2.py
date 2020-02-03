#!/usr/bin/python3

from collections import Counter
from matplotlib import pyplot as plt

grades = [85, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)  # Counter({80: 4, 90: 3, 70: 3, 0: 2, 60: 1})

plt.bar([x + 5 for x in histogram.keys()],  # Shift bars right by 5
        histogram.values(),  # give each bar its correct height
        edgecolor=(0, 0, 0))  # Black edges for each bar

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])  # x-axis labels 0, 10, ... 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()
