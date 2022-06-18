import cv2

def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]* percent/100)
    height=int(frame.shape[0]* percent/100)
    dim=(width, height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

camera=cv2.VideoCapture(0)

while True:
    _,frame=camera.read()
    image=rescale_frame(frame,percent=70)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    faces=face_cascade.detectMultiScale(gray)
    jumlah=str(len(faces))
    
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.rectangle(image,(0,0),(175,30),(255,255,255),-1)
    cv2.putText(image,"Face Detected : "+str(jumlah),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),0)
    cv2.imshow('Face Detection & Counting',image)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()