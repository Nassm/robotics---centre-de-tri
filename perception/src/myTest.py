#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imageio
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

img = "/home/nassim/pic.jpg"

def get_image_min():
    pic = imageio.imread(img)
    plt.figure(figsize = (15,15))

    #imag = pic.copy()

    grayF = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114])
    gray = grayF(pic)

    #plt.imshow(pic[: , : , 0])
    plt.imshow(pic)
    #plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))

    """
    line = imag.shape[0]
    col = imag.shape[1]
    for i in range(line):
        for j in range(col):
                imag[i][j][0] = (pic[i][j][0] * 0.299)
                imag[i][j][1] = (pic[i][j][0] * 0.587)
                imag[i][j][2] = (pic[i][j][0] * 0.114)
    """
    """
    pic[50:150 , : , 0] =  255
    pic[250:350 , : , 1] =  255
    pic[450:550 , : , 2] =  255
    pic[50:550 , 250:300 , [0,1,2]] =  200
    """

    plt.show() 

    print('Type of the image RGB : {}'.format(pic.shape))
    print('Maximum RGB value in this image RGB {}'.format(pic.max()))
    print('Minimum RGB value in this image RGB {}'.format(pic.min()))
    print('dtype of the image RGB : {}'.format(pic.dtype))

    
    print('Type of the image GRAY {} :'.format(gray.shape))
    print('Maximum RGB value in this image GRAY {}'.format(gray.max()))
    print('Minimum RGB value in this image GRAY {}'.format(gray.min()))
    print('Type of the image GRAY : {}'.format(gray.dtype))
    


    """
    print('Type of the image : \n'.format(pic.shape))
    print('Shape of the image : {}'.format(pic.shape))
    print('dType of the image : {}\n'.format(pic.dtype))
    print('Image Hight {}'.format(pic.shape[0]))
    print('Image Width {}'.format(pic.shape[1]))
    print('Image ndim {}'.format(pic.shape[2]))
    print('Dimension of Image {}'.format(pic.ndim))

    print('Image size {}'.format(pic.size))
    print('Maximum RGB value in this image {}'.format(pic.max()))
    print('Minimum RGB value in this image {}'.format(pic.min()))

    print('Value of pic {}'.format(pic[100, 50]))
    print('Value of only R channel {}'.format(pic[ 100, 50, 0]))
    print('Value of only G channel {}'.format(pic[ 100, 50, 1]))
    print('Value of only B channel {}'.format(pic[ 100, 50, 2]))

    print('RGB  value : {0}, {1}, {2} \n'.format(r, g, b))
    """

get_image_min()
    


    

   
