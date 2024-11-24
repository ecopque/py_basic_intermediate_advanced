#[terminal]$: pip install PyPDF2 #1:
from pathlib import Path #2:
from PyPDF2 import PdfReader, PdfWriter, PdfMerger #3: #16: #26:

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

#Generating new single page pdf
writer = PdfWriter()
writer.add_page(page_one) #17:

with open(NEW_FOLDER / 'page_zero.pdf', 'wb') as temp_image2: #18:
    writer.write(temp_image2) #19: #20:

#Generating new pdf for each page
for i, page in enumerate(reader.pages): #21:
    writer2 = PdfWriter()
    with open(NEW_FOLDER / f'pdf_page{i}.pdf', 'wb') as temp_image3: #22:
        writer2.add_page(page) #23:
        writer2.write(temp_image3) #25:

#Merging pdf files
files = [
    NEW_FOLDER / 'pdf_page1.pdf',
    NEW_FOLDER / 'pdf_page0.pdf',
] #27:
merger = PdfMerger() #28:
for file in files: #29:
    merger.append(file) #30:

merger.write(NEW_FOLDER / 'zmerged.pdf') #31:
merger.close() #32:



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
#16: Let's write PDF files.
#17: Adds the first page to the PdfWriter object.
#18: Opens a new file in the specified directory to write the first page extracted from the PDF.
#19: Writes the extracted page to the opened PDF file.
#20: View image E001.
#21: Iterates over each page in the original PDF.
#22: Opens a new file in the specified directory to write the current page of the PDF.
#23: Adds the current page to the PdfWriter object.
#24: Writes the current page to the opened PDF file.
#25: View image E002. Here, it will display the generated files.
#26: PDF files merging.
#27: We create a list of paths to the individual PDF files we want to merge.
#28: We initialize a PdfMerger object, which will allow us to merge the PDF files.
#29: Initiates a loop that iterates over each file in the list of files to be merged.
#30: Adds each PDF file to the PdfMerger object. By the end of this loop, all PDF files in the list will be merged into a single file.
#31: Writes the merged PDF file to the NEW_FOLDER directory with the name zmerged.pdf.
#32: Closes the PdfMerger object after the merging operation is completed.
#Doc: https://pypdf2.readthedocs.io/en/3.0.0/

# Edson Copque | https://linktr.ee/edsoncopque
