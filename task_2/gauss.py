import matplotlib.pyplot as plt
import numpy as np
import math

def gaussKernel(n, sigma):
    def gaussFunc(x, y):
        return (1 / (2 * math.pi * sigma ** 2)) * math.e ** ((x ** 2 + y ** 2) / (-2 * sigma ** 2))

    kernel = [[gaussFunc(x - n // 2, y - n // 2) for x in range(n)] for y in range(n)]
    kernel = np.array(kernel)
    kernel /= kernel.sum()
    
    print(kernel)

    return kernel

def filter(img, kernel):
    result = np.zeros_like(img)

    p = kernel.shape[0] // 2

    # inflating borders by flipping the image
    infImg = np.vstack([
        np.hstack([img[p::-1, p::-1, :],    img[p::-1, :, :],    img[p::-1, :-p-1:-1, :]]),
        np.hstack([img[:, p::-1, :],        img,                 img[:, :-p-1:-1, :]]),
        np.hstack([img[:-p-1:-1, p::-1, :], img[:-p-1:-1, :, :], img[:-p-1:-1, :-p-1:-1, :]])
    ])

    for k in range(img.shape[2]): # for each color channel
        for i in range(0, img.shape[0]):
            for j in range(0, img.shape[1]):
                window = infImg[i:i+2*p+1, j:j+2*p+1, k]
                result[i, j, k] = (kernel * window).sum()
                
    return result

def main():
    
    img = plt.imread("img.png")[:, :, :3]
    img2 = filter(img, gaussKernel(7, 10))

    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()
