import sys
import cv2

###version
print(cv2.__version__)

#image name as first arg
data=sys.argv[1]

# image read
img=cv2.imread(data,1)
print(img)
print(img.shape)
#width height color channel
cv2.imshow('windowname',img)
cv2.imshow('windowname1' ,img-50)
cv2.imshow('windowname2' ,img+100)
cv2.waitKey(0)		#holding window for infinite tym


img1=cv2.imread(data,0)		#grey image
cv2.imshow('windowname3', img1)

#saving image
cv2.imwrite('img.jpg',img1)