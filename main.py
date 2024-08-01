import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
hand_detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    # Detect hands in the image
    hand , img = hand_detector.findHands(img)

    cv2.rectangle(img,(100,100),(200,200),(255,0,255),cv2.FILLED)
    cv2.putText(img,'Q',(115,180),cv2.FONT_HERSHEY_DUPLEX,5,(255,255,255),5)
     # Display the image
    cv2.imshow("Hand Detection", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
