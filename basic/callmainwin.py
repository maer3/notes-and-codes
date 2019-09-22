# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore,QtGui
from mainwin import Ui_MainWindow

class mymainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(mymainwindow,self).__init__(parent)
        self.setupUi(self)
        self.widget.hide()
        self.textEdit_2.hide()
        self.action1_2.triggered.connect(self.openUrl)
        self.action2_2.triggered.connect(self.juji)
        self.action1_3.triggered.connect(self.yugao)
        self.widget_2.hide()

    def yugao(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://movie.douban.com/trailer/251878/'))

    def openUrl(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://baike.baidu.com/item/%E7%BD%97%E5%B0%8F%E9%BB%91%E6%88%98%E8%AE%B0/8383472?fr=aladdin'))

    def juji(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://www.bilibili.com/bangumi/play/ep32374/?share_medium=web&share_source=qq&bbid=5758CC01-5759-40AE-970F-FE1CDF5DE9A31613infoc&ts=1568732453499'))

    def center(self):

        screen = QDesktopWidget().screenGeometry()#获取屏幕坐标系
        size = self.geometry()#获取窗口坐标
        newleft = (screen.width() - size.width()) / 2
        newtop = (screen.height() - size.height()) / 2

        self.move(newleft.newtop)


   # def rewujieshao(self):

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('images/tubiao1.ico'))
    mywin = mymainwindow()
    mywin.show()
    sys.exit(app.exec_())