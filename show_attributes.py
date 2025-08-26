import numpy as np

def show_attributes(img):
    print("Type:", type(img))
    print("dtype:", img.dtype)
    print("Shape:", img.shape)
    if type(img.max()) != np.bool:
        print("Max Pixel Value:", img.max().round(2))
    else:
        print("Max Pixel Value:", img.max())
    if type(img.min()) != np.bool:
        print("Min Pixel Value:", img.min().round(2))
    else:
        print("Min Pixel Value:", img.min())