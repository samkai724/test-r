from numpy import *
from scipy.stats import norm
a=zeros(100)
b=zeros(100)
for i in range(100):
    c=norm.rvs(0,1,6)
    sum=0
    for j in range(6):
        if c[j]<0:
            b[i]=b[i]+1
        sum+=c[j]
    a[i]=sum/6
print a
print b
