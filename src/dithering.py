"""
Unicamp - 13/04/2022
Author: André Igor Nóbrega da Silva
email: a203758@dac.unicamp.br
Simple dithering exercise, as part of Introduction to Digital Image Processing Course.
6 dithering masks techniques where implemented:
    - a) Floyd and Steinberg
    - b) Stevenson and Acre
    - c) Burkes
    - d) Sierra
    - e) Stucki
    - f) Jarvis, Judice and Ninke
"""

import sys
import time

import cv2

from masks import *
from utils import *

class InputParameterError(Exception):
    "Raised when input parameter is not as expected"
    pass

def main():
    # input parameters
    if len(sys.argv) != 5:
        message = 'Error in dithering.py:\n '
        message += '<P1> <P2> <P3> <P4> \n'
        message += 'P1: Input image\nP2: Dithering Mask.\n'
        message += '\t- floyd_steinberg\n \t- stevenson\n \t- burkes\n \t- sierra\n \t- stucki\n \t- jarvis_judice_ninke\n'
        message += 'P3: Sweeping method.\n\t- uniform\n\t- zigzag\nP4: Output image'
        raise InputParameterError(message)
    tic = time.time()

    # reading image and transforming it to hsv
    input_image = cv2.imread(sys.argv[1])
    hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

    # reading input masks
    mask = get_chosen_mask(sys.argv[2])

    # acessing only the "value" (luminance) of hsv image
    f = hsv_image[:,:,2].copy() # input luminance
    output_image = f.copy()

    # dithering algorithm
    for x in range(f.shape[0]):
        dithering_direction = get_dithering_direction(x, sys.argv[3]) # the direction of dithering matters. Therefore, we change it depending on the row
        for y in range(f.shape[1]):
            i, j = get_index_from_direction(f, x, y, dithering_direction) # changing the matrix index given the direction
            output_image[i,j] = calculate_new_image_value(f, i, j) # simple threshold in the output image
            error = calculate_error(f, output_image, i, j) # calculating error
            difuse_error(f, error, mask, dithering_direction,  i, j) # difusing the calculated error accordingly to the mask
    
    toc = time.time()
    print('Dithering algorithm finished with sucess in {:.2f}s'.format(toc - tic))

    # rebuild hsv image and transform it to rgb
    hsv_output_image = hsv_image.copy()
    hsv_output_image[:,:,2] = output_image * 255
    rgb_output_image = cv2.cvtColor(hsv_output_image, cv2.COLOR_HSV2BGR)

    # saving output rgb image
    print("Saving output image as {}".format('../outputs/' + sys.argv[4]))
    cv2.imwrite('../outputs/' + sys.argv[4], rgb_output_image)

if __name__ == '__main__':
    main()