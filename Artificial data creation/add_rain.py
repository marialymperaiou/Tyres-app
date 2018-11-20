#inserts random spots similar to rain
import numpy as np
import cv2

def generate_random_lines(imshape,slant,drop_length, drop_amount):
    drops=[]
    for i in range(drop_amount): #If You want heavy rain, try increasing this
        if slant<0:
            x= np.random.randint(slant,imshape[1])
        else:
            x= np.random.randint(0,imshape[1]-slant)
        y= np.random.randint(0,imshape[0]-drop_length)
        drops.append((x,y))
    return drops

def add_rain(image, drop_color, drop_length, drop_width, drop_amount, slant_extreme):
    
    imshape = image.shape
    #slant_extreme=10
    slant= np.random.randint(-slant_extreme,slant_extreme) 

    rain_drops= generate_random_lines(imshape,slant,drop_length, drop_amount)
    
    for rain_drop in rain_drops:
        cv2.line(image,(rain_drop[0],rain_drop[1]),(rain_drop[0]+slant,rain_drop[1]+drop_length),drop_color,drop_width)
    return image