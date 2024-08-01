import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
hand_detector = HandDetector(detectionCon=0.8)


class Button():
    def __init__(self, pos, text, size=[95,95]):
        self.pos = pos
        self.size = size
        self.text = text

    def draw(self, img):
        x,y=self.pos
        w,h=self.size
        cv2.rectangle(img, self.pos, (x+w,y+h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, self.text, (self.pos[0] + 15, self.pos[1] + 75), cv2.FONT_HERSHEY_DUPLEX, 3, (255, 255, 255),
                    2)
        return img


mybutton = Button([100, 100], "Q")

while True:
    success, img = cap.read()
    # Detect hands in the image
    hand, img = hand_detector.findHands(img)

    img = mybutton.draw(img)
    # Display the image
    cv2.imshow("Hand Detection", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
