import glob
import main

files = glob.glob("./original/*.png")

# Files
for file in files:
    print(file)

# Cut
for file in files:
    for i in range(10):
        print(main.ImageCropFromFile(file))
