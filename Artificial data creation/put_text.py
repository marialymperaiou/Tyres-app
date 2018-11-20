import cv2
from add_rain import add_rain
from blurring import blurring

def optional(back_opt2, back_opt1, text, coords, font, font_size, text_color_opt2, text_color_opt1, text_thickness_opt2, text_thickness_opt1, line_type_out):
    #Optional outermost layers for canny
    #first outermost
    cv2.putText(back_opt2, text,coords, font, font_size,text_color_opt2,text_thickness_opt2, line_type_out)
    back_opt2 = add_rain(back_opt2, drop_color=(0,0,0,0), drop_length=50,drop_width=50, drop_amount = 100, slant_extreme = 100)
    #back_opt2 = add_rain(back_opt2, drop_color=(0,0,0,0), drop_length=50,drop_width=50, drop_amount = 100, slant_extreme = 300)
    back_opt2 = blurring(back_opt2, av_kernel=2, gauss_kernel=3, blur_kernel=3, median_kernel=5)
    #black layer 'inside' the previous
    cv2.putText(back_opt1, text,coords, font, font_size,text_color_opt1,text_thickness_opt1, line_type_out)
    back_opt1 = add_rain(back_opt1, drop_color=(0,0,0,0), drop_length=50,drop_width=50, drop_amount = 4000, slant_extreme = 10)
    back_opt1 = blurring(back_opt1, av_kernel=2, gauss_kernel=3, blur_kernel=3, median_kernel=5)
    
    return back_opt2, back_opt1

def all_layers(back2, back3, back4, text,coords, font, font_size,text_color_out, text_color,text_color_in, text_thickness_out, text_thickness, text_thickness_in, line_type):
        #first draw the 'border' of the letters       
        cv2.putText(back2, text,coords, font, font_size,text_color_out,text_thickness_out, line_type)
        #add random white spots like rain. You can play with the parameters
        back2 = add_rain(back2, drop_color=(0,0,0,0), drop_length=5,drop_width=5, drop_amount = 3000, slant_extreme = 10)
        #blur the result
        back2 = blurring(back2, av_kernel=2, gauss_kernel=3, blur_kernel=3, median_kernel=5)  
              
        #now put the 'inside' of the letters
        cv2.putText(back3, text,coords, font, font_size,text_color,text_thickness, line_type)  
        back3 = add_rain(back3, drop_color=(255,255,255,0), drop_length=5,drop_width=5, drop_amount = 1500, slant_extreme = 10)  
        back3 = blurring(back3, av_kernel=2, gauss_kernel=3, blur_kernel=3, median_kernel=5)  
        
        #and last, the innermost layer
        #ATTENTION! This layer may be useful only for canny transformation. In case you use
        #thresholding, depending on the case, this layer may be unecessary. To make your life 
        #easier, you can just put the colors of the layer no 3!
        cv2.putText(back4, text,coords, font, font_size,text_color_in,text_thickness_in, line_type)  
        back4 = add_rain(back4, drop_color=(0,0,0,0), drop_length=4,drop_width=5, drop_amount = 1500, slant_extreme = 10) 
        back4 = blurring(back4, av_kernel=2, gauss_kernel=3, blur_kernel=3, median_kernel=5) 
        
        return back2, back3, back4
