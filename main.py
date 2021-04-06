from containerBuilder import merg
from costumeBuilder import addImg
from indexBuilder import build
import sys  
import re
import requests
import os

x = int(input(" 1 for add new, 2 for edit, 3 for delete: "))


if(x == 1):
  #ToDo: copy img from other locations to project location.
  x = "y"
  while ( x == 'Y' or x == 'y'):
    number = input ("input the image's number: ")
    name = input( "input the image's addrees: ") 
    
    #regex for valid image address
    regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp))$)"
    reg = re.compile(regex)
   
    if(re.search(reg,name)):
      downloaded_obj = requests.get(name)
      f_format = os.path.splitext(name)[-1]
      f_name = 'img_{}{}'.format(number,f_format)
      fileName = 'img_{}'.format(number) #for costume's html file
      imgName = "/home/majid/Desktop/project/images/" + f_name
      print(imgName)
      with open(imgName, "wb") as file:
        file.write(downloaded_obj.content)
    else:
      break
    
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

    addImg(fileName,imgName,total_input)

    x = input( "Do you want to add new image? Y for continue, any Button for end. ")

  merg()
 
  build()
  