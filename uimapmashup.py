# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mapmashup.ui'
#
# Created: Sat Jan 14 14:57:36 2017
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_Mapmashup(object):
    def setupUi(self, Mapmashup):
        Mapmashup.setObjectName(_fromUtf8("Mapmashup"))
        Mapmashup.resize(327, 446)
        self.verticalLayout = QtGui.QVBoxLayout(Mapmashup)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hlImageFolder = QtGui.QHBoxLayout()
        self.hlImageFolder.setObjectName(_fromUtf8("hlImageFolder"))
        self.leImageFolder = QtGui.QLineEdit(Mapmashup)
        self.leImageFolder.setObjectName(_fromUtf8("leImageFolder"))
        self.hlImageFolder.addWidget(self.leImageFolder)
        self.butBrowseImg = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butBrowseImg.sizePolicy().hasHeightForWidth())
        self.butBrowseImg.setSizePolicy(sizePolicy)
        self.butBrowseImg.setMinimumSize(QtCore.QSize(100, 0))
        self.butBrowseImg.setMaximumSize(QtCore.QSize(100, 16777215))
        self.butBrowseImg.setObjectName(_fromUtf8("butBrowseImg"))
        self.hlImageFolder.addWidget(self.butBrowseImg)
        self.verticalLayout.addLayout(self.hlImageFolder)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.leRegistrationFolder = QtGui.QLineEdit(Mapmashup)
        self.leRegistrationFolder.setObjectName(_fromUtf8("leRegistrationFolder"))
        self.horizontalLayout_2.addWidget(self.leRegistrationFolder)
        self.butBrowseReg = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butBrowseReg.sizePolicy().hasHeightForWidth())
        self.butBrowseReg.setSizePolicy(sizePolicy)
        self.butBrowseReg.setMinimumSize(QtCore.QSize(100, 0))
        self.butBrowseReg.setMaximumSize(QtCore.QSize(100, 16777215))
        self.butBrowseReg.setObjectName(_fromUtf8("butBrowseReg"))
        self.horizontalLayout_2.addWidget(self.butBrowseReg)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.cboRegistrations = QtGui.QComboBox(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboRegistrations.sizePolicy().hasHeightForWidth())
        self.cboRegistrations.setSizePolicy(sizePolicy)
        self.cboRegistrations.setObjectName(_fromUtf8("cboRegistrations"))
        self.horizontalLayout_5.addWidget(self.cboRegistrations)
        self.butRefresh = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRefresh.sizePolicy().hasHeightForWidth())
        self.butRefresh.setSizePolicy(sizePolicy)
        self.butRefresh.setMinimumSize(QtCore.QSize(100, 0))
        self.butRefresh.setMaximumSize(QtCore.QSize(100, 16777215))
        self.butRefresh.setObjectName(_fromUtf8("butRefresh"))
        self.horizontalLayout_5.addWidget(self.butRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Mapmashup)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.leName = QtGui.QLineEdit(Mapmashup)
        self.leName.setObjectName(_fromUtf8("leName"))
        self.horizontalLayout.addWidget(self.leName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Mapmashup)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.hsTransparency = QtGui.QSlider(Mapmashup)
        self.hsTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.hsTransparency.setTickPosition(QtGui.QSlider.TicksBelow)
        self.hsTransparency.setTickInterval(10)
        self.hsTransparency.setObjectName(_fromUtf8("hsTransparency"))
        self.horizontalLayout_3.addWidget(self.hsTransparency)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.groupBox = QtGui.QGroupBox(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 61))
        self.groupBox.setMaximumSize(QtCore.QSize(3000, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cbTransparentColour = QtGui.QCheckBox(self.groupBox)
        self.cbTransparentColour.setGeometry(QtCore.QRect(10, 15, 211, 17))
        self.cbTransparentColour.setObjectName(_fromUtf8("cbTransparentColour"))
        self.butTransparentColour = QtGui.QPushButton(self.groupBox)
        self.butTransparentColour.setGeometry(QtCore.QRect(45, 35, 36, 23))
        self.butTransparentColour.setText(_fromUtf8(""))
        self.butTransparentColour.setObjectName(_fromUtf8("butTransparentColour"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 35, 56, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.leStyleFile = QtGui.QLineEdit(Mapmashup)
        self.leStyleFile.setObjectName(_fromUtf8("leStyleFile"))
        self.horizontalLayout_6.addWidget(self.leStyleFile)
        self.pbBrowseStyleFile = QtGui.QPushButton(Mapmashup)
        self.pbBrowseStyleFile.setMinimumSize(QtCore.QSize(100, 0))
        self.pbBrowseStyleFile.setObjectName(_fromUtf8("pbBrowseStyleFile"))
        self.horizontalLayout_6.addWidget(self.pbBrowseStyleFile)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.cbApplyStyle = QtGui.QCheckBox(Mapmashup)
        self.cbApplyStyle.setObjectName(_fromUtf8("cbApplyStyle"))
        self.verticalLayout.addWidget(self.cbApplyStyle)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.butLoadImage = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLoadImage.sizePolicy().hasHeightForWidth())
        self.butLoadImage.setSizePolicy(sizePolicy)
        self.butLoadImage.setMinimumSize(QtCore.QSize(30, 30))
        self.butLoadImage.setMaximumSize(QtCore.QSize(30, 30))
        self.butLoadImage.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/mashup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butLoadImage.setIcon(icon)
        self.butLoadImage.setIconSize(QtCore.QSize(26, 26))
        self.butLoadImage.setObjectName(_fromUtf8("butLoadImage"))
        self.horizontalLayout_4.addWidget(self.butLoadImage)
        self.butLoadImageFile = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLoadImageFile.sizePolicy().hasHeightForWidth())
        self.butLoadImageFile.setSizePolicy(sizePolicy)
        self.butLoadImageFile.setMinimumSize(QtCore.QSize(30, 30))
        self.butLoadImageFile.setMaximumSize(QtCore.QSize(30, 30))
        self.butLoadImageFile.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/mashup2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butLoadImageFile.setIcon(icon1)
        self.butLoadImageFile.setIconSize(QtCore.QSize(26, 26))
        self.butLoadImageFile.setObjectName(_fromUtf8("butLoadImageFile"))
        self.horizontalLayout_4.addWidget(self.butLoadImageFile)
        self.butLoadImageBrowse = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butLoadImageBrowse.sizePolicy().hasHeightForWidth())
        self.butLoadImageBrowse.setSizePolicy(sizePolicy)
        self.butLoadImageBrowse.setMinimumSize(QtCore.QSize(30, 30))
        self.butLoadImageBrowse.setMaximumSize(QtCore.QSize(30, 30))
        self.butLoadImageBrowse.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/mashup3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butLoadImageBrowse.setIcon(icon2)
        self.butLoadImageBrowse.setIconSize(QtCore.QSize(26, 26))
        self.butLoadImageBrowse.setObjectName(_fromUtf8("butLoadImageBrowse"))
        self.horizontalLayout_4.addWidget(self.butLoadImageBrowse)
        self.butClearLast = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClearLast.sizePolicy().hasHeightForWidth())
        self.butClearLast.setSizePolicy(sizePolicy)
        self.butClearLast.setMinimumSize(QtCore.QSize(30, 30))
        self.butClearLast.setMaximumSize(QtCore.QSize(30, 30))
        self.butClearLast.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/removelayer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClearLast.setIcon(icon3)
        self.butClearLast.setIconSize(QtCore.QSize(26, 26))
        self.butClearLast.setObjectName(_fromUtf8("butClearLast"))
        self.horizontalLayout_4.addWidget(self.butClearLast)
        self.butClear = QtGui.QPushButton(Mapmashup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClear.sizePolicy().hasHeightForWidth())
        self.butClear.setSizePolicy(sizePolicy)
        self.butClear.setMinimumSize(QtCore.QSize(30, 30))
        self.butClear.setMaximumSize(QtCore.QSize(30, 30))
        self.butClear.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/removelayers.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClear.setIcon(icon4)
        self.butClear.setIconSize(QtCore.QSize(26, 26))
        self.butClear.setObjectName(_fromUtf8("butClear"))
        self.horizontalLayout_4.addWidget(self.butClear)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 150, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Mapmashup)
        QtCore.QMetaObject.connectSlotsByName(Mapmashup)

    def retranslateUi(self, Mapmashup):
        Mapmashup.setWindowTitle(_translate("Mapmashup", "TomBio", None))
        self.leImageFolder.setToolTip(_translate("Mapmashup", "Path of folder for temp image files", None))
        self.butBrowseImg.setToolTip(_translate("Mapmashup", "Browse for image folder", None))
        self.butBrowseImg.setText(_translate("Mapmashup", "Image folder", None))
        self.leRegistrationFolder.setToolTip(_translate("Mapmashup", "Folder where WLD files are kept", None))
        self.butBrowseReg.setToolTip(_translate("Mapmashup", "Browse for folder containing WLD files", None))
        self.butBrowseReg.setText(_translate("Mapmashup", "Registration folder", None))
        self.cboRegistrations.setToolTip(_translate("Mapmashup", "Select WLD registration info", None))
        self.butRefresh.setToolTip(_translate("Mapmashup", "Refresh the list of WLD files", None))
        self.butRefresh.setText(_translate("Mapmashup", "Refresh", None))
        self.label_2.setText(_translate("Mapmashup", "Layer name", None))
        self.leName.setToolTip(_translate("Mapmashup", "Text to be used in layer name", None))
        self.label.setText(_translate("Mapmashup", "Global transparency", None))
        self.hsTransparency.setToolTip(_translate("Mapmashup", "Set the layer\'s global transparency", None))
        self.groupBox.setTitle(_translate("Mapmashup", "Transparent colour", None))
        self.cbTransparentColour.setText(_translate("Mapmashup", "Set transparent background colour", None))
        self.butTransparentColour.setToolTip(_translate("Mapmashup", "Use this button to select transparent colour", None))
        self.label_3.setText(_translate("Mapmashup", "Colour", None))
        self.leStyleFile.setToolTip(_translate("Mapmashup", "Path of style file to apply to created maps", None))
        self.pbBrowseStyleFile.setText(_translate("Mapmashup", "Browse style file", None))
        self.cbApplyStyle.setText(_translate("Mapmashup", "Apply style", None))
        self.butLoadImage.setToolTip(_translate("Mapmashup", "Paste image from clipboard to map with specified registration", None))
        self.butLoadImageFile.setToolTip(_translate("Mapmashup", "Paste most recent  image from image folder to map with specified registration", None))
        self.butLoadImageBrowse.setToolTip(_translate("Mapmashup", "Browse for image to paste into map with specified registration", None))
        self.butClearLast.setToolTip(_translate("Mapmashup", "Remove last mashed map", None))
        self.butClear.setToolTip(_translate("Mapmashup", "Remove all mashed maps", None))

