import cv2

def capture(num):
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite(f'blocks_{str(num)}.jpg', frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

capture(1)