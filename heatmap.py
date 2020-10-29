import numpy,seaborn,matplotlib.pyplot 
seaborn.set()
seaborn.heatmap(numpy.loadtxt('result.txt'),cmap="RdBu_r",\
vmin=-1500,vmax=5000,center=1000	) 
matplotlib.pyplot.show()