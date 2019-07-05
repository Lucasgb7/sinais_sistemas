import numpy as np
import matplotlib.pyplot as plt

dataset = [1,5,7,8,6,7,8,2,5,2,6,8,2,6,13]

def media_movel(valor, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(valor, weights, 'valid')
    return smas

plt.figure()
plt.title('Filtro media movel')
plt.plot(media_movel(dataset, 3))

# import numpy as np
# import matplotlib as matplotlib  # for plotting
# import matplotlib.pyplot as plt
 
# np.random.seed(17)
# n = 10
# N = 500
# x = np.linspace(0, n, N)
# y0 = -0.05*x**4 + 5*x**2 + 7*x - 6
# yn = 4.5*np.random.standard_normal(N) * np.log10(y0**2 + 0.1)/2
# y = y0 + yn
# # Create a figure canvas and plot the original, noisy data
# fig, ax = plt.subplots()
# ax.plot(x, y, label="Original")
# # Compute moving averages using different window sizes
# window_lst = [3, 6, 10, 16, 22, 35]
# y_avg = np.zeros((len(window_lst) , N))
# for i, window in enumerate(window_lst):
# 	avg_mask = np.ones(window) / window
# 	y_avg[i, :] = np.convolve(y, avg_mask, 'same')
# 	# Plot each running average with an offset of 50
# 	# in order to be able to distinguish them
# 	ax.plot(x, y_avg[i, :] + (i+1)*50, label=window)
# # Add legend to plot
# ax.legend()
# plt.show()