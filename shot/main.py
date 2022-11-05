import cv2

# Variable
CaptureDeviceID = 0
CaptureResolution = [720,480,15]  # Width, Height, fps

# Definition
def DataCrop():
    # Write code
    print(DataCrop)

if __name__ == "__main__":
    # Launch Camera
    cap = cv2.VideoCapture(CaptureDeviceID)
    cap.set(3, CaptureResolution[0])
    cap.set(4, CaptureResolution[1])
    cap.set(5, CaptureResolution[2])

    while True:
        resultBool, capture = cap.read()
        cv2.imshow("Capture Display", capture)
        k = cv2.waitKey(1)
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()