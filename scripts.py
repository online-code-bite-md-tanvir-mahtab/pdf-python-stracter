path = 'E:/software downloads/tesseract-ocr/tesseract.exe'
from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = f'{path}'

#Define path to image
path_to_image = 'Demo.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)




























# # creating a pdf file object 
# pdfFileObj = open('dha.pdf', 'rb') 
    
# # creating a pdf reader object 
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# # printing number of pages in pdf file 
# print(pdfReader.numPages) 
    
# # creating a page object 
# pageObj = pdfReader.getPage(0) 
    
# # extracting text from page 
# print(pageObj.extractText()) 
    
# # closing the pdf file object 
# pdfFileObj.close() 