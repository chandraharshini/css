import numpy as np

# 1-D array
arr_1d = np.array([1, 2, 3])
print(f"1-D Array: {arr_1d}")
print(f"Number of dimensions (ndim): {arr_1d.ndim}")
print(f"Shape: {arr_1d.shape}\n")

# 2-D array
arr_2d = np.array([[1, 2], [3, 4]])
print(f"2-D Array:\n{arr_2d}")
print(f"Number of dimensions (ndim): {arr_2d.ndim}")
print(f"Shape: {arr_2d.shape}\n")

# 3-D array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3-D Array:\n{arr_3d}")
print(f"Number of dimensions (ndim): {arr_3d.ndim}")
print(f"Shape: {arr_3d.shape}")