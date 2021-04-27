
from pytube import YouTube 
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 500
        self.top = 500
        self.width = 400
        self.height = 180
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
       
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.setPlaceholderText("Enter Youtube Link:")
        
        self.Nametextbox = QLineEdit(self)
        self.Nametextbox.move(20, 80)
        self.Nametextbox.resize(280,40)
        self.Nametextbox.setPlaceholderText("Enter path to download:")
       
        
        self.button = QPushButton('Download mp4', self)
        self.button.move(20,140)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):

        textboxValue = self.textbox.text()
        
        video_link =  textboxValue
        path = self.Nametextbox.text()
        try :
            video = YouTube(video_link) 
        except:
            msg = QMessageBox()
            msg.setText("\nError wrong link.Try again.\n")
            x = msg.exec_()
        if (video == None ):
            msg = QMessageBox()
            msg.setText("\nError.\n")
            x = msg.exec_()
       
        video.streams.filter(file_extension='mp4')
        stream = video.streams.get_by_itag(18)
        download_path = stream.download(path)

        if download_path ==   str(path ) + "\\" + str(video.title) +'.mp4':
            msg = QMessageBox()
            msg.setText("\nThe video was downloaded at your preferred destination.\n")
            x = msg.exec_()
            
        else :
            msg = QMessageBox()
            msg.setText("\nError please try again.\n")
            x = msg.exec_()
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




 
