# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_biorec.ui'
#
# Created: Sat Jan 14 18:31:56 2017
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

class Ui_Biorec(object):
    def setupUi(self, Biorec):
        Biorec.setObjectName(_fromUtf8("Biorec"))
        Biorec.resize(395, 573)
        self.verticalLayout = QtGui.QVBoxLayout(Biorec)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Biorec)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.butBrowse = QtGui.QPushButton(self.tab)
        self.butBrowse.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butBrowse.sizePolicy().hasHeightForWidth())
        self.butBrowse.setSizePolicy(sizePolicy)
        self.butBrowse.setObjectName(_fromUtf8("butBrowse"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.butBrowse)
        self.lblLayer = QtGui.QLabel(self.tab)
        self.lblLayer.setObjectName(_fromUtf8("lblLayer"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblLayer)
        self.mlcbSourceLayer = QgsMapLayerComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mlcbSourceLayer.sizePolicy().hasHeightForWidth())
        self.mlcbSourceLayer.setSizePolicy(sizePolicy)
        self.mlcbSourceLayer.setObjectName(_fromUtf8("mlcbSourceLayer"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.mlcbSourceLayer)
        self.lblGridRefCol = QtGui.QLabel(self.tab)
        self.lblGridRefCol.setObjectName(_fromUtf8("lblGridRefCol"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lblGridRefCol)
        self.fcbGridRefCol = QgsFieldComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcbGridRefCol.sizePolicy().hasHeightForWidth())
        self.fcbGridRefCol.setSizePolicy(sizePolicy)
        self.fcbGridRefCol.setObjectName(_fromUtf8("fcbGridRefCol"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fcbGridRefCol)
        self.lblXCol = QtGui.QLabel(self.tab)
        self.lblXCol.setObjectName(_fromUtf8("lblXCol"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lblXCol)
        self.fcbXCol = QgsFieldComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcbXCol.sizePolicy().hasHeightForWidth())
        self.fcbXCol.setSizePolicy(sizePolicy)
        self.fcbXCol.setObjectName(_fromUtf8("fcbXCol"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.fcbXCol)
        self.lblYCol = QtGui.QLabel(self.tab)
        self.lblYCol.setObjectName(_fromUtf8("lblYCol"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.lblYCol)
        self.fcbYCol = QgsFieldComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fcbYCol.sizePolicy().hasHeightForWidth())
        self.fcbYCol.setSizePolicy(sizePolicy)
        self.fcbYCol.setObjectName(_fromUtf8("fcbYCol"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.fcbYCol)
        self.lblAbundanceColumn = QtGui.QLabel(self.tab)
        self.lblAbundanceColumn.setObjectName(_fromUtf8("lblAbundanceColumn"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.lblAbundanceColumn)
        self.cboAbundanceCol = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboAbundanceCol.sizePolicy().hasHeightForWidth())
        self.cboAbundanceCol.setSizePolicy(sizePolicy)
        self.cboAbundanceCol.setObjectName(_fromUtf8("cboAbundanceCol"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.cboAbundanceCol)
        self.lblTaxonCol = QtGui.QLabel(self.tab)
        self.lblTaxonCol.setObjectName(_fromUtf8("lblTaxonCol"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.lblTaxonCol)
        self.cboTaxonCol = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboTaxonCol.sizePolicy().hasHeightForWidth())
        self.cboTaxonCol.setSizePolicy(sizePolicy)
        self.cboTaxonCol.setObjectName(_fromUtf8("cboTaxonCol"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.cboTaxonCol)
        self.cbIsScientific = QtGui.QCheckBox(self.tab)
        self.cbIsScientific.setEnabled(False)
        self.cbIsScientific.setChecked(False)
        self.cbIsScientific.setObjectName(_fromUtf8("cbIsScientific"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.cbIsScientific)
        self.lblGroupingCol = QtGui.QLabel(self.tab)
        self.lblGroupingCol.setEnabled(False)
        self.lblGroupingCol.setObjectName(_fromUtf8("lblGroupingCol"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.lblGroupingCol)
        self.cboGroupingCol = QtGui.QComboBox(self.tab)
        self.cboGroupingCol.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboGroupingCol.sizePolicy().hasHeightForWidth())
        self.cboGroupingCol.setSizePolicy(sizePolicy)
        self.cboGroupingCol.setObjectName(_fromUtf8("cboGroupingCol"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.cboGroupingCol)
        self.lblInputCRS = QtGui.QLabel(self.tab)
        self.lblInputCRS.setObjectName(_fromUtf8("lblInputCRS"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.lblInputCRS)
        self.pswInputCRS = QgsProjectionSelectionWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pswInputCRS.sizePolicy().hasHeightForWidth())
        self.pswInputCRS.setSizePolicy(sizePolicy)
        self.pswInputCRS.setObjectName(_fromUtf8("pswInputCRS"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.pswInputCRS)
        self.lblOutputCRS = QtGui.QLabel(self.tab)
        self.lblOutputCRS.setObjectName(_fromUtf8("lblOutputCRS"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.lblOutputCRS)
        self.pswOutputCRS = QgsProjectionSelectionWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pswOutputCRS.sizePolicy().hasHeightForWidth())
        self.pswOutputCRS.setSizePolicy(sizePolicy)
        self.pswOutputCRS.setObjectName(_fromUtf8("pswOutputCRS"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.pswOutputCRS)
        self.cbMatchCRS = QtGui.QCheckBox(self.tab)
        self.cbMatchCRS.setEnabled(True)
        self.cbMatchCRS.setChecked(False)
        self.cbMatchCRS.setObjectName(_fromUtf8("cbMatchCRS"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.cbMatchCRS)
        spacerItem = QtGui.QSpacerItem(20, 84, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(12, QtGui.QFormLayout.LabelRole, spacerItem)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tvTaxa = QtGui.QTreeView(self.tab_3)
        self.tvTaxa.setToolTip(_fromUtf8(""))
        self.tvTaxa.setObjectName(_fromUtf8("tvTaxa"))
        self.tvTaxa.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.tvTaxa)
        self.frame_2 = QtGui.QFrame(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.butContract = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butContract.sizePolicy().hasHeightForWidth())
        self.butContract.setSizePolicy(sizePolicy)
        self.butContract.setMinimumSize(QtCore.QSize(25, 0))
        self.butContract.setMaximumSize(QtCore.QSize(25, 16777215))
        self.butContract.setObjectName(_fromUtf8("butContract"))
        self.horizontalLayout.addWidget(self.butContract)
        self.butExpand = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butExpand.sizePolicy().hasHeightForWidth())
        self.butExpand.setSizePolicy(sizePolicy)
        self.butExpand.setMinimumSize(QtCore.QSize(25, 0))
        self.butExpand.setMaximumSize(QtCore.QSize(25, 16777215))
        self.butExpand.setObjectName(_fromUtf8("butExpand"))
        self.horizontalLayout.addWidget(self.butExpand)
        self.butCheckAll = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butCheckAll.sizePolicy().hasHeightForWidth())
        self.butCheckAll.setSizePolicy(sizePolicy)
        self.butCheckAll.setMinimumSize(QtCore.QSize(55, 0))
        self.butCheckAll.setMaximumSize(QtCore.QSize(55, 16777215))
        self.butCheckAll.setObjectName(_fromUtf8("butCheckAll"))
        self.horizontalLayout.addWidget(self.butCheckAll)
        self.butUncheckAll = QtGui.QPushButton(self.frame_2)
        self.butUncheckAll.setMinimumSize(QtCore.QSize(65, 0))
        self.butUncheckAll.setMaximumSize(QtCore.QSize(65, 16777215))
        self.butUncheckAll.setObjectName(_fromUtf8("butUncheckAll"))
        self.horizontalLayout.addWidget(self.butUncheckAll)
        spacerItem1 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.butGenTree = QtGui.QPushButton(self.frame_2)
        self.butGenTree.setObjectName(_fromUtf8("butGenTree"))
        self.horizontalLayout.addWidget(self.butGenTree)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.cboBatchMode = QtGui.QComboBox(self.tab_5)
        self.cboBatchMode.setMinimumSize(QtCore.QSize(130, 0))
        self.cboBatchMode.setMaximumSize(QtCore.QSize(130, 16777215))
        self.cboBatchMode.setObjectName(_fromUtf8("cboBatchMode"))
        self.cboBatchMode.addItem(_fromUtf8(""))
        self.cboBatchMode.addItem(_fromUtf8(""))
        self.verticalLayout_5.addWidget(self.cboBatchMode)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.leStyleFile = QtGui.QLineEdit(self.tab_5)
        self.leStyleFile.setObjectName(_fromUtf8("leStyleFile"))
        self.horizontalLayout_4.addWidget(self.leStyleFile)
        self.pbBrowseStyleFile = QtGui.QPushButton(self.tab_5)
        self.pbBrowseStyleFile.setMinimumSize(QtCore.QSize(105, 0))
        self.pbBrowseStyleFile.setObjectName(_fromUtf8("pbBrowseStyleFile"))
        self.horizontalLayout_4.addWidget(self.pbBrowseStyleFile)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.cbApplyStyle = QtGui.QCheckBox(self.tab_5)
        self.cbApplyStyle.setObjectName(_fromUtf8("cbApplyStyle"))
        self.verticalLayout_5.addWidget(self.cbApplyStyle)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_2 = QtGui.QLabel(self.tab_5)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_8.addWidget(self.label_2)
        self.hsLayerTransparency = QtGui.QSlider(self.tab_5)
        self.hsLayerTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.hsLayerTransparency.setTickPosition(QtGui.QSlider.TicksBelow)
        self.hsLayerTransparency.setTickInterval(10)
        self.hsLayerTransparency.setObjectName(_fromUtf8("hsLayerTransparency"))
        self.horizontalLayout_8.addWidget(self.hsLayerTransparency)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.mGroupBox = QgsCollapsibleGroupBox(self.tab_5)
        self.mGroupBox.setObjectName(_fromUtf8("mGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.mGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label = QtGui.QLabel(self.mGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(34, 0))
        self.label.setMaximumSize(QtCore.QSize(34, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        self.cboOutputFormat = QtGui.QComboBox(self.mGroupBox)
        self.cboOutputFormat.setEditable(False)
        self.cboOutputFormat.setObjectName(_fromUtf8("cboOutputFormat"))
        self.cboOutputFormat.addItem(_fromUtf8(""))
        self.cboOutputFormat.addItem(_fromUtf8(""))
        self.cboOutputFormat.addItem(_fromUtf8(""))
        self.cboOutputFormat.addItem(_fromUtf8(""))
        self.cboOutputFormat.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.cboOutputFormat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.qgsOutputCRS = QgsProjectionSelectionWidget(self.mGroupBox)
        self.qgsOutputCRS.setObjectName(_fromUtf8("qgsOutputCRS"))
        self.verticalLayout_2.addWidget(self.qgsOutputCRS)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.leImageFolder = QtGui.QLineEdit(self.mGroupBox)
        self.leImageFolder.setObjectName(_fromUtf8("leImageFolder"))
        self.horizontalLayout_3.addWidget(self.leImageFolder)
        self.pbBrowseImageFolder = QtGui.QPushButton(self.mGroupBox)
        self.pbBrowseImageFolder.setObjectName(_fromUtf8("pbBrowseImageFolder"))
        self.horizontalLayout_3.addWidget(self.pbBrowseImageFolder)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.cbTaxonMetaData = QtGui.QCheckBox(self.mGroupBox)
        self.cbTaxonMetaData.setMinimumSize(QtCore.QSize(131, 0))
        self.cbTaxonMetaData.setMaximumSize(QtCore.QSize(131, 16777215))
        self.cbTaxonMetaData.setObjectName(_fromUtf8("cbTaxonMetaData"))
        self.horizontalLayout_10.addWidget(self.cbTaxonMetaData)
        self.mlcbTaxonMetaDataLayer = QgsMapLayerComboBox(self.mGroupBox)
        self.mlcbTaxonMetaDataLayer.setObjectName(_fromUtf8("mlcbTaxonMetaDataLayer"))
        self.horizontalLayout_10.addWidget(self.mlcbTaxonMetaDataLayer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_5.addWidget(self.mGroupBox)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.butHelp = QtGui.QPushButton(self.tab_5)
        self.butHelp.setMinimumSize(QtCore.QSize(32, 32))
        self.butHelp.setMaximumSize(QtCore.QSize(32, 32))
        self.butHelp.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/bang.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butHelp.setIcon(icon)
        self.butHelp.setIconSize(QtCore.QSize(26, 26))
        self.butHelp.setObjectName(_fromUtf8("butHelp"))
        self.horizontalLayout_7.addWidget(self.butHelp)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        spacerItem3 = QtGui.QSpacerItem(20, 52, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pteLog = QtGui.QPlainTextEdit(self.tab_4)
        self.pteLog.setObjectName(_fromUtf8("pteLog"))
        self.verticalLayout_4.addWidget(self.pteLog)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.progBatch = QtGui.QProgressBar(Biorec)
        self.progBatch.setProperty("value", 0)
        self.progBatch.setObjectName(_fromUtf8("progBatch"))
        self.horizontalLayout_6.addWidget(self.progBatch)
        self.pbCancel = QtGui.QPushButton(Biorec)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_6.addWidget(self.pbCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.cboSymbol = QtGui.QComboBox(Biorec)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboSymbol.sizePolicy().hasHeightForWidth())
        self.cboSymbol.setSizePolicy(sizePolicy)
        self.cboSymbol.setMinimumSize(QtCore.QSize(90, 0))
        self.cboSymbol.setMaximumSize(QtCore.QSize(90, 16777215))
        self.cboSymbol.setObjectName(_fromUtf8("cboSymbol"))
        self.cboSymbol.addItem(_fromUtf8(""))
        self.cboSymbol.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cboSymbol)
        self.cboMapType = QtGui.QComboBox(Biorec)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboMapType.sizePolicy().hasHeightForWidth())
        self.cboMapType.setSizePolicy(sizePolicy)
        self.cboMapType.setObjectName(_fromUtf8("cboMapType"))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.cboMapType.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cboMapType)
        self.dsbGridSize = QtGui.QDoubleSpinBox(Biorec)
        self.dsbGridSize.setDecimals(3)
        self.dsbGridSize.setMaximum(100000000.0)
        self.dsbGridSize.setSingleStep(100.0)
        self.dsbGridSize.setObjectName(_fromUtf8("dsbGridSize"))
        self.horizontalLayout_5.addWidget(self.dsbGridSize)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.butMap = QtGui.QPushButton(Biorec)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butMap.sizePolicy().hasHeightForWidth())
        self.butMap.setSizePolicy(sizePolicy)
        self.butMap.setMinimumSize(QtCore.QSize(32, 32))
        self.butMap.setMaximumSize(QtCore.QSize(32, 32))
        self.butMap.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/maptaxa.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butMap.setIcon(icon1)
        self.butMap.setIconSize(QtCore.QSize(30, 30))
        self.butMap.setObjectName(_fromUtf8("butMap"))
        self.horizontalLayout_2.addWidget(self.butMap)
        self.butSaveImage = QtGui.QPushButton(Biorec)
        self.butSaveImage.setMinimumSize(QtCore.QSize(32, 32))
        self.butSaveImage.setMaximumSize(QtCore.QSize(32, 32))
        self.butSaveImage.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/saveimage.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butSaveImage.setIcon(icon2)
        self.butSaveImage.setIconSize(QtCore.QSize(28, 28))
        self.butSaveImage.setObjectName(_fromUtf8("butSaveImage"))
        self.horizontalLayout_2.addWidget(self.butSaveImage)
        self.butShowAll = QtGui.QPushButton(Biorec)
        self.butShowAll.setMinimumSize(QtCore.QSize(32, 32))
        self.butShowAll.setMaximumSize(QtCore.QSize(32, 32))
        self.butShowAll.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/layershow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butShowAll.setIcon(icon3)
        self.butShowAll.setIconSize(QtCore.QSize(26, 26))
        self.butShowAll.setObjectName(_fromUtf8("butShowAll"))
        self.horizontalLayout_2.addWidget(self.butShowAll)
        self.butHideAll = QtGui.QPushButton(Biorec)
        self.butHideAll.setMinimumSize(QtCore.QSize(32, 32))
        self.butHideAll.setMaximumSize(QtCore.QSize(32, 32))
        self.butHideAll.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/layerhide.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butHideAll.setIcon(icon4)
        self.butHideAll.setIconSize(QtCore.QSize(26, 26))
        self.butHideAll.setObjectName(_fromUtf8("butHideAll"))
        self.horizontalLayout_2.addWidget(self.butHideAll)
        self.butRemoveMap = QtGui.QPushButton(Biorec)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRemoveMap.sizePolicy().hasHeightForWidth())
        self.butRemoveMap.setSizePolicy(sizePolicy)
        self.butRemoveMap.setMinimumSize(QtCore.QSize(32, 32))
        self.butRemoveMap.setMaximumSize(QtCore.QSize(32, 32))
        self.butRemoveMap.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/removelayer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butRemoveMap.setIcon(icon5)
        self.butRemoveMap.setIconSize(QtCore.QSize(30, 30))
        self.butRemoveMap.setObjectName(_fromUtf8("butRemoveMap"))
        self.horizontalLayout_2.addWidget(self.butRemoveMap)
        self.butRemoveMaps = QtGui.QPushButton(Biorec)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butRemoveMaps.sizePolicy().hasHeightForWidth())
        self.butRemoveMaps.setSizePolicy(sizePolicy)
        self.butRemoveMaps.setMinimumSize(QtCore.QSize(32, 32))
        self.butRemoveMaps.setMaximumSize(QtCore.QSize(32, 32))
        self.butRemoveMaps.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("images/removelayers.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butRemoveMaps.setIcon(icon6)
        self.butRemoveMaps.setIconSize(QtCore.QSize(30, 30))
        self.butRemoveMaps.setObjectName(_fromUtf8("butRemoveMaps"))
        self.horizontalLayout_2.addWidget(self.butRemoveMaps)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Biorec)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Biorec)

    def retranslateUi(self, Biorec):
        Biorec.setWindowTitle(_translate("Biorec", "TomBio", None))
        self.butBrowse.setToolTip(_translate("Biorec", "Browse for CSV file", None))
        self.butBrowse.setText(_translate("Biorec", "Create new source layer from CSV", None))
        self.lblLayer.setText(_translate("Biorec", "Source layer", None))
        self.lblGridRefCol.setText(_translate("Biorec", "OS Grid Ref Column", None))
        self.lblXCol.setText(_translate("Biorec", "X Column", None))
        self.lblYCol.setText(_translate("Biorec", "Y Column", None))
        self.lblAbundanceColumn.setText(_translate("Biorec", "Abundance Column", None))
        self.cboAbundanceCol.setToolTip(_translate("Biorec", "Optional column with abundance data", None))
        self.lblTaxonCol.setText(_translate("Biorec", "Taxon Column", None))
        self.cboTaxonCol.setToolTip(_translate("Biorec", "Select column with species names", None))
        self.cbIsScientific.setToolTip(_translate("Biorec", "Select if taxon column contains scientific binomials", None))
        self.cbIsScientific.setText(_translate("Biorec", "Scientific names", None))
        self.lblGroupingCol.setText(_translate("Biorec", "Grouping Column", None))
        self.cboGroupingCol.setToolTip(_translate("Biorec", "Optionally select a grouping column", None))
        self.lblInputCRS.setText(_translate("Biorec", "Input CRS", None))
        self.lblOutputCRS.setText(_translate("Biorec", "Output CRS", None))
        self.cbMatchCRS.setToolTip(_translate("Biorec", "Select if taxon column contains scientific binomials", None))
        self.cbMatchCRS.setText(_translate("Biorec", "Match to input CRS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Biorec", "Data specification", None))
        self.butContract.setToolTip(_translate("Biorec", "Contract all items", None))
        self.butContract.setText(_translate("Biorec", "-", None))
        self.butExpand.setToolTip(_translate("Biorec", "Expand all items", None))
        self.butExpand.setText(_translate("Biorec", "+", None))
        self.butCheckAll.setToolTip(_translate("Biorec", "Check all items", None))
        self.butCheckAll.setText(_translate("Biorec", "Check all", None))
        self.butUncheckAll.setToolTip(_translate("Biorec", "Uncheck all items", None))
        self.butUncheckAll.setText(_translate("Biorec", "Uncheck all", None))
        self.butGenTree.setToolTip(_translate("Biorec", "Create/recreate species tree", None))
        self.butGenTree.setText(_translate("Biorec", "Load taxa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Biorec", "Taxa", None))
        self.cboBatchMode.setToolTip(_translate("Biorec", "Single or batch mode?", None))
        self.cboBatchMode.setItemText(0, _translate("Biorec", "Single map mode", None))
        self.cboBatchMode.setItemText(1, _translate("Biorec", "Batch map mode", None))
        self.leStyleFile.setToolTip(_translate("Biorec", "Path of style file to apply to created maps", None))
        self.pbBrowseStyleFile.setText(_translate("Biorec", "Browse style file", None))
        self.cbApplyStyle.setText(_translate("Biorec", "Apply style", None))
        self.label_2.setText(_translate("Biorec", "Transparency", None))
        self.mGroupBox.setTitle(_translate("Biorec", "Output options", None))
        self.label.setText(_translate("Biorec", "Format", None))
        self.cboOutputFormat.setItemText(0, _translate("Biorec", "Image", None))
        self.cboOutputFormat.setItemText(1, _translate("Biorec", "Shapefile", None))
        self.cboOutputFormat.setItemText(2, _translate("Biorec", "GeoJSON", None))
        self.cboOutputFormat.setItemText(3, _translate("Biorec", "Composer image", None))
        self.cboOutputFormat.setItemText(4, _translate("Biorec", "Composer PDF", None))
        self.leImageFolder.setToolTip(_translate("Biorec", "Folder for atlas images", None))
        self.pbBrowseImageFolder.setText(_translate("Biorec", "Browse output folder", None))
        self.cbTaxonMetaData.setText(_translate("Biorec", "Taxon Metadata Layer", None))
        self.butHelp.setToolTip(_translate("Biorec", "Tips and help", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Biorec", "Options", None))
        self.pteLog.setToolTip(_translate("Biorec", "Information messages generated during map layer creation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Biorec", "Log", None))
        self.progBatch.setToolTip(_translate("Biorec", "Shows progress in batch mode", None))
        self.pbCancel.setToolTip(_translate("Biorec", "Cancel batch process", None))
        self.pbCancel.setText(_translate("Biorec", "Cancel", None))
        self.cboSymbol.setToolTip(_translate("Biorec", "Squares or circles?", None))
        self.cboSymbol.setItemText(0, _translate("Biorec", "Atlas squares", None))
        self.cboSymbol.setItemText(1, _translate("Biorec", "Atlas circles", None))
        self.cboMapType.setToolTip(_translate("Biorec", "Type of map", None))
        self.cboMapType.setItemText(0, _translate("Biorec", "Records as points", None))
        self.cboMapType.setItemText(1, _translate("Biorec", "Records as grid squares", None))
        self.cboMapType.setItemText(2, _translate("Biorec", "10 m atlas (8 fig gr)", None))
        self.cboMapType.setItemText(3, _translate("Biorec", "100 m atlas (6 fig gr)", None))
        self.cboMapType.setItemText(4, _translate("Biorec", "1 km atlas (monads)", None))
        self.cboMapType.setItemText(5, _translate("Biorec", "2 km atlas (tetrads)", None))
        self.cboMapType.setItemText(6, _translate("Biorec", "5 km atlas (quadrants)", None))
        self.cboMapType.setItemText(7, _translate("Biorec", "10 km atlas (hectads)", None))
        self.cboMapType.setItemText(8, _translate("Biorec", "User-defined atlas size:", None))
        self.dsbGridSize.setToolTip(_translate("Biorec", "<html><head/><body><p>Grid size for atlas - specify in units used by output CRS</p></body></html>", None))
        self.butMap.setToolTip(_translate("Biorec", "Create map layer", None))
        self.butSaveImage.setToolTip(_translate("Biorec", "Save temporary map layers as images or permanent layers", None))
        self.butShowAll.setToolTip(_translate("Biorec", "Show all generated map layers", None))
        self.butHideAll.setToolTip(_translate("Biorec", "Hide all generated map layers", None))
        self.butRemoveMap.setToolTip(_translate("Biorec", "Remove last map layer", None))
        self.butRemoveMaps.setToolTip(_translate("Biorec", "Remove all map layers", None))

from qgis.gui import QgsFieldComboBox, QgsProjectionSelectionWidget, QgsCollapsibleGroupBox, QgsMapLayerComboBox
