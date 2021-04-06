from containerBuilder import merg
from costumeBuilder import addImg
from indexBuilder import build
import sys  


x = int(input(" 1 for add new, 2 for edit, 3 for delete: "))

if(x == 1):
  #ToDo: copy img from other locations to project location.
  x = "y"
  while ( x == 'Y' or x == 'y'):
    name = input( "input the image's addrees: ") 

    total_input = []
    print( "input the image's caption': " )
    # for manage enter character in user input.
    while True:
      txt = input()
      if txt:
        total_input.append(txt)
      else:
        break

    total_input = '<br>'.join(total_input) #<br> tag uses in html file.

    addImg(name,total_input)

    x = input( "Do you want to add new image? Y for continue, any Button for end. ")

  merg()
 
  build()
  