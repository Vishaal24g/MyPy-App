#PLOT PROGRAM
import matplotlib.pyplot as pl
import numpy as np

print("What kind of graph would you like to plot?")
print("Enter 1 for Line Graph")
print("Enter 2 for Bar Graph")
print("Enter 3 for Pie Chart")
print("Enter 4 for Histogram")
print("Enter 5 for Scatter Chart")

resp = int(input("Enter your choice: "))

print("Enter your values for the graph")
X = np.arange(5)
Y = eval(input("Enter any five values for X-Axis: "))
Z = eval(input("Enter any five values for Y-Axis:"))

if resp == 1:
    pl.xlabel("X-Axis")
    pl.ylabel("Y-Axis")
    pl.title("Line Chart")
    pl.plot(X, Y, marker = 'o', markeredgecolor = 'red', label = 'Line A', linewidth = 3, linestyle = 'dashdot')
    pl.plot(X, Z, marker = 'o', markeredgecolor = 'green', label = 'Line B', linewidth = 3, linestyle = 'dashed')
    pl.legend()
    pl.grid("True", color = 'yellow')
    pl.show()
elif resp == 2:
    pl.bar(Y, Z, width = [0.6,0.7,0.8,0.9,1], color = ('red','blue','green','purple','orange'))
    pl.xlabel('X-Axis')
    pl.ylabel('Y-Axis')
    pl.title('Bar Graph')
    pl.show(Y,Z)
elif resp == 3:
    exp = [0,0.2,0.3,0,0.1]
    pl.pie(Y, colors = ['magenta','cyan','green','red','blue'], startangle = 90, explode = exp, shadow = True, autopct = '%.1f%%')
    pl.title('Pie Chart')
    pl.show()
elif resp == 4:
    pl.hist([Y,Z],bins = [20,25,30,35], color = ['green','orange'], rwidth = 0.95, histtype = "barstacked", orientation = "horizontal")
    pl.xlabel("Y-Axis")
    pl.ylabel("X-Axis")
    pl.title("Histogram")
elif resp == 5:
    pl.scatter(Y, Z, c = ['r','g','b','purple','cyan'], s = 20)
    pl.xlabel("X-Axis")
    pl.ylabel("Y-Axis")
    pl.title("Scatter Chart")
    pl.show(Y,Z)
elif resp > 5:
    print("Invalid input")
