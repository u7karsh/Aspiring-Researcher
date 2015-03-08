import numpy as np
import cv2
import glob
import os
os.chdir(".")
default_save_dir = 'processed/'

if not os.path.exists(default_save_dir):
    os.makedirs(default_save_dir)
    
##mouse callback function
mode = 1
drawing = False # true if mouse is pressed
def update_mask(event,x,y,flags,param):
    global drawing,mask,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        mask[y,x] = mode
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            mask[y,x] = mode
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
            

##height and width margin in percentages!
height_margin = 10.0
width_margin = 10.0

##setup mouse callback function
cv2.namedWindow("Original Image")
cv2.setMouseCallback("Original Image", update_mask)

for file in glob.glob("*.jpg"):

    print 'Processing image ' + file
    
    ##satisfaction flag
    satisfied = False

    ##init flag
    init = 0

    #read the image
    img = cv2.imread(file)

    #compute the size of image
    height, width = img.shape[:2]

    ##mask for grab cut algo
    mask = np.zeros((height, width),np.uint8)

    ##auto bounding box generation
    rect = (int((width_margin/200)*width),int((height_margin/200)*height),int(width-(width_margin/100)*width-1),int(height-(height_margin/100)*height-1))

    while not(satisfied):
            
        ###grab cut algorithm
        if init == 0:
            bgdModel = np.zeros((1,65),np.float64)
            fgdModel = np.zeros((1,65),np.float64)
            cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
            init = 1
        else:
            cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

        ##mask out the image
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        foreground = img*mask2[:,:,np.newaxis]

        ##display the output
        cv2.imshow("Foreground", foreground)
        cv2.imshow("Original Image", img)

        ##poll untill user inputs 'y' or 'n' key
        while True:
            key = cv2.waitKey(1)
            if (key == ord('y') or key == ord('Y')):
                satisfied = True
                print 'Saving output..'
                cv2.imwrite(default_save_dir + file, foreground)
                break
            elif (key == ord('n') or key == ord('N')):
                satisfied = False
                break
            ###caution.. use this command wisely..
            elif (key == ord('r') or key == ord('R')):  ###reset mask
                print 'Resetting the mask..'
                mask = np.zeros((height, width),np.uint8)
            ##foreground selection tool
            elif (key == ord('f') or key == ord('F')):
                mode = 1
            ##background selection tool
            elif (key == ord('b') or key == ord('B')):
                mode = 0

cv2.destroyAllWindows()

