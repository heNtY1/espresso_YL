import sys
import sqlite3

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(545, 294)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 361, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.idEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.idEdit.setReadOnly(True)
        self.idEdit.setObjectName("idEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idEdit)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameEdit)
        self.fireEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.fireEdit.setObjectName("fireEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fireEdit)
        self.pomolEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.pomolEdit.setObjectName("pomolEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pomolEdit)
        self.tastiEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.tastiEdit.setObjectName("tastiEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tastiEdit)
        self.priseEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.priseEdit.setObjectName("priseEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.priseEdit)
        self.VVEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.VVEdit.setObjectName("VVEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.VVEdit)
        self.nextButton = QtWidgets.QPushButton(parent=Form)
        self.nextButton.setGeometry(QtCore.QRect(270, 250, 75, 23))
        self.nextButton.setObjectName("nextButton")
        self.addButton = QtWidgets.QPushButton(parent=Form)
        self.addButton.setGeometry(QtCore.QRect(370, 250, 75, 23))
        self.addButton.setObjectName("addButton")
        self.redButton = QtWidgets.QPushButton(parent=Form)
        self.redButton.setGeometry(QtCore.QRect(154, 250, 91, 23))
        self.redButton.setObjectName("redButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ID:"))
        self.label_2.setText(_translate("Form", "Название:"))
        self.label_3.setText(_translate("Form", "Степень обжарки:"))
        self.label_4.setText(_translate("Form", "Помол:"))
        self.label_5.setText(_translate("Form", "Описание вкуса:"))
        self.label_6.setText(_translate("Form", "Цена:"))
        self.label_7.setText(_translate("Form", "Объем упаковки:"))
        self.nextButton.setText(_translate("Form", "Следующий"))
        self.addButton.setText(_translate("Form", "Добавить"))
        self.redButton.setText(_translate("Form", "Редактировать"))


class Ui_Form11(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(545, 294)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 361, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameEdit)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.fireEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.fireEdit.setObjectName("fireEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fireEdit)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.pomolEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.pomolEdit.setObjectName("pomolEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pomolEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.tastiEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.tastiEdit.setObjectName("tastiEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tastiEdit)
        self.label_6 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.priseEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.priseEdit.setObjectName("priseEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.priseEdit)
        self.label_7 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.VVEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.VVEdit.setObjectName("VVEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.VVEdit)
        self.okButton = QtWidgets.QPushButton(parent=Form)
        self.okButton.setGeometry(QtCore.QRect(380, 250, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Название:"))
        self.label_3.setText(_translate("Form", "Степень обжарки:"))
        self.label_4.setText(_translate("Form", "Помол:"))
        self.label_5.setText(_translate("Form", "Описание вкуса:"))
        self.label_6.setText(_translate("Form", "Цена:"))
        self.label_7.setText(_translate("Form", "Объем упаковки:"))
        self.okButton.setText(_translate("Form", "Готово"))


class Coffii(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.n = 1

    def initUI(self):
        self.neww = New_coffii()
        self.nextButton.clicked.connect(self.run)
        self.redButton.clicked.connect(self.updatt)
        self.addButton.clicked.connect(self.add)

    def updatt(self):
        con = sqlite3.connect('coffi')
        cur = con.cursor()
        result = cur.execute(f"""SELECT id FROM cofe""").fetchall()
        name = self.nameEdit.text()
        fire = self.fireEdit.text()
        molot = self.pomolEdit.text()
        taste = self.tastiEdit.text()
        price = self.priseEdit.text()
        V = self.VVEdit.text()
        cur.execute(f"""UPDATE cofe
                            SET name = '{name}', fire = '{fire}', molot = '{molot}', 
                            taste = '{taste}', price = '{price}', V = '{V}'
                            WHERE id = '{int(result[0][-1]) + 1}'""")
        con.commit()

    def run(self):
        try:
            con = sqlite3.connect('coffi')
            cur = con.cursor()
            result = cur.execute(f"""SELECT * FROM cofe
                            WHERE id = '{self.n}'""").fetchall()
            self.idEdit.setText(str(result[0][0]))
            self.nameEdit.setText(str(result[0][1]))
            self.fireEdit.setText(str(result[0][2]))
            self.pomolEdit.setText(str(result[0][3]))
            self.tastiEdit.setText(str(result[0][4]))
            self.priseEdit.setText(str(result[0][5]))
            self.VVEdit.setText(str(result[0][6]))
            self.n += 1
        except IndexError:
            self.n = 1

    def add(self):
        self.neww.show()


class New_coffii(QMainWindow, Ui_Form11):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.okButton.clicked.connect(self.run)

    def run(self):
        con = sqlite3.connect('coffi')
        cur = con.cursor()
        result = cur.execute(f"""SELECT id FROM cofe""").fetchall()
        name = self.nameEdit.text()
        fire = self.fireEdit.text()
        molot = self.pomolEdit.text()
        taste = self.tastiEdit.text()
        price = self.priseEdit.text()
        V = self.VVEdit.text()
        cur.execute(f"""INSERT INTO cofe(id, name, fire, molot, taste, price, V)
            VALUES('{int(result[0][-1]) + 1}','{name}', '{fire}', '{molot}', '{taste}', '{price}', '{V}')""")
        con.commit()
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Coffii()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
