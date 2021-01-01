from PyQt5.QtGui import QPixmap
import requests
from PyQt5.QtWidgets import QLabel, QWidget

class News(QWidget):

    count = 0

    def __init__(self, parent,author, title, description, url , urltoimage, publishtime):
        super().__init__()
        self.title = f"<a href = {url}> {title} </a>"
        self.description = description
        self.author = author
        self.publishtime = publishtime
        self.image = self.urlToImage(urltoimage)        
        self.parentwin = parent
        self.setUpUi()

    def urlToImage(self, url):
        '''Convert url into image and store it in temp folder'''

        response = requests.get(url = url, stream = True)
        with open(f"temp/{News.count}.png", 'wb') as out_file:
            out_file.write(response.raw, out_file)
        del response
        return f"temp/{News.count}"

    def setUpUi(self):

        self.width = self.parentwin.verticalLayoutWidget.width
        self.height = int(self.parentwin.verticalLayoutWidget.height/4)
        self.setGeometry(aw = self.width, ah= self.height)
        
        self.lb_img = QLabel(self)
        self.lb_img.setPixmap(QPixmap(self.image))
        self.lb_img.setGeometry(0,0,int(self.width/5),self.height)  # width = contentbox/5

        self.lb_title = QLabel(self)
        self.setGeometry(ax = int(self.width/5)+10, ay = 10)
        self.lb_title.setText(self.title)

        self.lb_description = QLabel(self.description,self)

    