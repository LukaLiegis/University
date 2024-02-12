import matplotlib.pyplot as plt
import numpy as np
smile=float(input('How would you describe your mood on a scale of 1-10?\n'))
mood = str(input('How would you describe your mood in one word?\n'))
x=np.linspace(0,2*np.pi,1000)
y=np.linspace(-0.5,0.5,1000)
plt.title(mood)
plt.plot(np.cos(x),np.sin(x),color='blue') # head
plt.plot(y,(smile-5)*0.4*(y**2)-0.45,linewidth=2,color='blue') # mouth
plt.plot([-0.4,0.4],[0.45,0.45],'o',markersize=8,color='g') #eyes
plt.axis('equal')
plt.show()