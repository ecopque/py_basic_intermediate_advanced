#[terminal]$ pip install pillow #1:
from PIL import Image #13:
from pathlib import Path #2:

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'image00.jpg'
NEW_IMAGE = ROOT_FOLDER / 'image01_new.jpg'

pil_image = Image.open(ORIGINAL) #3:
print(pil_image.size) #4:

width_image, height_image = pil_image.size #5:
exif_image = pil_image.info['exif'] #6:

# try: #10:
#     exif_image = pil_image.info['exif']
# except KeyError:
#     exif_image = None

new_width_image = 640
new_height_image = round((height_image * new_width_image) / width_image) #7:
print(new_width_image, new_height_image) #8:
print(new_width_image, round(new_height_image)) #9:

new_image = pil_image.resize(size=(new_width_image, new_height_image)) #11:
new_image.save(NEW_IMAGE, optimize=True, quality=70, exif=exif_image) #12:

#Explanation: The script opens an image, prints its dimensions, resizes the image to a specific size, rounding the proportional dimensions to integers, and saves the resized image to a new file, keeping the original image's EXIF information if available.

#1: Installing the pillow package. Remember to activate the virtual environment.
#2: Imports the Path class from the pathlib module, which is used for file path manipulation.
#3: Opens the original image using the open method of the Image class and assigns the resulting image object to the pil_image variable.
#4: Response: (4898, 3265).
#5: Gets the width and height of the original image and assigns them to the width_image and height_image variables, respectively.
#6: Gets the EXIF information from the original image and assigns it to the exif_image variable. This line may raise an error if there is no EXIF information in the image.
#7: Calculates the height of the new image proportionally to the desired width, maintaining the original image's aspect ratio. The result is rounded to the nearest integer.
#8: If round is not used on "new_height_image", we will have the following response: 640 426.62311147407104.
#9: Response: 640 427.
#10: Tries to obtain the EXIF information from the image, and if it does not exist, sets exif_image to None.
#11: Resizes the original image to the specified new dimensions.
#12: Saves the new image to the file specified by NEW_IMAGE, optimizing it to save disk space, setting the quality to 70, and including the original image's EXIF information.
#13: Imports the Image class from the PIL module, which is used to work with images.