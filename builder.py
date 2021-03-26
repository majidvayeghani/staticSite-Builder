
# render template.html
from os import listdir
from os.path import isfile, join
from io import StringIO
from jinja2 import Environment, FileSystemLoader

def test1():
    
    mypath = "/home/majid/Desktop/website/templates/Items"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    itemNames = []
    for i in onlyfiles:
        i = i.split(".")
        itemNames.append(i[0])


    # array = [] # list of images (item1.html,item2.html,...). just its number
    # for  i in range(1, num+1):
    #     array.append(str(i)) # because jinja template just acceptes string value

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')
    item = template.render(a=itemNames)

    # save rendered block code 
    fileName = "./templates/block/block.html"
    with open(fileName, "w") as newItem:
        newItem.write(item)

    print("yes")