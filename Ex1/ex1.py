from cv2 import bitwise_not, equalizeHist, hconcat, vconcat
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

# Task 1


def t1():
    img = cv.imread("mammogram.tif")
    # Generate the negative image
    negative_img = cv.bitwise_not(img)
    # Combine the images into 1
    img_combined = cv.hconcat([img, negative_img])
    # Display the images
    cv.imshow("Image v Negative Image", img_combined)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Task 2


def t2():
    img = cv.imread("pollen.tif", cv.COLOR_BGR2GRAY)
    # Convert image to grayscale 
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # histogram equalization
    eq_hist = equalizeHist(img)
    # this ends up being unused because matplot can do that on its own
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    # cv.imshow('Task 2',img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    fig, ax = plt.subplots(2, 2, figsize=(6, 6))
    ax[0, 0].imshow(img)
    ax[1, 0].hist(img.ravel(), 256, (0, 256))
    ax[1, 0].set_xlim(0, 250)
    ax[0, 1].imshow(eq_hist)
    ax[1, 1].hist(eq_hist.ravel(), 256, (0, 256))
    ax[1, 1].set_xlim(0, 250)
    plt.show()



# Task 3
def t3():
    # Load image
    img = cv.imread("pollen.tif", cv.COLOR_BGR2GRAY)
    # Find specific region in image
    region = find_region(img,1,200,200,500)
    # Combine specific region with whole image
    img_combined = hconcat(img,region)
    # Display the image
    cv.imshow("Image v Region",img_combined)
    # cv.imshow("Region",region)
    cv.waitKey(0)
    cv.destroyAllWindows()

def find_region(image,row_1,row_2,col_1,col_2):
    area = image[row_1:row_2,col_1:col_2]
    return area

if "__main__" == __name__:
    t3()
