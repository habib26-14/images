import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = 'images1.png'
image = Image.open(image_path)
texte = pytesseract.image_to_string(image)
print(texte)