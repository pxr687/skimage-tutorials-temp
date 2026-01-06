""" Utilities for displaying graphics
"""
import shutil
from warnings import warn

import numpy as np
import matplotlib.pyplot as plt

import skimage as ski
import sympy as sy


def show_mat(arr, ndigits=2):
    return sy.Matrix(np.round(arr, ndigits))


def save_load_show_mat(arr, img_fname, ndigits=2, dpi=600):
    """ Save math display of `arr` in graphic file

    If we cannot save, load existing file.
    """
    if not shutil.which('latex'):
        warn('No LaTeX installation; cannot save. '
             f'Loading existing file "{img_fname}"')
    else:  # Save image to `img_fname`.
        arr_sym = show_mat(arr, ndigits)
        sy.preview(arr_sym, viewer='file',
                euler=False,
                dvioptions=["-T", "tight", "-z", "0", f"-D {dpi}"],
                filename=img_fname)
    return ski.io.imread(img_fname)

def show_both(original,
              altered,
              alteration='',
	      original_title="Original",
              figsize=(14, 14)):
    """ Display original and altered image side by side.
    """
    plt.figure(figsize=figsize)
    plt.subplot(1, 2, 1)
    plt.title(original_title)
    plt.imshow(original)
    plt.subplot(1, 2, 2)
    plt.title(alteration)
    plt.imshow(altered)
