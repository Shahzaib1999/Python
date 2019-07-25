import numpy as np
import matplotlib.pyplot as plt
import  random 
x=np.linspace(-4,4,9)
y=np.linspace(-5,5,11)
#print(x)
#print(y)
xx,yy=np.meshgrid(x,y)
#print(yy)
#ellipse=xx**2.0+4.0*yy**2.0
rand=np.random.random_sample((11, 9))
plt.contourf(xx,yy,rand,cmap="jet")
plt.colorbar()
plt.show()



