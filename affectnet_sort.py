import shutil
import csv

# change path where to save accordingly from A - M or any
pathto = 'img/AffectNet/CNN/A' 


# function move image files based on emotion 
def expression1(path_in_csv,express):

	# change exprssion from 0 - 10 accordingly
    if express == '1':
        print(path)
        # move file from path into pathto 
        shutil.move("img/AffectNet/raw/cropped_Annotated/"+path_in_csv, pathto)



# where to grab  csv file
path = 'img/AffectNet/training.csv'

# open csv file
with open(path) as csvfile:

   	# read csv file
    csv1 = csv.reader(csvfile)

   	# reading each row with [0]column, [6]column  
    for row in csv1:
        # call back function expression1
        expression1(row[0],row[6])

