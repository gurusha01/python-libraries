import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-2.0*np.pi, 2.0*np.pi, 201)
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,color='r',label='sin')
plt.plot(x,z,color='g',label='cos')
plt.axes().spines['bottom'].set_position(('data',0))
plt.axes().spines['left'].set_position(('data',0))
plt.axhline(y=plt.ylim()[0],color='black')
plt.axvline(x=plt.xlim()[0],color='black')
plt.title('plot of sine and cosine')
plt.xlabel('angle')
plt.ylabel('magnitude')
plt.legend()
plt.grid()
plt.show()
