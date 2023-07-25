import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import uic

class Example(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('new_app.ui',self )
        self.pushbutton.clicked.connect(self.on_button_click)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple PyQt5 App')
        self.show()
        
    def on_button_click(self):
        self.label.setText('Button clicked!')
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

        