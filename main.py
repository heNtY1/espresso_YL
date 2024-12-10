import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Coffii(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.n = 1

    def initUI(self):
        uic.loadUi('main.ui', self)
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


class New_coffii(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('addEditCoffeeForm.ui', self)
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
