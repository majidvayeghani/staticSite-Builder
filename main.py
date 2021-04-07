from containerBuilder import merg
from costumeBuilder import addImg
from indexBuilder import build
from gitPy import autoPush
import sys  
import re
import requests
import os
import shutil

x = int(input(" 1 for add new, 2 for edit, 3 for delete: "))

if(x == 1):
  #ToDo: copy img from other locations to project location.
  x = "y"
  fileList = []
  commit = ""
  while ( x == 'Y' or x == 'y'):
    number = input ("input the image's number: ")
    source = input( "input the image's addrees: ") 
    
    #regex for valid image address
    regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"
    reg = re.compile(regex)
   
    if(re.search(reg,source)):
      downloaded_obj = requests.get(source)
      f_format = os.path.splitext(source)[-1]
      f_name = 'img_{}{}'.format(number,f_format)
      fileName = 'img_{}'.format(number) #for costume's html file
      destination = "/home/majid/Desktop/project/images/" + f_name
      with open(destination, "wb") as file:
        file.write(downloaded_obj.content)
    
    else:
      f_format = os.path.splitext(source)[-1]
      f_name = 'img_{}{}'.format(number,f_format)
      destination = "/home/majid/Desktop/project/images/" + f_name
      fileName = 'img_{}'.format(number) #for costume's html file

      try:
        shutil.copyfile(source, destination)
        print("File copied successfully.")

      # If source and destination are same
      except shutil.SameFileError:
        print("Source and destination represents the same file.")
        
      # If destination is a directory.
      except IsADirectoryError:
        print("Destination is a directory.")
        
      # If there is any permission issue
      except PermissionError:
        print("Permission denied.")
        
      # For other errors
      except:
        print("Error occurred while copying file.")

    # for manage enter character in user input.
    total_input = []
    print( "input the image's caption': " )
    while True:
      txt = input()
      if txt:
        total_input.append(txt)
      else:
        break

    total_input = '<br>'.join(total_input) #<br> tag uses in html file.

    addImg(fileName,destination,total_input)

    fileList.append(destination)

    
    x = input( "Do you want to add new image? Y for continue, any Button for end. ")
    # End of adding img
  
  # for auto on github  
  for i in fileList:
    massege = "img_{}{} ".format(number,f_format)
    commit = commit + massege
    
  autoPush(fileList,commit)

  merg()
 
  build()