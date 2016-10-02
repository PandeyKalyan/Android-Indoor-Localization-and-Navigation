# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:35:40 2016
@author: pandey
"""
import numpy as np
import matplotlib.pyplot as plt

A = -2  # RSSI value at 1m distance
n = 2   # path loss exponent

x1 = 0.0   # AP1 x-coordinate
y1 = 0.0   # AP1 y-coordinate
x2 = 15.0  # AP2 x-coordinate
y2 = 0.0   # AP2 y-coordinate
x3 = 0.0   # AP3 x-coordinate
y3 = 15.0  # AP3 y-coordinate

rssi1 = input("Enter rssi of AP1:")
rssi2 = input("Enter rssi of AP2:")
rssi3 = input("Enter rssi of AP3:")

d1 = pow(10, (A - float(rssi1)) / (10 * n))
d2 = pow(10, (A - float(rssi2)) / (10 * n))
d3 = pow(10, (A - float(rssi3)) / (10 * n))
alpha = (d1**2 - d3**2) - (x1**2 - x3**2) - (y1**2 - y3**2)
beta = (d2**2 - d3**2) - (x2**2 - x3**2) - (y2**2 - y3**2)
x31 = 2 * (x3 - x1)
x32 = 2 * (x3 - x2)
y31 = 2 * (y3 - y1)
y32 = 2 * (y3 - y2)

M = [[x31, y31], [x32, y32]]
M1 = [[alpha, y31], [beta, y32]]
M2 = [[x31, alpha], [x32, beta]]
xvalue = np.linalg.det(M1) / np.linalg.det(M)
yvalue = np.linalg.det(M2) / np.linalg.det(M)

plt.title('TRILATERATION')
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.plot(x1, y1, 'bo')
plt.plot(x2, y2, 'bo')
plt.plot(x3, y3, 'bo')
plt.plot(xvalue, yvalue, 'bo')
plt.text(x1, y1, 'AP1', color='r')
plt.text(x2, y2, 'AP2', color='g')
plt.text(x3, y3, 'AP3', color='b')
plt.text(xvalue, yvalue, 'You are here')
plt.plot([x1, xvalue], [y1, yvalue], color='r')
plt.plot([x2, xvalue], [y2, yvalue], color='g')
plt.plot([x3, xvalue], [y3, yvalue], color='b')

circle1 = plt.Circle((x1, y1), d1, fill=False, clip_on=True, color='r')
circle2 = plt.Circle((x2, y2), d2, fill=False, clip_on=True, color='g')
circle3 = plt.Circle((x3, y3), d3, fill=False, clip_on=True, color='b')
fig = plt.gcf()
fig.gca().add_artist(circle1)
fig.gca().add_artist(circle2)
fig.gca().add_artist(circle3)
plt.show()
