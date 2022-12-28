import cv2
import time

# Main Variable
CaptureDeviceID = 0
CaptureResolution = (640, 480, 15)  # Width, Height, fps
ShotTiming = 2.8
acceptShotTimingRange = 0.2

# Save Directory
ImageOriginalFolder = "./original/"

# Override Rectangle
AreaStartAt = ((CaptureResolution[0] - CaptureResolution[1]) / 2, 0)
AreaEndAt = (
    ((CaptureResolution[0] - CaptureResolution[1]) / 2) + CaptureResolution[1],
    CaptureResolution[1],
)

def LaunchCaptureDevice(
    CaptureDeviceID: int = CaptureDeviceID,
    CaptureResolution: tuple = CaptureResolution,
    shotTiming: float = ShotTiming,
    acceptShotTimingRange: float = acceptShotTimingRange,
):
    # Launch Camera
    cap = cv2.VideoCapture(CaptureDeviceID, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("H", "2", "6", "4"))
    cap.set(3, CaptureResolution[0])
    cap.set(4, CaptureResolution[1])
    cap.set(5, CaptureResolution[2])

    # Reset Variable
    timer = 0
    start = time.time()

    while True:
        resultBool, capture = cap.read()
        end = time.time()
        timer = round(end - start, 1)
        phase = round(timer % 4, 1)

        # Shot Image
        if shotTiming < phase < shotTiming + acceptShotTimingRange:
            cv2.imwrite(ImageOriginalFolder + "shot_" + str(timer) + ".png", capture)

        cv2.rectangle(
            capture,
            (int(AreaStartAt[0]), int(AreaStartAt[1])),
            (int(AreaEndAt[0]), int(AreaEndAt[1])),
            (0, 255, 0),
            thickness=4,
            lineType=cv2.LINE_8,
            shift=0,
        )
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
            cv2.rectangle(
                capture,
                (0, 0),
                (int(CaptureResolution[0]), int(CaptureResolution[1])),
                (0, 0, 255),
                thickness=10,
                lineType=cv2.LINE_8,
                shift=0,
            )
        elif (
            (0.0 < phase < 0.1)
            or (0.9 < phase < 1.1)
            or (1.9 < phase < 2.1)
            or (3.9 < phase < 4.0)
        ):
            cv2.rectangle(
                capture,
                (0, 0),
                (int(CaptureResolution[0]), int(CaptureResolution[1])),
                (3, 212, 241),
                thickness=10,
                lineType=cv2.LINE_8,
                shift=0,
            )

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
