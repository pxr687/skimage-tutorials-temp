""" Utilities for displaying graphics
"""
import shutil
from warnings import warn

import numpy as np
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
