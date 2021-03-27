from io import StringIO
from jinja2 import Environment, FileSystemLoader
import os
### render new item.html
def addImg(imgName,txt):

    src = "./images/img_" +imgName +".jpg"  #image address
    caption = txt 

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('costumeTemp.html')
    item = template.render(img=src,caption=caption)

    #Checking Directory(costumes) Exists
    path = os.getcwd()
    path = path + '/templates/costumes/'
    if( os.path.exists(path) ):
        pass
    else:
        os.mkdir(path)
        
    #save new item
    fileName = path + imgName + ".html"
    with open(fileName, "w") as newItem:
        newItem.write(item)