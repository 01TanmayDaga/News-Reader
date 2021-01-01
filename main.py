import sys
from PyQt5.QtGui import QPixmap
import requests
import json
from PyQt5 import QtWidgets
from newsapi import NewsApiClient
from GUI import Ui_MainWindow
API_KEY = '9659803702a54e11b4478b56acb581f7'


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ex = Ui_MainWindow(win)
    win.show()
    ex.setupUi(win)
    sys.exit(app.exec_())
main()