import gui_modules
from PyQt5.QtWidgets import QApplication,QLineEdit
import sys


app=QApplication(sys.argv)
while True:
    window=gui_modules.GUI()

    window.name_edit()
    window.exec_()
