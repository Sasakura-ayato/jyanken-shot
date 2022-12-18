import os
import cv2
import random
import time

# Main Variable
CaptureDeviceID = 0
CaptureResolution = (1920, 1080, 15)  # Width, Height, fps
CroppingSize = 720
OutputResolution = 64

ShotTiming = 2.5
acceptShotTimingRange = 0.2

# Override Rectangle
AreaStartAt = ((CaptureResolution[0] - CaptureResolution[1]) / 2, 0)
AreaEndAt = (
    ((CaptureResolution[0] - CaptureResolution[1]) / 2) + CaptureResolution[1],
    CaptureResolution[1],
)

# Save Point
ImageResizerFolder = "./resized"
ImageCropperFolder = "./cropped"
ImageShotFolder = "./original"

# Definition
def ImageCropFromFile(
    path: str, cropSize: int = CroppingSize, Resolution: int = OutputResolution) -> bool:
    basename = os.path.splitext(os.path.basename(path))[0]
    original = cv2.imread(path)
    cropAreaStartLimitW, cropAreaStartLimitH = (
        original.shape[0] - cropSize + 1,
        original.shape[1] - cropSize + 1,
    )
    RandomStartAtW, RandomStartAtH = random.randint(
        0, cropAreaStartLimitW
    ), random.randint(0, cropAreaStartLimitH)
    cropped = original[
        RandomStartAtH : RandomStartAtH + cropSize,
        RandomStartAtW : RandomStartAtW + cropSize,
    ]
    resized = cv2.resize(cropped, dsize=(Resolution, Resolution))
    cv2.imwrite(ImageCropperFolder + "/out_" + basename + ".png", resized)
    return (
        True,
        [cropAreaStartLimitW, cropAreaStartLimitH],
        [RandomStartAtW, RandomStartAtH],
        [RandomStartAtW + cropSize, RandomStartAtH + cropSize],
        Resolution,
    )


def ImageResizerFromFile(path: str, Resolution: int = OutputResolution) -> bool:
    basename = os.path.splitext(os.path.basename(path))[0]
    original = cv2.imread(path)
    resized = cv2.resize(original, dsize=(Resolution, Resolution))
    cv2.imwrite(ImageResizerFolder + "/out_" + str(basename) + ".png", resized)
    return True, Resolution


def LaunchCaptureDevice(
    CaptureDeviceID: int = CaptureDeviceID, CaptureResolution: tuple = CaptureResolution, shotTiming: float = ShotTiming, acceptShotTimingRange: float = acceptShotTimingRange
):
    # Launch Camera
    cap = cv2.VideoCapture(CaptureDeviceID)
    cap.set(3, CaptureResolution[0])
    cap.set(4, CaptureResolution[1])
    cap.set(5, CaptureResolution[2])

    # Reset Variable
    timer = 0
    start = time.time()

    while True:

        resultBool, capture = cap.read()
        cv2.rectangle(
            capture,
            (int(AreaStartAt[0]), int(AreaStartAt[1])),
            (int(AreaEndAt[0]), int(AreaEndAt[1])),
            (0, 255, 0),
            thickness=4,
            lineType=cv2.LINE_8,
            shift=0,
        )
        end = time.time()
        timer = round(end - start, 1)
        phase = round(timer % 4, 1)
        cv2.putText(
            capture,
            text="Time: " + str(timer),
            org=(100, 100),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),
        )

        # IndicateTiming
        if 2.9 < phase < 3.1:
            cv2.rectangle(capture, (0, 0), (int(CaptureResolution[0]), int(CaptureResolution[1])), (0, 0, 255), thickness=10, lineType=cv2.LINE_8, shift=0)
        elif (0.0 < phase < 0.1) or (0.9 < phase < 1.1) or (1.9 < phase < 2.1) or (3.9 < phase < 4.0):
            cv2.rectangle(capture, (0, 0), (int(CaptureResolution[0]), int(CaptureResolution[1])), (3, 212, 241), thickness=10, lineType=cv2.LINE_8, shift=0)

        # Shot Image
        if shotTiming < phase < shotTiming + acceptShotTimingRange:
            cv2.imwrite('./original/shot_' + str(timer) + '.png', capture)

        cv2.imshow(
            "[Jyanken-Shot] Capture | When You Press ESC Key, Abort Program.", capture
        )
        k = cv2.waitKey(1)
        if k == 27:  # [ESC] Key
            print("[Key]: Key ID = " + str(k))
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    LaunchCaptureDevice()
