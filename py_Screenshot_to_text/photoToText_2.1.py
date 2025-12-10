from PIL import Image
import pytesseract
import time
import pyscreenshot as ImageGrab

#wait for 1 seconds for me to switch to the target window
time.sleep(1)

# (left, top, width, height)
x, y, w, h = 0, 0, 1920, 820
img = ImageGrab.grab(bbox=(x, y, x + w, y + h))  # bbox = (x1, y1, x2, y2)
img.save("question.png")

#img = Image.open("question.png")
text = pytesseract.image_to_string(img, lang='eng')

print('###########################')
print('#           New           #')
print('###########################')
print(text)

#adjuntar text to .txt file:
# python photoToText_2.1.py >> output.txt
