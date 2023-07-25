
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 200, 30)
        self.label.setText('Hello, World!')
        
        self.button = QPushButton(self)
        self.button.setGeometry(100, 100, 80, 30)
        self.button.setText('Click me')
        self.button.clicked.connect(self.on_button_click)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple PyQt5 App')
        self.show()
        
    def on_button_click(self):
        self.label.setText('Button clicked!')
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
