import os
import cv2
from PIL import Image

# Variable
CaptureDeviceID = 0
CaptureResolution = [1920,1080,15]  # Width, Height, fps
OutputResolution = 64

# Save Point
ImageResizerFolder = './resized'

# Definition
def ImageCrop():
    # Write code
    print('DataCrop')

def ImageResizer(Resolution, path):
    basename = os.path.splitext(os.path.basename(path))[0]
    original = Image.open(path)
    resized = original.resize((Resolution, Resolution))
    resized.save(ImageResizerFolder + '/out_' + str(basename) + '.png', quality=90)

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