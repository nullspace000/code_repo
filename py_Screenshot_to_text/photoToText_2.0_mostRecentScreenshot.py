#extracts text from most recent screenshot
#prints extracted text

from PIL import Image
import pytesseract
import glob
import os

# Folder containing screenshots
folder = "/home/null/Pictures/Screenshots"

# Get all PNG files in the folder
files = glob.glob(os.path.join(folder, "*.png"))

if not files:
    raise FileNotFoundError("No PNG files found in the screenshots folder.")

# Get the newest file by modification time
image_path = max(files, key=os.path.getmtime)

print("Using image:", image_path)

img = Image.open(image_path)
text = pytesseract.image_to_string(img, lang='eng')

print('###########################')
print('#                         #')
print('###########################')
print(text)
