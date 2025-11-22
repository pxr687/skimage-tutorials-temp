import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Adapted from: https://www.geeksforgeeks.org/python/how-to-generate-2-d-gaussian-array-using-numpy
def make_gaussian_kernel(kernel_size=17,
                    sigma=1,
                    muu=0,
                    axis_bins=8,
                    figsize=(8, 18),
                    plot_contour=False,
                    plot_3D=False):
    
    x_lin = np.linspace(-3, 3, kernel_size)
    y_lin = x_lin.copy()
    x, y = np.meshgrid(x_lin,
                       y_lin)
    dst = np.sqrt(x**2 + y**2)

    normal = 1 / (2 * np.pi * sigma**2)

    gauss = np.exp(-((dst - muu)**2 / (2.0 * sigma**2))) * normal

    gauss = 1/gauss.sum() * gauss
    
    if plot_contour == True:
        plt.figure()
        plt.contour(gauss)
        plt.xlabel('Integer Index \n`axis = 0`')
        plt.ylabel('Integer Index \n`axis = 1`')
        
    if plot_3D == True:

        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_wireframe(x, y, gauss, color='red')
        ax.set_xticks(np.linspace(x_lin.min(), x_lin.max(), gauss.shape[0]))
        ax.set_yticks(np.linspace(y_lin.min(), y_lin.max(), gauss.shape[1]))
        ax.set_xticklabels(np.arange(0, gauss.shape[0]))
        ax.set_yticklabels(np.arange(0, gauss.shape[1]))
        ax.set_xlabel('Integer Index \n`axis = 0`')
        ax.set_ylabel('Integer Index \n`axis = 1`')
        ax.set_zlabel('Kernel Element Value', labelpad=2)
        plt.locator_params(axis='x', nbins=axis_bins)
        plt.locator_params(axis='y', nbins=axis_bins)

    return gauss

def generate_illustration(var=0.5):
    x = np.linspace(0, 2, 100)
    y = np.linspace(0, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = 0.25 * np.exp(-((X - 1)**2 / (2 * var**2) + (Y - 1)**2 / (2 * var**2)))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, color='red')
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.set_zticks([])