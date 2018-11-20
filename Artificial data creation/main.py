#main

"""
Artificial image creation to represent processed (adaptive thresholding, canny edge detection) 
tire images. Create random characters of certain length and overlap them on existing
backgrounds. Tune the parameters to achieve more realistic results.
"""
import cv2
from input_data import input_data
import os
from output import output
from create_layers import create_layers
from put_text import optional, all_layers

counter = 0
n_text = 100                    #how many times you want the whole procedure to be repeated
mode = 'edges'                  #alternative modes = 'edges' or 'threshold'  
#for adaptive thresholding images
path1 = 'C:/Users/anna/Desktop/OpenCV_Image_processing/preprocessing/backgrounds/thresholded_backgrounds/'

#for canny edge detection images
path2 = 'C:/Users/anna/Desktop/OpenCV_Image_processing/preprocessing/backgrounds/edge_backgrounds_2/'

if mode == 'threshold':
    path = path1
elif mode == 'edges':
    path = path2
    
for i in range(n_text):
    for filename1 in os.listdir(path): 
        counter+=1
        back1= cv2.imread(path+filename1)
        
        #create layers
        back1, back2, back3, back4, back_opt1, back_opt2 = create_layers(back1, mode)
        
        #give input
        text, coords, font, font_size, text_color, text_thickness, line_type, text_color_out, text_thickness_out, line_type_out, text_color_in, text_thickness_in, line_type_in, text_color_opt1, text_thickness_opt1, text_color_opt2, text_thickness_opt2 = input_data()
        
        #optional layer for canny edge detection
        back_opt2, back_opt1 = optional(back_opt2, back_opt1, text, coords, font, font_size, text_color_opt2, text_color_opt1, text_thickness_opt2, text_thickness_opt1, line_type_out)
        
        #the 3 layers for both processes
        back2, back3, back4 = all_layers(back2, back3, back4, text,coords, font, font_size,text_color_out, text_color,text_color_in, text_thickness_out, text_thickness, text_thickness_in, line_type)
    
        #do not forget to remove printing in 'output.py' if you want to produce 
        #a big amount of images!
        output(back1, back2, back3, back4, back_opt1, back_opt2, mode, counter)