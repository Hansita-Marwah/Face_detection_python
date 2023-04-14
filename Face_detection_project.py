import cv2

# STEP 2
face_cap = cv2.CascadeClassifier("C:/Users/v-hmarwah/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# STEP 1

video_cap = cv2.VideoCapture(0)
# for enabling camera through cv2 module in cv library
while(True): # infinite loop for enabling camera until any key
    #is pressed
    ret , video_data = video_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    
    #2
    # faces has the face detection code according to various dimensions
    
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        # w - width, h - height
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
        # video_data contains the video_cap.read()
        # the data must be shown along with the width and height so x + w, x + h
        #0,255,0 contains the color 
        # rectangle is the function used to make the rectangle
        
    # images are being read
    cv2.imshow("video_live",video_data)
    # camera will open with the name of video_live
    # showing video in variable video_data
    if cv2.waitKey(10) == ord("a"):
        # when "a" is pressed then the video will stop
        # but the tab remains open so we hv to cross it
        # to close it 
        break
video_cap.release()
#release is a function in cv2

        
