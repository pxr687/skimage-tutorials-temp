# Generate voxel illustrations (first pass)

# TEMPORARY
import matplotlib.pyplot as plt
import numpy as np

def voxel_illustration(array, 
                       slices=3,
                       azim=160,
                       elev=45):

    switch_slice_off = [1, 0] * slices
    
    to_stack = []
    for i in np.arange(slices*2):
        to_stack.append(array)

    array_for_voxels = np.stack(to_stack,
                      axis=2)

    array_for_voxels  = array_for_voxels  * switch_slice_off

    # and plot everything
    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(array_for_voxels.T,
              facecolor="white",
              edgecolor='black')
    ax.set_xlim([0, int(array.shape[1]*2)])
    ax.set_ylim([0, int(array.shape[1]*2)])
    ax.set_zlim([0, int(array.shape[1]*2)])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.grid(False)
    plt.axis('off')
    ax.view_init(elev=elev, azim=azim)
    plt.show()
    
    
array = np.array([[1, 1,], 
                  [1, 1,]])

voxel_illustration(array, slices=3)