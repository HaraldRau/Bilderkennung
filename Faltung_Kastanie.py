import numpy as np

# Input image (8x9)
image = np.array([
  [136,120,112,110,112,118,117,112],
	[183,164,138,125,115,112,114,115],
	[211,200,181,165,143,128,120,116],
	[226,223,213,204,186,162,141,124],
	[224,222,218,218,215,202,181,162],
	[228,227,225,224,222,218,211,203],
	[232,231,225,222,222,221,220,223],
	[231,230,230,229,228,223,219,223]
	])

# Kernel (3x3)
kernel = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
])

# Define convolution function
def convolve2d(image, kernel):
    kernel_size = kernel.shape[0]
    output_size = image.shape[0] - kernel_size + 1
    output = np.zeros((output_size, output_size))

    for i in range(output_size):
        for j in range(output_size):
            region = image[i:i + kernel_size, j:j + kernel_size]
            output[i, j] = np.sum(region * kernel)

    return output

# Perform convolution
feature_map = convolve2d(image, kernel)
print(feature_map)
