import numpy as np

a=np.random.normal(size=(10,10))
print("the initial array:\n")
print(a)
b=a<0
a[b]=0
print("The vectorized array:\n")
print(a)
