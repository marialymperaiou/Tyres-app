#define the parameters of the letters on the tires

#Recommendations: 
#For adaptive thresholding mode choose white outer text and black inner - intermediate text.
#The innermost layer can be 'absent' -> same color as the inner - intermediate.
#Ideal thickness is 2 or 3 for the inner - intermediate, and 7 for the outer.

#For canny edge detection mode choose:
#white for the innermost text of thickness 1
#black inner - intermediate text of thickness 4 and 
#outer with white color and thickness 8 or more.

import cv2
import string
import random

def input_data():
    #generate the string on the tire
    txt = []                #random characters are stored here
    lenght = 8              #we assume that tire strings have 8 characters, which is the most usual case.
    for i in range(lenght):
        rand = random.choice(string.ascii_uppercase + string.digits)
        txt.append(rand)
        text = ''.join(txt)
    print(text)
    
    coords = (200,230)                  #at this place the text is going to start
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #Innermost text
    #It is possible that this layer is useful only to imitate the canny transformation,
    #and maybe in the thresholding mode it is not necessary.
    #If you use thresholding, check to easily 'remove' this layer by assigning
    #text_color_in = text_color

    font_size = 2.5                     #be careful to have the same size as the outer layers!
    text_color_in = (255,255,255,255)   #thresholding hint: text_color_in = text_color    
    text_thickness_in = 1                  
    line_type_in = cv2.LINE_AA
    
    #2nd Inner text

    #font_size = 2.5                     #be careful to have the same size as the outer text!
    text_color = (0,0,0,50)             #define inner text color and transparency    
    text_thickness = 4                  #normally, the thickness should be smaller than the outside text
    line_type = cv2.LINE_AA
    
    #Outer text/border
    text_color_out = (255,255,255,255) 
    text_thickness_out = 8
    line_type_out = cv2.LINE_AA
    
    #Optional layers
    #For improvement of the canny method
    #if you use thresholding mode, put those black
    #First optional layer
    text_color_opt1 = (0,0,0,255) 
    text_thickness_opt1 = 10
    
    #Second optional layer, outermost
    text_color_opt2 = (255,255,255,255) 
    text_thickness_opt2 = 11
    
    return text, coords, font, font_size, text_color, text_thickness, line_type, text_color_out, text_thickness_out, line_type_out, text_color_in, text_thickness_in, line_type_in, text_color_opt1, text_thickness_opt1, text_color_opt2, text_thickness_opt2 