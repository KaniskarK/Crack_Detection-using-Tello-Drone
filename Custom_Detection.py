import pygame
import cv2
path = 'cascade.xml'  # PATH OF THE CASCADE
cameraNo = 0          # CAMERA NUMBER
objectName = 'Crack'  # OBJECT NAME TO DISPLAY
frameWidth= 640       # DISPLAY WIDTH
frameHeight = 480     # DISPLAY HEIGHT
color= (255,0,255)
def init():
        pygame.init()
        win=pygame.display.set_mode((400,400))

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",0,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)
cascade = cv2.CascadeClassifier(path)


def getKey(keyName):
        ans = False
        for eve in pygame.event.get():pass
        keyInput=pygame.key.get_pressed()
        myKey = getattr(pygame, 'K_{}'.format(keyName))
        if keyInput[myKey]:
                ans=True
        pygame.display.update()
        return ans

def findFace(img):
    # faceCascade = cv2.CascadeClassifier("cascade.xml")
    # path = 'haarcascades/cascade.xml'  # PATH OF THE CASCADE

    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Result") / 1000)
    neig = cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray, scaleVal, neig)
    # DISPLAY THE DETECTED OBJECTS
    for (x, y, w, h) in objects:
        area = w * h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            cv2.putText(img, objectName, (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            roi_color = img[y:y + h, x:x + w]

    cv2.imshow("Result", img)


    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    # for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img

def main():
        if getKey("LEFT"):
                print("Left Key Pressed")
        if getKey("RIGHT"):
                print("Right Key Pressed")


if __name__ == '__main__':
        init()
        while True:
                main()
