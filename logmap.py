import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)


n = 100000
r = np.linspace(2.5, 4.0, n)

iterations = 1000
last = 100

x = 1e-5 * np.ones(n)

fig, ax = plt.subplots(1, 1, figsize=(15, 9))# sharex=True, sharey=True)

for i in range(iterations):
    x = logistic(r, x)
    if i >= (iterations - last):
        ax.plot(r, x, ',c', alpha=.25)
        #use the below command to ignore marker and get a vector line graph
        #it has vertical lines connecting branches of each bifurcation
        #but the effect of change in r is more profound
        #if possible use jupyter notebook and qt backend for best result
        #ax.plot(r, x, 'c', alpha=.25)

ax.set_xlim(2.5, 4)
ax.set_title("Bifurcation diagram")
