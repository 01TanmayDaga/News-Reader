import requests
import shutil
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QWidget

class News(QWidget):

    def __init__(self):
        
        super().__init__()
    
    def urlToImage(self, url, name):
        '''Convert url into image and store it in temp folder'''

        response = requests.get(url = url, stream = True)
        with open(f"temp/{name}.png", 'wb') as out_file:
            out_file.write(response.raw, out_file)
        del response

    