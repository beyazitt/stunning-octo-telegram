import sys
from PyQt5 import QtWidgets #Pencere ve butonlar burada

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("PyQt5 Ders 1")

    pencere.show()

    sys.exit(app.exec_())  #Bunun sayesişnde Çarpı tuşuna basmadığımız sürece uygulama çalışır.

Pencere()
