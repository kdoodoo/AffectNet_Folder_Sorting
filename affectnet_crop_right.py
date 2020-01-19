from PIL import Image 
import glob
import os

# folders from 1 - 1381 you may change ranges accordingly eg. 1-100, 101-200
for folders in range(1,1381):
	# open each files based on the file type: jpeg, jpg, bmp, png 
    for filename in glob.glob('img/AffectNet/raw/cropped_Annotated/'+str(folders)+'/*.jpg'): 

        
        im = Image.open(filename)

        width, height = im.size   # Get dimensions
        # crop right side : leave only the right side of the facial image
        left = width/2
        top = 0
        right = width
        bottom = height
		# cropping  
        im1 = im.crop((left, top, right, bottom)) 
#     save the file
        im1.save(filename)
