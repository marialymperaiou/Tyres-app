#Creating the layers of the final image

import cv2
import numpy as np
def create_layers(back1, mode):
    # the background needs to be converted to RGBA colorspace (from RGB)
    b_channel, g_channel, r_channel = cv2.split(back1)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
    back1 = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    
    #create a BGRA image as a "layer" on which we will place letters
    #for our case, we need 2 layers, as we are going to crate a text with borders. 
    #The one layer will be the actual text and the other will actually be the border text
    back2 = np.zeros((499, 750, 4))         #for the border: (height, widht, number of channels). 4 channels to include transparency
    back3 = np.zeros((499, 750, 4))         #for the inner
    back4 = np.zeros((499, 750, 4))         #for the 2nd inner
    #optional layers
    back_opt1 = np.zeros((499, 750, 4))
    back_opt2 = np.zeros((499, 750, 4))
    
    back2[:] = (255,255,255,0)              #better not change this
    back3[:] = (255,255,255,0)  
    back4[:] = (255,255,255,0)
    
    back_opt1[:] = (255,255,255,0)
    back_opt2[:] = (255,255,255,0)
    
    return back1, back2, back3, back4, back_opt1, back_opt2