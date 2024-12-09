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
        self.pushButton.clicked.connect(self.run)

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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Coffii()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
