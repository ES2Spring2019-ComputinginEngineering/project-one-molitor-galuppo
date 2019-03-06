import numpy as np
x  = np.linspace(0,20,201)
y = x * x

for i in range(len(x)):
    print( (x[i], y[i]))
