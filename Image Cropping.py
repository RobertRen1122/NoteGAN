import cv2
import numpy as np

image = cv2.imread('test.jpeg')
height = image.shape[0]
array = [['I', '183', '298', '300', '489', '0'], ['l', '501', '291', '525', '497', '0'], ['o', '555', '297', '616', '377', '0'], ['v', '639', '306', '703', '387', '0'], ['e', '704', '285', '786', '385', '0'], ['u', '918', '295', '988', '380', '0']]
for i in range(0, len(array)):
    x1 = height - int(array[i][4])
    y1 = height - int(array[i][2])
    x2 = int(array[i][1])
    y2 = int(array[i][3])
    cropped_image = image[x1:y1, x2:y2] # [height - [4] : height - [2], [1] : [3]]
    cv2.imshow("cropped", cropped_image)
    name = "Cropped Image" + str(i) + ".jpeg"
    cv2.imwrite(name, cropped_image)



