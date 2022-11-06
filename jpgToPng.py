from PIL import Image
import glob
def converter():
    path = r'/Users/macbook/desktop/lab2'
    for file in glob.glob(path + "**/*.jpg"):
        image = Image.open(file)
        print(image)
        image.save(path + "/*.png")
        print(file)