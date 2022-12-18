import glob
import main
import shutil
import os

originals = glob.glob("./original/*.png")

for original in originals:
    print(original)

# Cut
n = 0
for original in originals:
    for i in range(10):
        n = n + 1
        print(
            main.ImageCropFromFile(
                original, savePath=main.ImagePreprocessingFolder + "/" + str(n) + ".png"
            )
        )

# Square
for original in originals:
    print(
        main.ImageResizerFromFile(
            original, savePath=main.ImagePreprocessingFolder + "/" + str(n) + ".png"
        )
    )

# Resize
n = 0
resizeDatas = glob.glob("./preprocessing/*.png")
for resizeData in resizeDatas:
    n = n + 1
    print(
        main.ImageResizerFromFile(
            resizeData, savePath=main.ImageResizeFolder + "/" + str(n) + ".png"
        )
    )

# Delete
for f in resizeDatas:
    os.remove(f)