import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import uic

class Example(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('Calculators.ui',self)

        self.dial1.valueChanged.connect(self.on_perform_op)
        self.dial2.valueChanged.connect(self.on_perform_op)


    def on_perform_op(self):
            x=self.dial.value()
            y=self.dial.value()
            self.line1.setText(str(x))
            self.line2.setText(str(y))
            if self.op.currentText()=='Add':
                self.lcd.display(x+y)

            if self.op.currentText()=='Differnce':
                self.lcd.display(abs(x-y))

            if self.op.currentText()=='Multiply':
                self.lcd.display(x*y)

            if self.op.currentText()=='Divide':
                self.lcd.display(x/y) 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

        