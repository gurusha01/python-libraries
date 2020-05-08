import matplotlib.pyplot as plt
import random
from itertools import count
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation

x=[]
y=[]

def animate(i):
    x.append(i/50)
    y.append(np.sin(i/50))
    plt.plot(x,y, color='red')
    
ani=FuncAnimation(plt.gcf(), animate, interval=10)
plt.tight_layout()
plt.show()
              
