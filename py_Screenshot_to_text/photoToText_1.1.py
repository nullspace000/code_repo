from PIL import Image
import pytesseract
#on archlinux python-pytesseract
# 30) english

# Path to the image file
image_path = '/home/null/Pictures/Screenshots/1.png'

# Open the image
img = Image.open(image_path)

# Use pytesseract to extract text
text = pytesseract.image_to_string(img, lang='eng')

# Indicator
print('###########################')
print('#                         #')
print('###########################')

# Print the extracted text
print(text)
