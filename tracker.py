import cv2

tracker_types=["BOOSTING","MIL","KCF","TLD","MEDIANFLOW","GOTURN"]
choose=tracker_types[4]

if choose=="BOOSTING":
	tracker=cv2.TrackerBoosting_create()
if choose=="MIL":
	tracker=cv2.TrackerMIL_create()
if choose=="KCF":
	tracker=cv2.TrackerKCF_create()
if choose=="TLD":
	tracker=cv2.TrackerTLD_create()
if choose=="MEDIANFLOW":
	tracker=cv2.TrackerMedianFlow_create()
if choose=="GOTURN":
	tracker=cv2.TrackerGOTURN_create()

cap=cv2.VideoCapture(0)
ret,frame=cap.read()


bbox=cv2.selectROI(frame,False)
ret=tracker.init(frame,bbox)

while(True):
	ret,frame=cap.read()
	ret,newbox=tracker.update(frame)

	x=(int(newbox[0]),int(newbox[1]))
	y=(int(newbox[0]+newbox[2]),int(newbox[1]+newbox[3]))
	cv2.rectangle(frame,x,y,(0,0,255),2,1)

	cv2.imshow("video",frame)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break;

cap.release()
cv2.destroyAllWindows()