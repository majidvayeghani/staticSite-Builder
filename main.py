from containerBuilder import merg
from imgBuilder import addImg
from indexBuilder import build


x = int(input(" 1 for add new, 2 foe edi, 3 for delet: "))

if(x == 1):
  #ToDo: number must be uniqe.
  #ToDo: copy img from other locations to project location
  x = "y"
  while ( x == 'Y' or x == 'y'):
    name = input( "input the image number: ") 
    txt = input("Input the image's caption: ")

    addImg(name,txt)

    x = input( "Do you want to add new image? Y for continue, any Button for end. ")

  merg()
 
  build()
  