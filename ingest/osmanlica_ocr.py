import pytesseract
from PIL import Image

def ocr_ottoman(image_path):

    img = Image.open(image_path)

    text = pytesseract.image_to_string(img, lang="tur")

    return text
