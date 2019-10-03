from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pyautogui

db=sqlite3.connect('blackspot.db')
cr=db.cursor()

class Ui_MainWindow(object):
    def click(self):
        self.label_3.show()
        x,y = pyautogui.position()
        self.label_3.move(x-20,y-50)
        #print('normal ',x,'  ',y)
        xc = []
        yc = []
        cr.execute('select x,y from coordinates')
        for row in cr.fetchall():
            xc.append(row [0])
            yc.append(row [1])
        x2 = min(xc,key = lambda x1:abs(x1-x))
        y2 = min(yc,key = lambda y1:abs(y1-y))
        #print('cal ',x2,'  ',y2)
        cr.execute('select place from coordinates where x=?',(x2,))
        self.lineEdit.setText(str(cr.fetchone())[2:-3]) 
        spot = self.lineEdit.text()
        #print(spot)
        
        xn = []
        yn = []
        cr.execute('select x,y from coordinates where place=?',(spot,))
        for row1 in cr.fetchall():
            xn.append(row1 [0])
            yn.append(row1 [1])
            
        xn1 = xn[1:-1] 
        yn1 = yn[1:-1]
        
        self.label_4.show()
        if(spot == 'SAMBAJI CHOWK'):
            self.label_4.move(607-20,412-50)
        elif(spot == 'AKURDI RAILWAY STATION'):
            self.label_4.move(442-20,419-50)
        elif(spot == 'AKURDI CHOWK'):
            self.label_4.move(1012-20,380-50)
        elif(spot == 'DY PATIL COLLEGE RD'):
            self.label_4.move(266-20,501-50)
        elif(spot == 'MAHALSAKANT CHOWK'):
            self.label_4.move(754-20,406-50)
        elif(spot == 'THERMAX ENERGY HOUSE'):
            self.label_4.move(1246-20,316-50)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1371, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1371, 541))
        self.widget.setStyleSheet("background-image: url(E:/Project/Python/img/1.png);")
        self.widget.setObjectName("widget")   
        self.widget.mouseReleaseEvent=lambda event: self.click()
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(400, 270, 21, 31))
        self.label_3.setStyleSheet("image: url(E:/Project/Python/img/drop.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.hide()
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(210, 30, 21, 21))
        self.label_4.setStyleSheet("image: url(E:/Project/Python/img/dot.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.label_4.move(100,100)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 580, 411, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(670, 580, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-90, 540, 1461, 141))
        self.label_2.setStyleSheet("background-image: url(E:/Project/Python/img/regis.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nearest Black Spot from your current location is :-</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
