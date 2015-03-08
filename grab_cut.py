import numpy as np
import cv2

##height and width margin in percentages!
height_margin = 10.0
width_margin = 10.0

#read the image
img = cv2.imread('messi5.jpg')

#compute the size of image
height, width = img.shape[:2]

##mask for grab cut algo
mask = np.zeros((height, width),np.uint8)

##auto bounding box generation
rect = (int((width_margin/200)*width),int((height_margin/200)*height),int(width-(width_margin/100)*width-1),int(height-(height_margin/100)*height-1))

###grab cut algorithm
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

##mask out the image
img = img*mask2[:,:,np.newaxis]

##display the output
cv2.imshow("out", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

