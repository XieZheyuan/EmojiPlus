from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QMessageBox,QFileDialog,QInputDialog
import sys
import os
from imagetotext import to
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setWindowTitle("Emoji++")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 601, 391))
        self.textEdit.setObjectName("textEdit")
        self.fn = QtWidgets.QLabel(self.centralwidget)
        self.fn.setGeometry(QtCore.QRect(10, 420, 121, 16))
        self.fn.setObjectName("fn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_N = QtWidgets.QAction(MainWindow)
        self.action_N.setObjectName("action_N")
        self.action_O = QtWidgets.QAction(MainWindow)
        self.action_O.setObjectName("action_O")
        self.action_I = QtWidgets.QAction(MainWindow)
        self.action_I.setObjectName("action_I")
        self.actionQuit_Q = QtWidgets.QAction(MainWindow)
        self.actionQuit_Q.setObjectName("actionQuit_Q")
        self.action_A = QtWidgets.QAction(MainWindow)
        self.action_A.setObjectName("action_A")
        self.actionS = QtWidgets.QAction(MainWindow)
        self.actionS.setObjectName("actionQuit_Q_2")
        self.action_T = QtWidgets.QAction(MainWindow)
        self.action_T.setObjectName("action_T")
        self.action_Y = QtWidgets.QAction(MainWindow)
        self.action_Y.setObjectName("action_Y")
        self.action_N.setText("新建(&N)")
        self.action_N.setShortcut("Ctrl+N")
        self.action_X=QtWidgets.QAction(MainWindow)
        self.action_X.setText("希腊语(&X)")
        self.action_X.setShortcut("Ctrl+Shift+X")
        self.action_P=QtWidgets.QAction(MainWindow)
        self.action_P.setText("注音符号(&P)")
        self.action_P.setShortcut("Ctrl+Shift+P")
        self.action_L = QtWidgets.QAction(MainWindow)
        self.action_L.setText("拉丁语(&L)")
        self.action_L.setShortcut("Ctrl+Shift+L")
        self.action_C = QtWidgets.QAction(MainWindow)
        self.action_C.setText("清空(&C)")
        self.action_C.setShortcut("Ctrl+Shift+C")

        self.menu_F.addAction(self.action_N)
        self.menu_F.addAction(self.action_O)
        self.menu_F.addAction(self.action_I)
        self.menu_F.addAction(self.actionQuit_Q)
        self.menu_F.addAction(self.action_A)
        self.menu_F.addAction(self.actionS)

        self.menu_E.addAction(self.action_T)
        self.menu_E.addAction(self.action_Y)

        self.menu_E.addAction(self.action_X)
        self.menu_E.addAction(self.action_P)
        self.menu_E.addAction(self.action_L)
        self.menu_E.addAction(self.action_C)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.fn.setText(_translate("MainWindow", "Untitled.emoji"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "插入(&E)"))
        self.action_O.setText(_translate("MainWindow", "打开(&O)"))
        self.action_O.setToolTip(_translate("MainWindow", "打开一个EMOJI文件"))
        self.action_O.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_I.setText(_translate("MainWindow", "打开来自图片(&I)"))
        self.action_I.setToolTip(_translate("MainWindow", "打开来自图片的文件"))
        self.action_I.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionS.setText(_translate("MainWindow", "保存(&S)"))
        self.actionS.setToolTip(_translate("MainWindow", "保存为EMOJI文件"))
        self.actionS.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_A.setText(_translate("MainWindow", "另存为……(&A)"))
        self.action_A.setToolTip(_translate("MainWindow", "另存为EMOJII文件"))
        self.action_A.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionQuit_Q.setText(_translate("MainWindow", "Quit(&Q)"))
        self.action_T.setText(_translate("MainWindow", "特殊字符(&T)"))
        self.action_T.setToolTip(_translate("MainWindow", "打开特殊字符选项卡"))
        self.action_T.setShortcut(_translate("MainWindow", "Ctrl+Shift+T"))
        self.action_Y.setText(_translate("MainWindow", "颜文字模板(&Y)"))
        self.action_Y.setToolTip(_translate("MainWindow", "颜文字模板"))
        self.action_Y.setShortcut(_translate("MainWindow", "Ctrl+Shift+Y"))

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.filename="Untitled.emojji"
        self.fd=""
        self.actionQuit_Q.triggered.connect(self.quit_)
        self.action_N.triggered.connect(self.new)
        self.action_I.triggered.connect(self.image)
        self.action_A.triggered.connect(self.saveAs)
        self.action_O.triggered.connect(self.Open)
        self.actionS.triggered.connect(self.save)
        self.action_T.triggered.connect(self.chars)
        self.action_Y.triggered.connect(self.yan)
        self.action_X.triggered.connect(self.xila)
        self.action_P.triggered.connect(self.zhuyin)
        self.action_L.triggered.connect(self.latin)
        self.action_C.triggered.connect(self.copy)
    def new(self):
        self.textEdit.clear()
        self.filename = "Untitled.emoji"
        self.fd=""
        self.fn.setText(self.filename)
        QMessageBox.information(self,"Emoji++","新建文件完成")
    def image(self):
        s=QFileDialog.getOpenFileName(self,"选择一个图片",
                              os.getcwd(),
                              "支持的图片文件(*.jpg *.jpeg *.jff *.png *.bmp *.tif *.tiff)"
                              )[0]

        if(s != "" or s != None):
            self.s=to(s)

            self.textEdit.setText(self.s)

    def saveAs(self):
        v=self.textEdit.toPlainText()

        s=QFileDialog.getSaveFileName(
            self,
            "另存为",
            os.getcwd(),
            "Emoji++文档(*.emoji *.txt)"
        )[0]
        self.fd=s
        with open(s,"w") as f:
            f.write(v)
        self.fn.setText(os.path.split(s)[1])
    def save(self):
        v=self.textEdit.toPlainText()

        if(self.fd == ""):
            s = QFileDialog.getSaveFileName(
                self,
                "另存为",
                os.getcwd(),
                "Emoji++文档(*.emoji *.txt)"
            )[0]
            self.fd=s
        else:
            s=self.fd
        with open(s,"w") as f:
            f.write(v)
        self.fn.setText(os.path.split(s)[1])

    def Open(self):
        s = QFileDialog.getOpenFileName(
            self,
            "打开",
            os.getcwd(),
            "Emoji++文档(*.emoji *.txt)"
        )[0]
        with open(s,"r") as f:
            v=f.read()
        self.textEdit.setText(v)
        self.fn.setText(os.path.split(s)[1])
        self.fd=s
    def chars(self):
        ch=("△","∶","∵","∴","∷","∑","∏","￥",
            "＋","－","×","÷","＝","＜","＞","≤","≥",
            "≈","≒","≠","∝","∽","∈","∩","∧","⊙","⌒","∥",
            "∟","∣","∞","≌","∉","∪","∨","⊿","⊕","⊥","∠","∫",
            "∮","℅","‰","℃","℉","〒","′","″",
            "▽","○","◇","□","☆","▷","◁","♤","♡","♢","♧","☼","☽",
            "☾","♀","♂","▁","▃","▅","█","▏","▌","▉",
            "∷","※","▓","♩","♪","♫","♬","§","〼","◎","¤","۞",
            "♭","℗","®","©","℡","™","♯","♮","‖","¶","卍","卐","▬","〓","☊"
            )
        item,ok=QInputDialog.getItem(self,"Emoji++","选取一个符号",ch)
        if(item and ok):
            self.textEdit.insertPlainText(item)

    def yan(self):
        ch=(
            "w(ﾟДﾟ)w",
            "(ノへ￣、)",
            "(￣_,￣ )",
            "ヽ(✿ﾟ▽ﾟ)ノ",
            "(๑•̀ㅂ•́)و✧",
            "（づ￣3￣）づ╭❤～",
            "(￣ε(#￣)☆╰╮o(￣皿￣///)",
            "Σ( ° △ °|||)︴",
            "(～￣(OO)￣)ブ",
            "凸(艹皿艹 )",
            "(* ￣3)(ε￣ *)",
            "(*￣rǒ￣)",
            "┗|｀O′|┛ 嗷~~",
            "φ(≧ω≦*)♪",
            "︿(￣︶￣)︿",
            "Hi~ o(*￣▽￣*)ブ",
            "♪(^∇^*)",
            "o(*≧▽≦)ツ┏━┓",
            "╰(*°▽°*)╯",
            "----更多颜文字----"
        )
        item, ok = QInputDialog.getItem(self, "Emoji++", "选取一个颜文字", ch)
        if (item and ok):

            if(item != "----更多颜文字----"):
                self.textEdit.insertPlainText(item)
            else:
                webbrowser.open("http://www.yanwenzi.com/changyong/")
    def xila(self):
        ch=("ς","ε","ρ","τ","υ","θ","ι","ο",
            "π","α","σ","δ","φ","γ","η","ξ",
            "κ","λ","ζ","χ","ψ","ω","β","ν",
            "μ",
            "Ε","Ρ","Τ","Υ","Θ","Ι","Ο","Π",
            "Α","Σ","Δ","Φ","Γ","Η","Ξ","Κ",
            "Λ","Ζ","Χ","Ψ","Ω","Β","Ν","Μ")

        item, ok = QInputDialog.getItem(self, "Emoji++", "选取一个字母", ch)
        if (item and ok):


            self.textEdit.insertPlainText(item)



    def zhuyin(self):
        ch=(
            "ā","á","ǎ","à","ō","ó","ǒ","ò",
            "ê","ē","é","ě","è",
            "ī","í","ǐ","ì","ū","ú","ǔ","ù",
            "ǖ","ǘ","ǚ","ǜ","ü","ń","ň","",
            "",
            "ㄚ","ㄛ","ㄜ","ㄧ","ㄨ","ㄩ","ㄝ","ㄞ",
            "ㄟ","ㄠ","ㄡ","ㄢ","ㄣ","ㄤ","ㄥ","ㄦ",
            "ㄅ","ㄆ","ㄇ","ㄈ","ㄉ","ㄊ","ㄋ","ㄌ",
            "ㄍ","ㄎ","ㄏ","ㄐ","ㄑ","ㄒ","ㄓ","ㄔ",
            "ㄕ","ㄖ","ㄗ","ㄘ","ㄙ"
        )

        item, ok = QInputDialog.getItem(self, "Emoji++", "选取一个注音符号", ch)
        if (item and ok):
            self.textEdit.insertPlainText(item)

    def latin(self):
        ch=(
            "À","Á","Â","Ã","Ä","Å","Æ","Ç",
            "È","É","Ê","Ë","Ì","Í","Î","Ï",
            "Ð","Ñ","Ò","Ó","Ô","Õ","Ö","Ø",
            "Ù","Ú","Û","Ü","Ý","Þ","Š","Ÿ",
            "Œ"
        )

        item, ok = QInputDialog.getItem(self, "Emoji++", "选取一个拉丁字母", ch)
        if (item and ok):
            self.textEdit.insertPlainText(item)

    def copy(self):
        self.textEdit.clear()
    def quit_(self):
        exit(0)
if __name__ == '__main__':
    app = QApplication([])
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())