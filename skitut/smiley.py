import numpy as np
import matplotlib.pyplot as plt

def create_smiley():
    smiley = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 1, 0],
                       [0, 1, 1, 0, 0, 1, 1, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]])

    plt.matshow(smiley,
          cmap="gray")
    plt.xticks(np.arange(smiley.shape[1]))
    plt.yticks(np.arange(smiley.shape[0]))