import numpy as np  
import cv2  
img = cv2.imread(r'cat.png',cv2.IMREAD_COLOR)  
#defining points for polylines  
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)  
# pts = pts.reshape((-1,1,2))  
cv2.polylines(img, [pts], True, (0,255,255), 3)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  