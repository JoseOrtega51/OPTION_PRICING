import numpy as np
import matplotlib.pyplot as plt
import options_lib as ol
from scipy.stats import norm

S,V,W=np.loadtxt("final_time_price.txt",unpack=True)

print(len(S[S>10000]))
print(np.where(S>10000))

x=np.linspace(0.01,np.max(S),100)

TIPO=1          #1-call europea   2- up and out call
S0=1.           #Precio inicial del subyacente
K=S0            #strike
r=0.03          #risk-free rate
sigma=0.15      #volatility
t=1.            #final time
B=1.2           #barrien


plt.hist(S,bins=round(np.sqrt(len(S))),density=True, label="Montecarlo histogram")
plt.plot(x,ol.lognormal(x,np.log(S0)+(r-0.5*sigma**2)*t,sigma*np.sqrt(t)),linewidth=3, label="Density function")
plt.legend()
plt.xlabel("S(T)")
plt.ylabel("frequency")
plt.show()

plt.hist(V,bins=100,density=True)
plt.xlabel("Option price")
plt.ylabel("frequency")
plt.show()

precio=np.exp(-r*t)*np.mean(V)
if(TIPO==1):
    precio_analytic=ol.euro_call(0,S0,sigma,r,t,K)
elif(TIPO==2):
    precio_analytic=ol.up_and_out_call(0,S0,sigma,r,t,K,B)

print("Montecarlo price", precio)
print("Analytic price",precio_analytic)