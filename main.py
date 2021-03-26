
from builder import test1
from itemBuilder import test
from build import test2


x = int(input(" 1 for add new, 2 foe edi, 3 for delet: "))

if(x == 1):
  #ToDo: number must be uniqe.
  #ToDo: 
  x = "y"
  while ( x == 'Y' or x == 'y'):
    number = input( "input the image number: ")#image & text number. 

    test(number)

    x = input( "Do you want to add new image? Y for continue, any Button for end. ")

  test1()
  print("ok")
  test2()
  print("hah")