from io import StringIO
from jinja2 import Environment, FileSystemLoader

def build():
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    item = template.render()

    # save rendered block code 
    fileName = "./index.html"
    with open(fileName, "w") as newItem:
        newItem.write(item)