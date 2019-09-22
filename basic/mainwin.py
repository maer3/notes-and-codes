# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1181, 852)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.guanbi = QtWidgets.QPushButton(self.centralwidget)
        self.guanbi.setGeometry(QtCore.QRect(980, 720, 201, 61))
        self.guanbi.setCheckable(False)
        self.guanbi.setAutoRepeat(False)
        self.guanbi.setAutoExclusive(False)
        self.guanbi.setObjectName("guanbi")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 0, 401, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/images/17a515a85edf8db1ae6b8e900e23dd54544e74c6.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(780, 310, 401, 351))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setToolTipDuration(0)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 660, 201, 61))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 781, 791))
        self.widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget.setObjectName("widget")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 781, 781))
        self.textEdit_2.setMouseTracking(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 781, 451))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/images/08d34c224f4a20a4cee5493097529822700ed097.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 410, 781, 361))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/pic/images/dae6b6dda144ad344b735b7cd7a20cf433ad8546.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 781, 781))
        self.widget_2.setObjectName("widget_2")
        self.dianying = QtWidgets.QTextBrowser(self.widget_2)
        self.dianying.setGeometry(QtCore.QRect(0, 0, 781, 281))
        self.dianying.setObjectName("dianying")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(390, 280, 391, 501))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pic/images2/785894d3ly1g5yzp61d1jj20u0197e82.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(0, 280, 391, 501))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/pic/images2/785894d3ly1g5yzp5vyfjj20u01974qs.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_3.raise_()
        self.label_2.raise_()
        self.textEdit_2.raise_()
        self.widget_2.raise_()
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 720, 201, 61))
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(980, 660, 201, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit.raise_()
        self.label.raise_()
        self.guanbi.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1181, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        icon = QtGui.QIcon.fromTheme("菜单")
        self.menu.setIcon(icon)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setToolTipsVisible(False)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setText("")
        self.action2.setObjectName("action2")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/7f6d7fdf8db1cb132d1bc0e7da54564e93584b1d.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action1_2.setIcon(icon)
        self.action1_2.setObjectName("action1_2")
        self.action2_2 = QtWidgets.QAction(MainWindow)
        self.action2_2.setObjectName("action2_2")
        self.action1_3 = QtWidgets.QAction(MainWindow)
        self.action1_3.setObjectName("action1_3")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_2)
        self.menu.addAction(self.action1_2)
        self.menu.addAction(self.action2_2)
        self.menu.addAction(self.action1_3)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.guanbi.clicked.connect(MainWindow.close)
        self.action.triggered.connect(self.widget.hide)
        self.pushButton.clicked.connect(self.textEdit_2.show)
        self.action_2.triggered.connect(self.widget.show)
        self.pushButton_3.clicked.connect(self.textEdit_2.hide)
        self.pushButton_2.clicked.connect(self.widget_2.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "罗小黑主页"))
        self.guanbi.setText(_translate("MainWindow", "关闭页面"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>。。。。</p></body></html>"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>点击查看更多</p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14pt; font-weight:600; color:#000000; background-color:#ffffff;\">《罗小黑战记》主要讲述了一个少女养猫而发生的种种离奇故事，整个作品风格很“中国式”。故事情节搞笑、</span><a href=\"https://baike.baidu.com/item/%E6%B8%A9%E9%A6%A8/5879252\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline; color:#000000; background-color:#ffffff;\">温馨</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14pt; font-weight:600; color:#000000; background-color:#ffffff;\">别致，单帧信息量庞大，画风极其可爱，惹得广大网友直呼“萌出一脸血”，堪称中国治愈系神作。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14pt; font-weight:600; color:#333333; background-color:#ffffff;\">《罗小黑战记》是中国大陆独立动画制作人</span><a href=\"https://baike.baidu.com/item/MTJJ\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14pt; font-weight:600; text-decoration: underline; color:#136ec2; background-color:#ffffff;\">MTJJ</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:14pt; font-weight:600; color:#333333; background-color:#ffffff;\">及其工作室制作的一部2D动画片，于2011年03月17日出品，播放平台主要是网络。</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "点击查看人物介绍"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#0000ff;\">人物介绍</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600; font-style:italic; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://baike.baidu.com/item/%E7%BD%97%E5%B0%8F%E9%BB%91/10712965\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:11pt; font-weight:600; text-decoration: underline; color:#000000;\">罗小黑</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:600; color:#000000;\">生日</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">：定在11月1日</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:600; color:#000000;\">种族</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">：妖精</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:600; color:#000000;\">年龄</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">：10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">能力类型：空间系-领域（已失去）、空间系-传送、御灵系-金</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">一只天真、勇敢且强大的小黑猫。实为</span><a href=\"https://baike.baidu.com/item/%E7%8C%AB%E5%A6%96/82570\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; text-decoration: underline; color:#000000;\">猫妖</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">，师从无限，不会识字。因盗取老君天明珠而被谛听打回原形。躲入纸箱中避雨误被小白捡回家，取名罗小黑。尾巴是身长的两倍，可变成翅膀，也可分裂成名为嘿咻的有意识体，随着小黑能力越强，嘿咻也会越多，现可分裂为四个，可以无限分裂，但总体积不变。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><a href=\"https://baike.baidu.com/item/%E7%BD%97%E5%B0%8F%E7%99%BD/19817163\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:11pt; font-weight:696; text-decoration: underline; color:#000000;\">罗小白</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">种族：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">人类</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">年龄：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">职业：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">学生</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">一名红领巾，善良正义，常帮好朋友山新打掩护、看护爱猫小皇。能很快亲近动物，有怪力，频繁刷新世界观。现持有法宝“蓝玉盘”（老君赠送）。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:11pt; font-weight:696; text-decoration: underline; color:#000000;\">阿根（罗根）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">种族：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">人类</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">/</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">妖精</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">能力：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">控制冰、火</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">小白的乡下堂哥，却又被众妖认作</span><a href=\"https://baike.baidu.com/item/%E4%B8%8A%E5%8F%A4%E7%A5%9E%E5%85%BD\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; text-decoration: underline; color:#000000;\">上古神兽</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">玄离（但在第21、22集否认自己是玄离，所以目前阿根与玄离关系不明）。寻常动物靠近他都会不自觉地咬他，可以吸收火焰、控制水的形态并凝结成冰（能力、特性与玄离相同），灵质空间据说是有足球场那么大的极寒地狱，可放置有独立意识的分身，妖力强大。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><a href=\"https://baike.baidu.com/item/%E6%AF%94%E4%B8%A2/19136882\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:11pt; font-weight:696; text-decoration: underline; color:#000000;\">比丢</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">生日：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">6月1日</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">种族：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">团鼠</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">特长：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">吃，跑的速度极快（克星是小黑）</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; font-weight:696; color:#000000;\">食物：</span><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">除了金属和生物外的所有东西，最喜欢吃木头</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:24px; background-color:#ffffff;\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000; background-color:#ffffff;\">基色为橘黄。团鼠在吃下一种东西后，会变成那种东西的主色，所以可以变成各种颜色，是一种对自身的保护机制，五分钟左右就会恢复原样。但也由于这样特殊的皮毛而被捕杀，所剩无几。跑到村里觅食时被阿根控制住，因“bi diu~”的叫声而被小白取名比丢并收养。看似呆呆的比丢其实很狡猾敏捷，只有小黑能制服它。因团鼠的生物特性，吃了金属和生物就会暴走（身体巨大化，变成蓝色），</span><a href=\"https://baike.baidu.com/item/%E6%9A%B4%E8%B5%B0/649\"><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; text-decoration: underline; color:#000000;\">暴走</span></a><span style=\" font-family:\'arial,宋体,sans-serif\'; font-size:12px; color:#000000;\">纹在眉心，碰一下就会变回原样，但会消耗生命。</span></p></body></html>"))
        self.dianying.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#0000ff;\">电影介绍</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#111111; background-color:#ffffff;\">在熙攘的人类世界里，很多妖精隐匿其中，他们与人类相安无事地生活着。猫妖罗小黑因为家园被破坏，开始了它的流浪之旅。这场旅途中惺惺相惜的妖精同类与和谐包容的人类伙伴相继出现，让小黑陷入了两难抉择，究竟何处才是真正的归属？</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#111111;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\">导演: </span><a href=\"https://movie.douban.com/celebrity/1379633/\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">木头</span></a><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> 编剧: </span><a href=\"https://movie.douban.com/celebrity/1379633/\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">木头</span></a><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> 主演: 山新 / </span><a href=\"https://movie.douban.com/celebrity/1340968/\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">郝祥海</span></a><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> / </span><a href=\"https://movie.douban.com/celebrity/1381516/\"><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">刘明月</span></a><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000; background-color:#ffffff;\">类型:</span><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> 动作 / 动画 / 奇幻 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000; background-color:#ffffff;\">制片国家/地区:</span><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> 中国大陆 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000; background-color:#ffffff;\">语言:</span><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> 汉语普通话 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000; background-color:#ffffff;\">上映日期:</span><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> 2019-09-07(中国大陆) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#000000; background-color:#ffffff;\">片长:</span><span style=\" font-family:\'Helvetica,Arial,sans-serif\'; font-size:11pt; color:#000000; background-color:#ffffff;\"> 101分钟</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "点击查看电影介绍"))
        self.pushButton_3.setText(_translate("MainWindow", "点击关闭人物介绍"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action1.setText(_translate("MainWindow", "打开"))
        self.action1_2.setText(_translate("MainWindow", "介绍"))
        self.action2_2.setText(_translate("MainWindow", "剧集"))
        self.action1_3.setText(_translate("MainWindow", "电影"))
        self.action.setText(_translate("MainWindow", "隐藏窗口"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_2.setText(_translate("MainWindow", "展示窗口"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+S"))

import dianying
import resource
