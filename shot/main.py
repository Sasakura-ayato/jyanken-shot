import os
import cv2

# Main Variable
CaptureDeviceID = 0
CaptureResolution = (1920, 1080, 15)  # Width, Height, fps
OutputResolution = 64

# Override Rectangle
RectangleStartAt = ()
RectangleEndAt = ()
RectangleColor = (0, 255, 0)  # Color(B, G, R)
RectangleLine = -1

# Save Point
ImageResizerFolder = "./resized"

# Definition
def ImageCrop():
    # Write code
    print("DataCrop")


def ImageResizer(path, Resolution = OutputResolution) -> bool:
    basename = os.path.splitext(os.path.basename(path))[0]
    original = cv2.imread(path)
    resized = cv2.resize(original, dsize=(Resolution, Resolution))
    cv2.imwrite(ImageResizerFolder + "/out_" + str(basename) + ".png", resized)
    return True


if __name__ == "__main__":
    # Launch Camera
    cap = cv2.VideoCapture(CaptureDeviceID)
    cap.set(3, CaptureResolution[0])
    cap.set(4, CaptureResolution[1])
    cap.set(5, CaptureResolution[2])

    while True:
        resultBool, capture = cap.read()
        cv2.rectangle(capture, RectangleStartAt, RectangleEndAt, RectangleLine)
        cv2.imshow("Capture Display", capture)
        k = cv2.waitKey(1)
        if k == 27:  # [ESC] Key
            break

    cap.release()
    cv2.destroyAllWindows()
