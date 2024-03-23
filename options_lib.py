import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def lognormal(x,mu,sigma):
    return(1/x/sigma/np.sqrt(2*np.pi)*np.exp(-((np.log(x)-mu)**2)/2/sigma**2))

def euro_call(t,x,sigma,r,T,K):
    tau=T-t
    dp=1/sigma/np.sqrt(tau)*(np.log(x/K)+(r+sigma**2/2)*tau)
    dm=1/sigma/np.sqrt(tau)*(np.log(x/K)+(r-sigma**2/2)*tau)
    return(x*norm.cdf(dp)-K*np.exp(-r*tau)*norm.cdf(dm))

def delta_p(tau,s,r,sigma):
    return(1/sigma/np.sqrt(tau)*(np.log(s)+(r+0.5*sigma**2)*tau))

def delta_m(tau,s,r,sigma):
    return(1/sigma/np.sqrt(tau)*(np.log(s)+(r-0.5*sigma**2)*tau))

def up_and_out_call(t,x,sigma,r,T,K,B):
    tau=T-t
    dp1=delta_p(tau,x/K,r,sigma)
    dp2=delta_p(tau,x/B,r,sigma)
    dp3=delta_p(tau,B**2/K/x,r,sigma)
    dp4=delta_p(tau,B/x,r,sigma)

    dm1=delta_m(tau,x/K,r,sigma)
    dm2=delta_m(tau,x/B,r,sigma)
    dm3=delta_m(tau,B**2/K/x,r,sigma)
    dm4=delta_m(tau,B/x,r,sigma)

    return(\
    x*(norm.cdf(dp1)-norm.cdf(dp2))-\
    np.exp(-r*tau)*K*(norm.cdf(dm1)-norm.cdf(dm2))-\
    B*(x/B)**(-2*r/(sigma**2))*(norm.cdf(dp3)-norm.cdf(dp4))+\
    np.exp(-r*tau)*K*(x/B)**(-2*r/(sigma**2)+1)*(norm.cdf(dm3)-norm.cdf(dm4))\
    )
