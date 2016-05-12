# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'complex.ui'
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

class Ui_PSafe(object):
    def setupUi(self, PSafe):
        PSafe.setObjectName(_fromUtf8("PSafe"))
        PSafe.resize(413, 727)
        PSafe.setStyleSheet(_fromUtf8("font: 8pt \"Lucida Sans\";\n"
"\n"
"background-color:     rgba(238, 238, 238);\n"
""))
        PSafe.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(PSafe)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.csv_button = QtGui.QToolButton(self.centralwidget)
        self.csv_button.setObjectName(_fromUtf8("csv_button"))
        self.verticalLayout.addWidget(self.csv_button)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.Serv_label = QtGui.QLabel(self.centralwidget)
        self.Serv_label.setObjectName(_fromUtf8("Serv_label"))
        self.verticalLayout.addWidget(self.Serv_label)
        self.Serv_lnedit = QtGui.QLineEdit(self.centralwidget)
        self.Serv_lnedit.setObjectName(_fromUtf8("Serv_lnedit"))
        self.verticalLayout.addWidget(self.Serv_lnedit)
        self.urllabel = QtGui.QLabel(self.centralwidget)
        self.urllabel.setObjectName(_fromUtf8("urllabel"))
        self.verticalLayout.addWidget(self.urllabel)
        self.url_linedit = QtGui.QLineEdit(self.centralwidget)
        self.url_linedit.setObjectName(_fromUtf8("url_linedit"))
        self.verticalLayout.addWidget(self.url_linedit)
        self.key_label = QtGui.QLabel(self.centralwidget)
        self.key_label.setObjectName(_fromUtf8("key_label"))
        self.verticalLayout.addWidget(self.key_label)
        self.auth_lineedit = QtGui.QLineEdit(self.centralwidget)
        self.auth_lineedit.setText(_fromUtf8(""))
        self.auth_lineedit.setObjectName(_fromUtf8("auth_lineedit"))
        self.verticalLayout.addWidget(self.auth_lineedit)
        self.Build_tbutton = QtGui.QToolButton(self.centralwidget)
        self.Build_tbutton.setStyleSheet(_fromUtf8("background-color: rgb(102,178,255);"))
        self.Build_tbutton.setObjectName(_fromUtf8("Build_tbutton"))
        self.verticalLayout.addWidget(self.Build_tbutton)
        self.datalabel = QtGui.QLabel(self.centralwidget)
        self.datalabel.setObjectName(_fromUtf8("datalabel"))
        self.verticalLayout.addWidget(self.datalabel)
        self.data_linedit = QtGui.QLineEdit(self.centralwidget)
        self.data_linedit.setObjectName(_fromUtf8("data_linedit"))
        self.verticalLayout.addWidget(self.data_linedit)
        self.get_button = QtGui.QPushButton(self.centralwidget)
        self.get_button.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(102,178,255);"))
        self.get_button.setObjectName(_fromUtf8("get_button"))
        self.verticalLayout.addWidget(self.get_button)
        self.post_button = QtGui.QPushButton(self.centralwidget)
        self.post_button.setStyleSheet(_fromUtf8("background-color: rgb(102,178,255);"))
        self.post_button.setObjectName(_fromUtf8("post_button"))
        self.verticalLayout.addWidget(self.post_button)
        self.put_button = QtGui.QPushButton(self.centralwidget)
        self.put_button.setStyleSheet(_fromUtf8("background-color: rgb(102,178,255);"))
        self.put_button.setObjectName(_fromUtf8("put_button"))
        self.verticalLayout.addWidget(self.put_button)
        self.del_button = QtGui.QPushButton(self.centralwidget)
        self.del_button.setStyleSheet(_fromUtf8("background-color: rgb(102,178,255);"))
        self.del_button.setObjectName(_fromUtf8("del_button"))
        self.verticalLayout.addWidget(self.del_button)
        self.filepath_label = QtGui.QLabel(self.centralwidget)
        self.filepath_label.setObjectName(_fromUtf8("filepath_label"))
        self.verticalLayout.addWidget(self.filepath_label)
        self.browse_tbutton = QtGui.QToolButton(self.centralwidget)
        self.browse_tbutton.setStyleSheet(_fromUtf8("background-color: rgb(102,178,255);"))
        self.browse_tbutton.setObjectName(_fromUtf8("browse_tbutton"))
        self.verticalLayout.addWidget(self.browse_tbutton)
        self.pathlinedit = QtGui.QLineEdit(self.centralwidget)
        self.pathlinedit.setObjectName(_fromUtf8("pathlinedit"))
        self.verticalLayout.addWidget(self.pathlinedit)
        self.importbutton = QtGui.QPushButton(self.centralwidget)
        self.importbutton.setStyleSheet(_fromUtf8("background-color: rgb(102,178,255);"))
        self.importbutton.setObjectName(_fromUtf8("importbutton"))
        self.verticalLayout.addWidget(self.importbutton)
        PSafe.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PSafe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 413, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PSafe.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PSafe)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PSafe.setStatusBar(self.statusbar)

        self.retranslateUi(PSafe)
        QtCore.QMetaObject.connectSlotsByName(PSafe)

    def retranslateUi(self, PSafe):
        PSafe.setWindowTitle(_translate("PSafe", "Psafe_Test", None))
        self.label.setText(_translate("PSafe", "<html><head/><body><p><span style=\" font-weight:600;\">Test Results</span></p></body></html>", None))
        self.csv_button.setText(_translate("PSafe", "Csv_sample", None))
        self.Serv_label.setText(_translate("PSafe", "<html><head/><body><p><span style=\" font-weight:600;\">Server Name</span></p></body></html>", None))
        self.Serv_lnedit.setPlaceholderText(_translate("PSafe", "eg.btu-bi", None))
        self.urllabel.setText(_translate("PSafe", "<html><head/><body><p><span style=\" font-weight:600;\">Url</span></p></body></html>", None))
        self.url_linedit.setPlaceholderText(_translate("PSafe", "Requests/Release/1", None))
        self.key_label.setText(_translate("PSafe", "<html><head/><body><p><span style=\" font-weight:600;\">Auth-Key</span></p></body></html>", None))
        self.auth_lineedit.setPlaceholderText(_translate("PSafe", "PS-Auth key=004FFC75-565B-41D2-ABA4-12B76CD331A7; runas=stacia;", None))
        self.Build_tbutton.setText(_translate("PSafe", "Build ", None))
        self.datalabel.setText(_translate("PSafe", "<html><head/><body><p><span style=\" font-weight:600;\">Data</span></p></body></html>", None))
        self.data_linedit.setPlaceholderText(_translate("PSafe", "eg.Name,Bajie, Age,400", None))
        self.get_button.setText(_translate("PSafe", "Get", None))
        self.post_button.setText(_translate("PSafe", "Create", None))
        self.put_button.setText(_translate("PSafe", "Update", None))
        self.del_button.setText(_translate("PSafe", "Delete", None))
        self.filepath_label.setText(_translate("PSafe", "<html><head/><body><p><span style=\" font-weight:600;\">File path</span></p></body></html>", None))
        self.browse_tbutton.setText(_translate("PSafe", "browse", None))
        self.pathlinedit.setPlaceholderText(_translate("PSafe", "eg. C:/Users/btuadmin.BTU/PycharmProjects/tests/", None))
        self.importbutton.setText(_translate("PSafe", "Import", None))

