# pip install pytesseract

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
text1 = pytesseract.image_to_string(r'image_1.png')
print(text1)