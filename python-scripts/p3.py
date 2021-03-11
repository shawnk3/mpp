import timeit
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dy_dx(y,x):
	return x - y

xs = np.linspace(0,5,100)
y0 = 1.0
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()



solvingResult = timeit.timeit(

	globals= globals(), 
	setup= 'y0 = 1.0, xs = np.linspace(0,5,100)',
	stmt= 'ys = odeint(dy_dx,y0,xs) ',
	number= 100000,
	timer= time.perf_counter

)



flatteningResult = timeit.timeit(

        globals= globals(),
        setup= 'ys = odeint(dy_dx, y0, xs)',
        stmt= 'np.array(ys).flatten()',
        number= 100000,
        timer= time.perf_counter
)

print(solvingResult)
print(flatteningResult)
