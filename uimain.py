from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QMessageBox,QFileDialog,QInputDialog
import sys
import os
from imagetotext import to
import webbrowser
from . import ui

class MyWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.filename="Untitled.emojji"
        self.fd=""
        self.actionQuit_Q.triggered.connect(quit)
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
        self.filename = "Untitled.emojji"
        self.fd=""
        self.fn.setText(self.filename)
        QMessageBox.information(self,"Emojji++","新建文件完成")
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
            "Emojji++文档(*.emojji *.txt)"
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
            "Emojji++文档(*.emoji *.txt)"
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
        item,ok=QInputDialog.getItem(self,"Emojji++","选取一个符号",ch)
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
        item, ok = QInputDialog.getItem(self, "Emojji++", "选取一个颜文字", ch)
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

        item, ok = QInputDialog.getItem(self, "Emojji++", "选取一个字母", ch)
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

        item, ok = QInputDialog.getItem(self, "Emojji++", "选取一个注音符号", ch)
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

        item, ok = QInputDialog.getItem(self, "Emojji++", "选取一个拉丁字母", ch)
        if (item and ok):
            self.textEdit.insertPlainText(item)
    def copy(self):
        self.textEdit.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())