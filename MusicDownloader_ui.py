# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\cyh\musicdownloader\MusicDownloader\MusicDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MusicDownloader(object):
    def setupUi(self, MusicDownloader):
        MusicDownloader.setObjectName("MusicDownloader")
        MusicDownloader.resize(700, 350)
        MusicDownloader.setMinimumSize(QtCore.QSize(700, 350))
        MusicDownloader.setMaximumSize(QtCore.QSize(700, 350))
        self.widget = QtWidgets.QWidget(MusicDownloader)
        self.widget.setGeometry(QtCore.QRect(10, 10, 681, 331))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ModeComboBox = QtWidgets.QComboBox(self.widget)
        self.ModeComboBox.setStyleSheet("QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: lightgray;\n"
"}\n"
"QComboBox QAbstractItemView::item\n"
"{\n"
"    height:16px;\n"
"}")
        self.ModeComboBox.setObjectName("ModeComboBox")
        self.ModeComboBox.addItem("")
        self.ModeComboBox.addItem("")
        self.ModeComboBox.addItem("")
        self.ModeComboBox.addItem("")
        self.ModeComboBox.addItem("")
        self.ModeComboBox.addItem("")
        self.gridLayout.addWidget(self.ModeComboBox, 0, 0, 1, 2)
        self.UrlIdLineEdit = QtWidgets.QLineEdit(self.widget)
        self.UrlIdLineEdit.setObjectName("UrlIdLineEdit")
        self.gridLayout.addWidget(self.UrlIdLineEdit, 0, 2, 1, 1)
        self.DownloadPushButton = QtWidgets.QPushButton(self.widget)
        self.DownloadPushButton.setObjectName("DownloadPushButton")
        self.gridLayout.addWidget(self.DownloadPushButton, 0, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FrontArtistCheckBox = QtWidgets.QCheckBox(self.widget)
        self.FrontArtistCheckBox.setObjectName("FrontArtistCheckBox")
        self.horizontalLayout.addWidget(self.FrontArtistCheckBox)
        self.RearArtistCheckBox = QtWidgets.QCheckBox(self.widget)
        self.RearArtistCheckBox.setObjectName("RearArtistCheckBox")
        self.horizontalLayout.addWidget(self.RearArtistCheckBox)
        self.LyricCheckBox = QtWidgets.QCheckBox(self.widget)
        self.LyricCheckBox.setChecked(True)
        self.LyricCheckBox.setObjectName("LyricCheckBox")
        self.horizontalLayout.addWidget(self.LyricCheckBox)
        self.HDCheckBox = QtWidgets.QCheckBox(self.widget)
        self.HDCheckBox.setChecked(True)
        self.HDCheckBox.setObjectName("HDCheckBox")
        self.horizontalLayout.addWidget(self.HDCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)
        self.PrintTextEdit = QtWidgets.QTextEdit(self.widget)
        self.PrintTextEdit.setEnabled(False)
        self.PrintTextEdit.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.PrintTextEdit.setObjectName("PrintTextEdit")
        self.gridLayout.addWidget(self.PrintTextEdit, 3, 0, 1, 4)
        self.APILineEdit = QtWidgets.QLineEdit(self.widget)
        self.APILineEdit.setObjectName("APILineEdit")
        self.gridLayout.addWidget(self.APILineEdit, 1, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)

        self.retranslateUi(MusicDownloader)
        QtCore.QMetaObject.connectSlotsByName(MusicDownloader)

    def retranslateUi(self, MusicDownloader):
        _translate = QtCore.QCoreApplication.translate
        MusicDownloader.setWindowTitle(_translate("MusicDownloader", "MusicDownloader"))
        self.ModeComboBox.setItemText(0, _translate("MusicDownloader", "网易云单曲"))
        self.ModeComboBox.setItemText(1, _translate("MusicDownloader", "网易云歌单"))
        self.ModeComboBox.setItemText(2, _translate("MusicDownloader", "QQ音乐单曲"))
        self.ModeComboBox.setItemText(3, _translate("MusicDownloader", "QQ音乐歌单"))
        self.ModeComboBox.setItemText(4, _translate("MusicDownloader", "网易云专辑"))
        self.ModeComboBox.setItemText(5, _translate("MusicDownloader", "网易云歌手下载"))
        self.DownloadPushButton.setText(_translate("MusicDownloader", "下 载"))
        self.FrontArtistCheckBox.setText(_translate("MusicDownloader", "歌曲名称前加歌手"))
        self.RearArtistCheckBox.setText(_translate("MusicDownloader", "歌曲名称后加歌手"))
        self.LyricCheckBox.setText(_translate("MusicDownloader", "歌曲是否下载歌词"))
        self.HDCheckBox.setText(_translate("MusicDownloader", "歌曲启用高清封面"))
        self.PrintTextEdit.setHtml(_translate("MusicDownloader", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MusicDownloader", "歌曲API服务器："))
