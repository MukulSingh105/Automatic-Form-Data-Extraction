import cv2
import numpy as np
import pytesseract

# read image
img = cv2.imread('result.png')
ori = cv2.imread('0001.jpg')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)[1]

# get contours
result = img.copy()
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
fields = []
for cntr in contours:
    x,y,w,h = cv2.boundingRect(cntr)
    if w*h > 100:
        fields.append((x,y,w,h))
        cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("x,y,w,h:",x,y,w,h)

# save resulting image
cv2.imwrite('blobs_result.jpg',result)

# show thresh and result
cv2.imwrite("bounding_box.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file1 = open("demofile.txt", "w")

for c in fields:
    (x,y,w,h) = c
    text1 = pytesseract.image_to_string(ori[y-10:y+h+10,x-10:])
    if text1 == "":
        text1 = pytesseract.image_to_string(ori[y-10:y+h+10,x-10:], config="--psm 10")
    text2 = pytesseract.image_to_string(ori[y-3*h:y,x:])
    print(text1, text2)
    s = text2 + " : " + text1 + '\n'
    file1.write(s)
file1.close()
