import pandas as pd 
import numpy as np 

a = np.array([2,3,1,1])
print (a)
q = 0
for i in range(len(a)):
    if a[i] == 1:
        q = q+1;

print(q)