#here you place all the layers together
import cv2

def output(back1, back2, back3, back4, back_opt1, back_opt2, mode, counter):
    res = back1[:] #copy the first layer into the resulting image
    #Optional layers
    
    if mode == 'edges':
        cnd = back_opt1[:, :, 3] > 0
        res[cnd] = back_opt1[cnd]
        cnd = back_opt2[:, :, 3] > 0
        res[cnd] = back_opt2[cnd]
    
    #The rest are mandatory layers
    cnd = back2[:, :, 3] > 0
    res[cnd] = back2[cnd]
    cnd = back3[:, :, 3] > 0
    res[cnd] = back3[cnd]
    cnd = back4[:, :, 3] > 0
    res[cnd] = back4[cnd]
    
    if (mode=='threshold'):
        picname='fake_thresholded_%08d.jpg'%(counter)
        #remove printing if you want to create a big dataset
        cv2.imshow('thresholded image',res)
        cv2.imwrite('C:/Users/anna/Desktop/OpenCV_Image_processing/preprocessing/Fake/fake_processed/adaptive_background_results/'+picname,res)
    elif (mode=='edges'):
        picname='fake_edged_%08d.jpg'%(counter)
        cv2.imshow('edged image',res)
        cv2.imwrite('C:/Users/anna/Desktop/OpenCV_Image_processing/preprocessing/Fake/fake_processed/edges_background_results/'+picname,res)
    cv2.waitKey()
    cv2.destroyAllWindows()
