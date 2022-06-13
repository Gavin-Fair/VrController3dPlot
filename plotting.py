from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


ax = plt.axes(projection='3d')

namefile = 'points.csv'
header1 = "x1_value"
header2 = "y1_value"
header3 = "z1_value"
header4 = "x2_value"
header5 = "y2_value"
header6 = "z2_value"

index = count()


def animate():
    data = pd.read_csv('points.csv')
    x1 = data[header1]
    y1 = data[header2]
    z1 = data[header3]
    x2 = data[header4]
    y2 = data[header5]
    z2 = data[header6]
    plt.cla()
    
    # Red is Controller 1 (Left controller)
    ax.plot3D(x1, y1, z1, 'red')
    
    # Blue is Controller 2 (Right controller)
    ax.plot3D(x2, y2, z2, 'blue')


ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
