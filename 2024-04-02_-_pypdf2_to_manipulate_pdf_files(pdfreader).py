#[terminal]$: pip install PyPDF2 #1:
from pathlib import Path #2:
from PyPDF2 import PdfReader #3:

#Defining directories
ROOT_FOLDER = Path(__file__).parent #4:
ORIGINALS_FOLDER = ROOT_FOLDER / 'pypdf2/original_pdf' #4:
NEW_FOLDER = ROOT_FOLDER / 'pypdf2/new_files' #4:
BACEN_REPORT = ORIGINALS_FOLDER / 'R20240322.pdf' #5:
NEW_FOLDER.mkdir(exist_ok=True) #6:

#Reading, extracting and printing
reader = PdfReader(BACEN_REPORT) #7:
print(len(reader.pages)) #7: #8:

page_one = reader.pages[0] #9:
print(page_one.extract_text()) #9: #10:
print('***' * 10)

#[terminal]$: pip install PyPDF2[image] #11:
print(page_one.images) #12: #13:
print(page_one.images[0]) #12: #14:

#Save image to another folder
image_zero = page_one.images[0]
with open(NEW_FOLDER / image_zero.name, 'wb') as temp_image: #15:
    temp_image.write(image_zero.data) #15:

#APRESENTAÇÃO
'''
How about exploring #PDF files with #PyPDF2? In this example, this script is capable of:

1. Reading PDF files and extracting information, such as the number of pages;
2. Extracting text from PDF pages;
3. Extracting and manipulating images present in the PDF pages.

This is a simple example of how to automate tasks related to PDF files using #Python.
The flexibility and ease of use of PyPDF2 make this task very simple. Want to know more
about this script? Check out my #Substack and #Github.
---
[#ptBR]
O que acha de explorar arquivos #PDF com #PyPDF2? Neste exemplo, este script é capaz de:
1. Ler arquivos PDF e extrair informações, como o número de páginas;
2. Extrair texto de páginas PDF;
3. Extrair e manipular imagens presentes nas páginas PDF.

Este é um exemplo simples de como automatizar tarefas relacionadas a arquivos PDF usando #Python.
A flexibilidade e facilidade de uso do PyPDF2 tornam essa tarefa muito simples. Quer saber mais
sobre este script? Acesse meu #Substack e #Github.
---
#substack:
#github:
'''

#COMMENTS:
#1: Installation of the PyPDF2 library using pip. Enable your virtual environment (source bin/activate).
#2: This is a class to represent file or directory paths independently of the operating system.
#3: This is already a class from the PyPDF2 library used to read PDF files.
#4: Here, the directories for the original files and the new files are defined.
#5: Sets the path for the input PDF file.
#6: Creates the output directory if it doesn't already exist.
#7: Reads the PDF file and prints the number of pages.
#8: Response: 2.
#9: Extracts text from the first page and prints it.
#10: Response: see image A003.png.
#11: Installing "image".
#12: Displays information about the images present on the first page and prints details about the first image.
#13: Response: see image A004.png.
#14: Response: File(name=X5.png, data: 1.3 kB).
#15: Saves the first image in a new directory.
#Doc: https://pypdf2.readthedocs.io/en/3.0.0/

# Edson Copque | https://linktr.ee/edsoncopque
