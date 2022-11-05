import os
import cv2
import random

# Main Variable
CaptureDeviceID = 0
CaptureResolution = (1920, 1080, 15)  # Width, Height, fps
CroppingSize = 720
OutputResolution = 64

# Override Rectangle
AreaStartAt = ((CaptureResolution[0] - CaptureResolution[1]) / 2, 0)
AreaEndAt = (((CaptureResolution[0] - CaptureResolution[1]) / 2) + CaptureResolution[1], CaptureResolution[1])

# Save Point
ImageResizerFolder = "./resized"
ImageCropperFolder = "./cropped"

# Definition
def ImageCropFromFile(path, cropSize: int = CroppingSize) -> bool:
    basename = os.path.splitext(os.path.basename(path))[0]
    original = cv2.imread(path)
    cropAreaStartLimitW, cropAreaStartLimitH = original.shape[0] - cropSize + 1, original.shape[1] - cropSize + 1
    RandomStartAtW, RandomStartAtH = random.randint(0, cropAreaStartLimitW), random.randint(0, cropAreaStartLimitH)
    cropped = original[RandomStartAtH : RandomStartAtH + cropSize, RandomStartAtW : RandomStartAtW + cropSize]
    cv2.imwrite(ImageCropperFolder + "/out_" + basename + ".png", cropped)
    return True, [cropAreaStartLimitW, cropAreaStartLimitH], [RandomStartAtW, RandomStartAtH]


def ImageResizerFromFile(path, Resolution = OutputResolution) -> bool:
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
        cv2.rectangle(capture, (int(AreaStartAt[0]), int(AreaStartAt[1])), (int(AreaEndAt[0]), int(AreaEndAt[1])), (0, 255, 0), thickness=4, lineType=cv2.LINE_8, shift=0)
        cv2.imshow("[Jyanken-Shot] Capture | When You Press ESC Key, Abort Program.", capture)
        k = cv2.waitKey(1)
        if k == 27:  # [ESC] Key
            print("[Key]: Key ID = " + str(k))
            break

    cap.release()
    cv2.destroyAllWindows()
