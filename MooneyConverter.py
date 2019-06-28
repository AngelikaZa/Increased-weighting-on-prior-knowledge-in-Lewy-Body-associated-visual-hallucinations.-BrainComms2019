""""
Converts images to two-tone Mooney images
Author: A. Zarkali
Date: 10th September 2018
"""

import cv2
import numpy as np
import os, os.path

template_path = r"<PATH_TO_FILES>"
size = (500, 500)

templateImgs = []
files = os.listdir(template_path)
for f in range(len(files)):
    templateImgs.append(os.path.join(template_path, files[f]))

#Threshold image
def apply_threshold(img, argument):
    switcher = {
        1: cv2.threshold(cv2.GaussianBlur(img, (9, 9), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        2: cv2.threshold(cv2.GaussianBlur(img, (7, 7), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        3: cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
    }
    return switcher.get(argument, "Invalid method")

def mooneyImage(path, method):
    img = cv2.imread(path)
    file_name = os.path.basename(path).split('.')[0]
    file_name = file_name.split()[0]
    print(path)

    img = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
    img = cv2. cvtColor(img, cv2.COLOR_RGB2GRAY)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    img = apply_threshold(img, method)

    save_path = os.path.join(file_name + "_filter_" + str(method) + ".jpg")
    cv2.imwrite(save_path, img)

for i in range(len(templateImgs)):
    mooneyImage(templateImgs[i],1)
