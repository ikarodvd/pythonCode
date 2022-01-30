import pytesseract as ocr
from PIL import Image


def menu_ ():
   # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    op = int (input ("Informe a opção que voce deseja utilizar\n1- Ler texto de uma imagem\n2- Encontrar palavras em uma imagem\n"))
    if op == 1:
        phrase = ocr.image_to_string (Image.open('phrase.jpg'))
        print (phrase)
        arq = []
        for i in phrase:
            arq.append(i)
    print (arq)

    for i in arq:
        if i == 'O':
            print ('achou')
menu_()
