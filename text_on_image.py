import numpy as np  
import cv2  
font = cv2.FONT_HERSHEY_SIMPLEX  
# Create a black image.  
img = cv2.imread(r"cat.png",1)  
cv2.putText(img,'Hack Projects',(10,500), font, 1,(255,255,255),2)  
#Display the image  
cv2.imshow("image",img)  
cv2.waitKey(0)