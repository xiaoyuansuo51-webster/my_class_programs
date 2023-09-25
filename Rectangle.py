import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
image = cv.line(img,(0,0),(511,511),(255,0,0),5)

image = cv.circle(img,(447,63), 63, (0,0,255), -1)
cv.imshow('circle', image)

image = cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv.imshow('rectangle', image)

image = cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv.imshow('ellipse', image)

font = cv.FONT_HERSHEY_SIMPLEX
image = cv.putText(img,'Xiaoyuan Suo',(10,500),
                   font, 4,(255,255,255),2,cv.LINE_AA)
cv.imshow('text', image)

cv.waitKey(0)

# Window shown waits for any key pressing event
cv.destroyAllWindows()