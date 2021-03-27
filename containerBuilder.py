
# render template.html
from os import listdir
from os.path import isfile, join
import os
from io import StringIO
from jinja2 import Environment, FileSystemLoader

def merg():
    
    #ToDo: آدرس پایینی رو باید از وابستگی به سیستم خودم در بیارم
    path = os.getcwd()
    path = path + '/templates/costumes/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('containerTemp.html')
    item = template.render(a=onlyfiles)

    # save rendered block code 
    fileName = "./templates/container.html"
    with open(fileName, "w") as newItem:
        newItem.write(item)