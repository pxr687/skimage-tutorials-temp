import numpy as np
import matplotlib.pyplot as plt

def random_colour_array(n_iters, fontsize, figsize =(12, 7)):
    plt.figure(figsize=figsize)
    two_D_ones_and_zeros = np.array([[1, 0,], 
                                     [0, 1,]])
    for i in np.arange(n_iters).astype(int):
        randoms = np.random.uniform(size=3).round(2)

        three_D_stack_array_altered_blend= np.stack([two_D_ones_and_zeros * randoms[0],
                                                     two_D_ones_and_zeros * randoms[1],
                                                     two_D_ones_and_zeros * randoms[2]], 
                                                     axis=2)
        plt.subplot(2, int(n_iters/2), i+1)
        plt.matshow(three_D_stack_array_altered_blend, fignum=0)
        plt.title(f"Blue (X3) = {randoms[2]} \n Green (X2) = {randoms[1]} \n Red (X1) = {randoms[0]}",
                 fontsize=fontsize)
        
def plot_int_float(figsize=(12, 10)):
    plt.figure(figsize=figsize)
    for i in np.arange(6):
        plt.subplot(2, 3, i+1)
        if i <= 2:
            max_intensity_val = 255
            img_arr = np.array([[1, 0,], 
                                [0, 1,]])
            dtype="`uint8` dtype"
            which_channel = np.array([max_intensity_val * (i==0),
                                    max_intensity_val * (i==1),
                                    max_intensity_val * (i==2)])
            plt.matshow(np.stack([img_arr * which_channel[0],
                            img_arr * which_channel[1],
                            img_arr * which_channel[2]], 
                            axis=2),
                            fignum=0)
        else:
            max_intensity_val = 1.0
            img_arr = np.array([[0., 0.],
                                [0., 0.]])
            dtype="`float64` dtype"
            which_channel = np.array([max_intensity_val * (i==3),
                                    max_intensity_val * (i==4),
                                    max_intensity_val * (i==5)])
            
            to_plot = np.stack([img_arr,
                                img_arr, 
                                img_arr], 
                            axis=2)
            to_plot[[0, 1], [0, 1], :] = which_channel
            plt.matshow(to_plot,
                        fignum=0)

        plt.title(f"{dtype}; (Max Intensity = {max_intensity_val})\nRed (X1) = {which_channel[0]}\nGreen (X2) = {which_channel[1]}\nBlue (X3) = {which_channel[2]}");