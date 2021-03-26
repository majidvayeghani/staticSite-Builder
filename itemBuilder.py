from io import StringIO
from jinja2 import Environment, FileSystemLoader

### render new item.html
#ToDo: get image number form user
def test(number):

        # number = input( "input the image number: ")#image & text number. 
        src = "./images/img_" +number +".jpg"  #image address
        # txt = "./website-master/images/caption" +number +".txt"  #caption address
        txt = "caption" 


        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('item.html')
        item = template.render(img=src,caption=txt)

        print(item)

        # save new item
        fileName = "./templates/Items/" + number + ".html"
        with open(fileName, "w") as newItem:
            newItem.write(item)
        
        # x = input( "Do you want to add new image? Y for continue, any Button for end. ")


