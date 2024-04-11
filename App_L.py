from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call
import webbrowser

url_try = "https://colab.research.google.com/"
url_plot = url = "http://localhost:8888/notebooks/Plot.ipynb"
url_quiz = "http://localhost:8888/notebooks/Quiz.ipynb"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/ico/MyPY.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(340, 10, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_title.setObjectName("label_title")
        self.label_tagline = QtWidgets.QLabel(self.centralwidget)
        self.label_tagline.setGeometry(QtCore.QRect(338, 100, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(14)
        self.label_tagline.setFont(font)
        self.label_tagline.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_tagline.setObjectName("label_tagline")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 140, 991, 20))
        self.line.setStyleSheet("color : rgb(35, 35, 35)")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_hello = QtWidgets.QLabel(self.centralwidget)
        self.label_hello.setGeometry(QtCore.QRect(10, 160, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_hello.setFont(font)
        self.label_hello.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_hello.setObjectName("label_hello")
        self.label_learn = QtWidgets.QLabel(self.centralwidget)
        self.label_learn.setGeometry(QtCore.QRect(10, 200, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_learn.setFont(font)
        self.label_learn.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_learn.setObjectName("label_learn")
        self.pushButton_bar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bar.setGeometry(QtCore.QRect(10, 240, 93, 28))
        self.pushButton_bar.setStyleSheet("color: rgb(35, 35, 35);\n"
"")
        self.pushButton_bar.setObjectName("pushButton_bar")
        self.pushButton_box = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_box.setGeometry(QtCore.QRect(140, 240, 93, 28))
        self.pushButton_box.setStyleSheet("color: rgb(35, 35, 35);")
        self.pushButton_box.setObjectName("pushButton_box")
        self.pushButton_freq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_freq.setGeometry(QtCore.QRect(270, 240, 141, 28))
        self.pushButton_freq.setStyleSheet("color: rgb(35, 35, 35);")
        self.pushButton_freq.setObjectName("pushButton_freq")
        self.pushButton_hist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_hist.setGeometry(QtCore.QRect(450, 240, 93, 28))
        self.pushButton_hist.setStyleSheet("color: rgb(35, 35, 35);")
        self.pushButton_hist.setObjectName("pushButton_hist")
        self.pushButton_line = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_line.setGeometry(QtCore.QRect(580, 240, 93, 28))
        self.pushButton_line.setStyleSheet("color: rgb(35, 35, 35);")
        self.pushButton_line.setObjectName("pushButton_line")
        self.pushButton_pie = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pie.setGeometry(QtCore.QRect(710, 240, 93, 28))
        self.pushButton_pie.setStyleSheet("color: rgb(35, 35, 35);")
        self.pushButton_pie.setObjectName("pushButton_pie")
        self.pushButton_scat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_scat.setGeometry(QtCore.QRect(840, 240, 93, 28))
        self.pushButton_scat.setStyleSheet("color: rgb(35, 35, 35);")
        self.pushButton_scat.setObjectName("pushButton_scat")
        self.pushButton_about = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_about.setGeometry(QtCore.QRect(900, 160, 93, 28))
        self.pushButton_about.setStyleSheet("color: rgb(35, 35, 35);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(35, 0, 0, 35));")
        self.pushButton_about.setObjectName("pushButton_about")

        self.pushButton_dark = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dark.setGeometry(QtCore.QRect(790, 160, 93, 28))
        self.pushButton_dark.setObjectName("pushButton_dark")
        self.pushButton_dark.setStyleSheet("color: rgb(35, 35, 35);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(35, 0, 0, 35));")
        self.pushButton_dark.setObjectName("pushButton_dark")

        self.pushButton_try = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_try.setGeometry(QtCore.QRect(680, 160, 93, 28))
        self.pushButton_try.setObjectName("pushButton_try")
        self.pushButton_try.setStyleSheet("color: rgb(35, 35, 35);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(225, 0, 0, 225));")
        self.pushButton_try.setObjectName("pushButton_try")

        self.pushButton_quiz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quiz.setGeometry(QtCore.QRect(570, 160, 93, 28))
        self.pushButton_quiz.setObjectName("pushButton_quiz")
        self.pushButton_quiz.setStyleSheet("color: rgb(35, 35, 35);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(225, 0, 0, 225));")
        self.pushButton_quiz.setObjectName("pushButton_quiz")

        self.pushButton_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plot.setGeometry(QtCore.QRect(460, 160, 93, 28))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.pushButton_plot.setStyleSheet("color: rgb(35, 35, 35);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(225, 0, 0, 225));")
        self.pushButton_plot.setObjectName("pushButton_plot")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(14, 285, 971, 431))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("test.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_quiz.clicked.connect(self.show_pushButton_quiz)
        self.pushButton_plot.clicked.connect(self.show_pushButton_plot)
        self.pushButton_dark.clicked.connect(self.show_pushButton_dark)
        self.pushButton_about.clicked.connect(self.show_pushButton_about)
        self.pushButton_bar.clicked.connect(self.show_pushButton_bar)
        self.pushButton_box.clicked.connect(self.show_pushButton_box)
        self.pushButton_freq.clicked.connect(self.show_pushButton_freq)
        self.pushButton_hist.clicked.connect(self.show_pushButton_hist)
        self.pushButton_line.clicked.connect(self.show_pushButton_line)
        self.pushButton_pie.clicked.connect(self.show_pushButton_pie)
        self.pushButton_scat.clicked.connect(self.show_pushButton_scat)
        self.pushButton_try.clicked.connect(self.show_pushButton_try)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyPY App"))
        self.label_title.setText(_translate("MainWindow", "MyPY App"))
        self.label_tagline.setText(_translate("MainWindow", "~ A Probono Platfrom"))
        self.label_hello.setText(_translate("MainWindow", "Hello, Welcome back!"))
        self.label_learn.setText(_translate("MainWindow", "What would you like to learn today?"))
        self.pushButton_bar.setText(_translate("MainWindow", "Bar Graph"))
        self.pushButton_box.setText(_translate("MainWindow", "Box Plot"))
        self.pushButton_freq.setText(_translate("MainWindow", "Frequency Polygon"))
        self.pushButton_hist.setText(_translate("MainWindow", "Histogram"))
        self.pushButton_line.setText(_translate("MainWindow", "Line Graph"))
        self.pushButton_pie.setText(_translate("MainWindow", "Pie Chart"))
        self.pushButton_scat.setText(_translate("MainWindow", "Scatter Chart"))
        self.pushButton_about.setText(_translate("MainWindow", "About"))
        self.pushButton_dark.setText(_translate("MainWindow", "Dark Mode"))
        self.pushButton_try.setText(_translate("MainWindow", "Try It Yourself"))
        self.pushButton_quiz.setText(_translate("MainWindow", "Quiz"))
        self.pushButton_plot.setText(_translate("MainWindow", "Plot Graphs"))

    def show_pushButton_about(self):
        self.photo.setPixmap(QtGui.QPixmap("res/misc/about_l.jpg"))

    def show_pushButton_bar(self):
        self.photo.setPixmap(QtGui.QPixmap("res/img/light/bar.jpg"))

    def show_pushButton_box(self):
        self.photo.setPixmap(QtGui.QPixmap("res/img/light/box.jpg"))

    def show_pushButton_freq(self):
        self.photo.setPixmap(QtGui.QPixmap("res/img/light/freq.jpg"))

    def show_pushButton_hist(self):
        self.photo.setPixmap(QtGui.QPixmap("res/img/light/hist.jpg"))

    def show_pushButton_line(self):
        self.photo.setPixmap(QtGui.QPixmap("res/img/light/line.jpg"))

    def show_pushButton_pie(self):
        self.photo.setPixmap(QtGui.QPixmap("res/img/light/pie.jpg"))

    def show_pushButton_scat(self):
        self.photo.setPixmap(QtGui.QPixmap("res/img/light/scatter.jpg"))

    def show_pushButton_dark(self):
        call(["python", "App_D.py"])

    def show_pushButton_try(self):
        webbrowser.get(chrome_path).open(url_try)

    def show_pushButton_quiz(self):
        webbrowser.get(chrome_path).open(url_quiz)

    def show_pushButton_plot(self):
        webbrowser.get(chrome_path).open(url_plot)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
