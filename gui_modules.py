from PyQt5 import uic
from PyQt5.QtWidgets import QDialog,QPushButton,QLineEdit

class GUI(QDialog):

    def __init__(self):
        super(GUI,self).__init__()

    def reg_ok(self):
        super(GUI,self).__init__()
        uic.loadUi('init_data/Reg_comp.ui',self)
        self.ok_btn=self.findChild(QPushButton,'ok_butn')

        self.ok_btn.clicked.connect(self.close)
        self.show()
    
    def reg_failed(self):
        super(GUI,self).__init__()
        uic.loadUi('init_data/Reg_failed.ui',self)
        self.ok_btn=self.findChild(QPushButton,'ok_butn')

        self.ok_btn.clicked.connect(self.close)
        self.show()


    def entr_ok(self):
        super(GUI,self).__init__()
        uic.loadUi('init_data/entry_marked.ui',self)
        self.ok_btn=self.findChild(QPushButton,'ok_butn')

        self.ok_btn.clicked.connect(self.close)
        self.show()

        
    def name_edit(self):
        name=""

        
        uic.loadUi('init_data/name_entry.ui',self)
        
        def get_name():
            global name
            name=per_name.text()
            self.close()

        per_name=self.findChild(QLineEdit,"name_edit")
        ok_btn=self.findChild(QPushButton,'ok_butn')

        ok_btn.clicked.connect(get_name)
        self.show()


    def return_name(self):
        global name
        return name    

    