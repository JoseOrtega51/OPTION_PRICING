import numpy as np
import matplotlib.pyplot as plt
import options_lib as ol

###########################

t=np.linspace(0.,1, 100)
x=np.linspace(0.5,1.5,100)

T,X=np.meshgrid(t,x)
S=ol.analytic_price(t=T,x=X,sigma=0.15,r=0.03,T=1.,K=1.)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(T,X,S)

ax.set(xlabel='t',ylabel='S',zlabel='V')

plt.show()

#####################
t=np.linspace(0.,1, 100)
x=np.linspace(0.5,1.2,100)

T,X=np.meshgrid(t,x)

S=ol.up_and_out_call(t=T,x=X,sigma=0.15,r=0.03,T=1.,K=1.,B=1.2)
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(T,X,S)

ax.set(xlabel='t',ylabel='S',zlabel='V')

plt.show()
