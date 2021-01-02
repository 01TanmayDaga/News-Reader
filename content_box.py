import requests
import shutil
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

class content_box(QWidget):

    counter = 0

    def __init__(self, title,url, description, urltoimage):
        super().__init__()

        self.setFixedHeight(121)
        self.setFixedWidth(681)
        self.set_pic(self.get_img(urltoimage))
        self.set_title(title,url)
        self.set_des(description)
    
    def get_img(self,urltoimg):
        '''Convert url into image and store it in temp folder'''

        response = requests.get(url = urltoimg, stream = True)
        with open(f"temp/{content_box.counter}.png", 'wb') as out_file:
            shutil.copyfileobj(response.raw,out_file)
        del response
        content_box.counter += 1
        return f"temp/{content_box.counter}"


    def set_pic(self,imgpath):

        lbl = QLabel(self)
        
        lbl.setGeometry(0,0,681,121)
        
        lbl.setPixmap(QPixmap(imgpath))

    def set_title(self, title, url):

        lbl = QLabel(f"<a href = {url}> {title} </a>", self)

        lbl.setGeometry(140,20,621,21)

    def set_des(self,des):

        lbl = QLabel(des,self)
        
        lbl.setGeometry(140,50,621,51)


