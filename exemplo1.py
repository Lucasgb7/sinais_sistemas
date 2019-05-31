from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import math
import numpy as np

# def plotaGrafico(x, y):
# 	plt.plot(x, y, 'ro')
# 	plt.axis([-5, 5, -15, 15])
# 	plt.ylabel('Modulo Z(W)')
# 	plt.xlabel('Magnitude (W)')
# 	plt.show()

# def extraiModulo(real, imaginario, magnitude):
# 	if magnitude:   
# 		return math.sqrt(real ** 2 + (imaginario * magnitude) ** 2)

# 	return math.sqrt((real)**2 + (imaginario)**2)

# w = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# a = 2
# b = 2
# modulo = []
# for i in w:
# 	modulo.append(extraiModulo(a, b, i))
# plotaGrafico(w, modulo)
#data generation
x = np.arange(-10,20,0.2)
y = 1.0/(1.0+np.exp(-x)) # nunpy does the calculation elementwise for you

fig, [ax0, ax1] = plt.subplots(ncols=2, figsize=(8,4))

# Eliminate upper and right axes
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
# Show ticks on the left and lower axes only
ax0.xaxis.set_tick_params(bottom='on', top='off')
ax0.yaxis.set_tick_params(left='on', right='off')

# Move remaining spines to the center
ax0.set_title('center')
ax0.spines['bottom'].set_position('center') # spine for xaxis 
#    - will pass through the center of the y-values (which is 0)
ax0.spines['left'].set_position('center')  # spine for yaxis 
#    - will pass through the center of the x-values (which is 5)

ax0.plot(x,y)


# Eliminate upper and right axes
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
# Show ticks on the left and lower axes only (and let them protrude in both directions)
ax1.xaxis.set_tick_params(bottom='on', top='off', direction='inout')
ax1.yaxis.set_tick_params(left='on', right='off', direction='inout')

# Make spines pass through zero of the other axis
ax1.set_title('zero')
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')

ax1.set_ylim(-0.4,1.0)

# No ticklabels at zero
ax1.set_xticks([-10,-5,5,10,15,20])
ax1.set_yticks([-0.4,-0.2,0.2,0.4,0.6,0.8,1.0])

ax1.plot(x,y)

plt.show() 