# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lmsbookedit.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BookEdit(object):
    def setupUi(self, BookEdit):
        BookEdit.setObjectName(_fromUtf8("BookEdit"))
        BookEdit.resize(509, 385)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BookEdit.setWindowIcon(icon)
        BookEdit.setStyleSheet(_fromUtf8(""))
        self.book_edit_title = QtGui.QLineEdit(BookEdit)
        self.book_edit_title.setGeometry(QtCore.QRect(150, 100, 221, 32))
        self.book_edit_title.setObjectName(_fromUtf8("book_edit_title"))
        self.book_edit_publisher = QtGui.QLineEdit(BookEdit)
        self.book_edit_publisher.setGeometry(QtCore.QRect(150, 180, 221, 32))
        self.book_edit_publisher.setInputMethodHints(QtCore.Qt.ImhNone)
        self.book_edit_publisher.setObjectName(_fromUtf8("book_edit_publisher"))
        self.book_edit_author = QtGui.QLineEdit(BookEdit)
        self.book_edit_author.setGeometry(QtCore.QRect(150, 140, 221, 32))
        self.book_edit_author.setInputMethodHints(QtCore.Qt.ImhNone)
        self.book_edit_author.setObjectName(_fromUtf8("book_edit_author"))
        self.book_edit_available = QtGui.QCheckBox(BookEdit)
        self.book_edit_available.setGeometry(QtCore.QRect(150, 260, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.book_edit_available.setFont(font)
        self.book_edit_available.setChecked(False)
        self.book_edit_available.setTristate(False)
        self.book_edit_available.setObjectName(_fromUtf8("book_edit_available"))
        self.book_edit_copies = QtGui.QLineEdit(BookEdit)
        self.book_edit_copies.setGeometry(QtCore.QRect(150, 220, 221, 32))
        self.book_edit_copies.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.book_edit_copies.setText(_fromUtf8(""))
        self.book_edit_copies.setObjectName(_fromUtf8("book_edit_copies"))
        self.label_2 = QtGui.QLabel(BookEdit)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 51, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtGui.QFrame.Plain)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(BookEdit)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 71, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(BookEdit)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 91, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtGui.QFrame.Plain)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(BookEdit)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 121, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtGui.QFrame.Plain)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(BookEdit)
        self.label_6.setGeometry(QtCore.QRect(190, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_6.setFrameShadow(QtGui.QFrame.Plain)
        self.label_6.setLineWidth(1)
        self.label_6.setMidLineWidth(0)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.book_edit_btn = QtGui.QPushButton(BookEdit)
        self.book_edit_btn.setGeometry(QtCore.QRect(320, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.book_edit_btn.setFont(font)
        self.book_edit_btn.setAutoDefault(True)
        self.book_edit_btn.setFlat(False)
        self.book_edit_btn.setObjectName(_fromUtf8("book_edit_btn"))
        self.book_edit_cancel_btn = QtGui.QPushButton(BookEdit)
        self.book_edit_cancel_btn.setGeometry(QtCore.QRect(220, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.book_edit_cancel_btn.setFont(font)
        self.book_edit_cancel_btn.setAutoDefault(True)
        self.book_edit_cancel_btn.setObjectName(_fromUtf8("book_edit_cancel_btn"))
        self.book_delete_btn = QtGui.QPushButton(BookEdit)
        self.book_delete_btn.setGeometry(QtCore.QRect(120, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.book_delete_btn.setFont(font)
        self.book_delete_btn.setCheckable(False)
        self.book_delete_btn.setAutoDefault(True)
        self.book_delete_btn.setObjectName(_fromUtf8("book_delete_btn"))
        self.book_edit_error = QtGui.QLabel(BookEdit)
        self.book_edit_error.setGeometry(QtCore.QRect(150, 289, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_edit_error.setFont(font)
        self.book_edit_error.setText(_fromUtf8(""))
        self.book_edit_error.setObjectName(_fromUtf8("book_edit_error"))
        self.book_edit_id = QtGui.QLineEdit(BookEdit)
        self.book_edit_id.setGeometry(QtCore.QRect(150, 60, 221, 32))
        self.book_edit_id.setReadOnly(True)
        self.book_edit_id.setObjectName(_fromUtf8("book_edit_id"))
        self.label = QtGui.QLabel(BookEdit)
        self.label.setGeometry(QtCore.QRect(100, 60, 31, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(BookEdit)
        QtCore.QMetaObject.connectSlotsByName(BookEdit)

    def retranslateUi(self, BookEdit):
        BookEdit.setWindowTitle(_translate("BookEdit", "MeX LMS - Edit book", None))
        self.book_edit_title.setPlaceholderText(_translate("BookEdit", "Title", None))
        self.book_edit_publisher.setPlaceholderText(_translate("BookEdit", "Publisher", None))
        self.book_edit_author.setPlaceholderText(_translate("BookEdit", "Author", None))
        self.book_edit_available.setText(_translate("BookEdit", "Available", None))
        self.book_edit_copies.setPlaceholderText(_translate("BookEdit", "No. of copies", None))
        self.label_2.setText(_translate("BookEdit", "Title", None))
        self.label_3.setText(_translate("BookEdit", "Author", None))
        self.label_4.setText(_translate("BookEdit", "Publisher", None))
        self.label_5.setText(_translate("BookEdit", "No. of copies", None))
        self.label_6.setText(_translate("BookEdit", "Edit Book", None))
        self.book_edit_btn.setText(_translate("BookEdit", "Save", None))
        self.book_edit_cancel_btn.setText(_translate("BookEdit", "Close", None))
        self.book_delete_btn.setText(_translate("BookEdit", "Delete", None))
        self.book_edit_id.setPlaceholderText(_translate("BookEdit", "ID", None))
        self.label.setText(_translate("BookEdit", "ID", None))

