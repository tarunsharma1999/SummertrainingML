import cv2

cap=cv2.VideoCapture(0)
print(cap.isOpened())


#adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
#saving video
output=cv2.VideoWriter('class.mp4',plugin,20,(640,480))


#now we can read input from camera
#print(cap.read())		#it will take first picture

#status,img=cap.read()
#status1,img1=cap.read()

#now showing
#cv2.imshow('liveimage',img)
#cv2.imshow('liveimage',img1)

##
while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow('live',frame)
	output.write(frame)
	if cv2.waitKey(10) & 0xff == ord('q') :
		break
cv2.destroyAllWindows()
cap.release()
