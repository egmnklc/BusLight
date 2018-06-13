import cv2

def recognition():
   cap = cv2.VideoCapture('C:\\Users\\Egemen\\Desktop\\cars.mp4')
   car_cascade = cv2.CascadeClassifier('C:\\Users\\Egemen\\Desktop\\Car Detection\\cars.xml')
   backsub = cv2.createBackgroundSubtractorMOG2(history=2000, varThreshold=16, detectShadows=False)   
   frames = 0
   b = 1
   while True:
      flag, frame = cap.read()
      if flag:
         ret, frame = cap.read()

         if ret:
           fgmask = backsub.apply(frame, None, 0.1)
           im,contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
           try:
               hierarchy = hierarchy[0]
           except:
               hierarchy = []
           for contour, hier in zip(contours, hierarchy):
               (x,y,w,h) = cv2.boundingRect(contour)
               if w > 20 and h > 20:
                   cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                   if x>50 and x<70:
                     with open("lol.txt", "a") as myfile:
                        frames+=1
                        a = str(frames) + "\n"
                        myfile.write(a)                         
                        b+=1
                        print(frames)
                        myfile.close()

           cv2.putText(frame,"# Of Cars: "+str(frames), (220, 20), cv2.FONT_HERSHEY_SIMPLEX,0.6, (0, 0, 0), 2)
           cv2.imshow("Car Recognition", frame)
           gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
           cars = car_cascade.detectMultiScale(gray, 1.1, 3)


                 #press Q on keyboard to exit
           if cv2.waitKey(25) & 0xFF == ord('q'):
                     break
      else:
                 # The next frame is not ready, so we try to read it again
                 # It is better to wait for a while for the next frame to be ready
                 cv2.waitKey(1000)
      if cv2.waitKey(10) == 27:
                 break
recognition()

