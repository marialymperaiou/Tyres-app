#choose the type of blurring and the parameters that the letters will have
import cv2
import numpy as np

def blurring(image, av_kernel=2, gauss_kernel=3, blur_kernel=3, median_kernel=5):
    #average filter
    kernel = np.ones((av_kernel,av_kernel),np.float32)/(av_kernel*av_kernel)
    image = cv2.filter2D(image,-1,kernel) 
    
    #gaussian filter
    #image = cv2.GaussianBlur(image,(gauss_kernel,gauss_kernel),0) 
    
    #blur
    #image = cv2.blur(image,(blur_kernel,blur_kernel))
    
    #median
    #image = cv2.medianBlur(image,median_kernel)
    return image