# -*- coding: utf-8 -*-
"""
/***************************************************************************
MapmashupDialog
                                 A QGIS plugin
 FSC Tomorrow's Biodiversity productivity tools for biological recorders
                             -------------------
        begin                : 2014-02-17
        copyright            : (C) 2014 by Rich Burkmar, Field Studies Council
        email                : richardb@field-studies-council.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from ui_mapmashup import Ui_Mapmashup
import os.path
import glob
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.QtNetwork import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from envmanager import *
from shutil import *
from dropImageLineEdit import *
import tempfile

#from PIL import *

class MapmashupDialog(QtGui.QWidget, Ui_Mapmashup):
    def __init__(self, iface, dockwidget):
        QtGui.QWidget.__init__(self)
        Ui_Mapmashup.__init__(self)
        self.setupUi(self)
        self.canvas = iface.mapCanvas()
        self.iface = iface
    
        self.pathPlugin = "%s%s%%s" % ( os.path.dirname( __file__ ), os.path.sep )
        
        self.butLoadImage.clicked.connect(self.fromClipboard)
        self.butLoadImageFile.clicked.connect(self.loadImageFile)
        self.butLoadImageBrowse.clicked.connect(self.loadImageFileBrowse)
        self.butBrowseImg.clicked.connect(self.BrowseImageFolder)
        self.butBrowseReg.clicked.connect(self.BrowseRegistrationFolder)
        self.leRegistrationFolder.textChanged.connect(self.listRegistrations)
        self.butRefresh.clicked.connect(self.listRegistrations)
        self.butClearLast.clicked.connect(self.removeMap)
        self.butClear.clicked.connect(self.removeMaps)
        self.butTransparentColour.clicked.connect(self.setTransparentColour)
        self.pbBrowseStyleFile.clicked.connect(self.browseStyleFile)
        
        #http://stackoverflow.com/questions/20834064/how-to-create-qpixmap-with-dragimagebits-from-my-browser
        #Replace the leImageFolder line edit with the custom one that handles image drops
        self.hlImageFolder.removeWidget(self.leImageFolder)
        self.hlImageFolder.removeWidget(self.butBrowseImg)
        self.leImageFolder.close()
        self.leImageFolder = DragLineEdit(self)
        self.hlImageFolder.addWidget(self.leImageFolder)
        self.hlImageFolder.addWidget(self.butBrowseImg)
        self.hlImageFolder.update()
        self.leImageFolder.imageDropped.connect(self.mapImageDropped)
      
        # Load the environment stuff
        self.env = envManager()
        
        # Inits
        self.layers = []
        self.tempFiles = []
        self.butLoadImage.setIcon(QIcon( self.pathPlugin % "images/mashup.png" ))
        self.butLoadImageFile.setIcon(QIcon( self.pathPlugin % "images/mashup2.png" ))
        self.butLoadImageBrowse.setIcon(QIcon( self.pathPlugin % "images/mashup3.png" ))
        self.butClearLast.setIcon(QIcon( self.pathPlugin % "images/removelayer.png" ))
        self.butClear.setIcon(QIcon( self.pathPlugin % "images/removelayers.png" ))
        self.butTransparentColour.setStyleSheet("QWidget { background-color: #FFFFFF }")
    
    def showEvent(self, ev):
        # Load the environment stuff
        self.env = envManager()
        self.leImageFolder.setText(self.env.getEnvValue("mapmashup.imgfolder"))
        self.leRegistrationFolder.setText(self.env.getEnvValue("mapmashup.regfolder"))
        return QWidget.showEvent(self, ev)    
        
    def _glob(self, path, *exts):
        """
        Glob for multiple file extensions
    
        Parameters
        ----------
        path : str
            A file name without extension, or directory name
        exts : tuple
            File extensions to glob for
    
        Returns
        -------
        files : list
            list of files matching extensions in exts in path
    
        """
        path = os.path.join(path, "*") if os.path.isdir(path) else path + "*"
        return [f for files in [glob.glob(path + ext) for ext in exts] for f in files]
    
    def browseStyleFile(self):
    
        #Reload env
        self.env.loadEnvironment()
        
        if os.path.exists(self.env.getEnvValue("mapmashup.stylefilefolder")):
            strInitPath = self.env.getEnvValue("mapmashup.stylefilefolder")
        else:
            strInitPath = ""
            
        dlg = QFileDialog
        fileName = dlg.getOpenFileName(self, "Browse for style file", strInitPath, "QML Style Files (*.qml)")
        if fileName:
            self.leStyleFile.setText(fileName)
            self.leStyleFile.setToolTip(fileName)
            
    def setTransparentColour(self):
        startCol = self.butTransparentColour.palette().color(QPalette.Background)
        col = QtGui.QColorDialog.getColor(startCol)
        if col.isValid():
            self.butTransparentColour.setStyleSheet("QWidget { background-color: %s }" % col.name())
        
    def mapImageDropped(self, image):
        #image is a QtGui.QImage object
        self.loadImage(image)
        
    def loadImageFile(self):
        self.loadImage()
        
    def loadImageFileBrowse(self):
    
        #Reload env
        self.env.loadEnvironment()
        
        dirImages = self.leImageFolder.text()
        #Check if image folder exists
        if not os.path.isdir(dirImages):
            dirImages = ""
    
        dlg = QFileDialog
        fileName = dlg.getOpenFileName(self, "Browse for image file", dirImages, "All Files (*.*)")
        if fileName:
            self.loadImage(None, fileName)
        
    def loadImage(self, image=None, imageFile=None):
   
        #Is a registration file selected?
        if self.cboRegistrations.count() == 0:
            self.iface.messageBar().pushMessage("Info", "No registration file selected.", level=QgsMessageBar.INFO)
            return
            
        dirImages = self.leImageFolder.text()
        #Check if image folder exists
        if not os.path.isdir(dirImages):
            self.iface.messageBar().pushMessage("Info", "The specified image folder - '" + dirImages + "' - cannot be found.", level=QgsMessageBar.INFO)
            return
    
        #Create temporary image filename 
        f = tempfile.NamedTemporaryFile(dir=dirImages)
        imageTemp = f.name + ".png"
        f.close()
            
        if not image is None:
            # Copy clipboard image to temp file
            image.save(imageTemp)
        elif not imageFile is None:
            # Copy the passed image to temp file
            copyfile(imageFile, imageTemp)
        else:
            # Get most recent image in image folder and copy to temp file
            imageFiles = self._glob(dirImages, ".gif", ".png", "jpg", ".tif", ".bmp", "jpeg", ".tiff")
            if len(imageFiles) == 0:
                self.iface.messageBar().pushMessage("Info", "No images found in folder '" + dirImages + "'.", level=QgsMessageBar.INFO)
                return
                
            recentImage = max(imageFiles, key=os.path.getmtime)
            if recentImage == "":
                return
            copyfile(recentImage, imageTemp)
        
        # Copy the wld file to image folder and give it the same name as the image
        regFileOut = imageTemp[:-4] + ".wld"
        regFile = os.path.join(self.leRegistrationFolder.text() , self.cboRegistrations.currentText() + ".wld")
        copyfile(regFile, regFileOut)
        
        # Load the raster
        if self.leName.text() != "":
            layerName = self.leName.text() + " " + self.cboRegistrations.currentText()
        else:
            layerName = self.cboRegistrations.currentText()
            
        rlayer = QgsRasterLayer(imageTemp, layerName)
        
        # General transparency
        opacity = (100-self.hsTransparency.value()) * 0.01
        rlayer.renderer().setOpacity(opacity)
        
        # Pixel transparency
        if self.cbTransparentColour.isChecked():
            color = self.butTransparentColour.palette().color(QPalette.Background)
            rlayer.renderer().rasterTransparency().initializeTransparentPixelList(color.red(), color.green(), color.blue())

        # Style file
        styleFile = None
        if self.cbApplyStyle.isChecked():
            if os.path.exists( self.leStyleFile.text()):
                styleFile = self.leStyleFile.text()
                rlayer.loadNamedStyle(self.leStyleFile.text())
         
        # Add to map
        regLayer = QgsMapLayerRegistry.instance().addMapLayer(rlayer)
        
        # Store ID and temp file
        self.layers.append(rlayer.id())
        self.tempFiles.append(imageTemp)

    def BrowseImageFolder(self):
        dlg = QtGui.QFileDialog(self)
        dlg.setFileMode(QtGui.QFileDialog.Directory)
        dlg.setOption(QtGui.QFileDialog.ShowDirsOnly, True)
        if os.path.exists(self.env.getEnvValue("mapmashup.imgfolder")):
            dlg.setDirectory(self.env.getEnvValue("mapmashup.imgfolder"))      
        folderName = dlg.exec_()
        if folderName:
            for folderImage in dlg.selectedFiles():
                self.leImageFolder.setText(folderImage)
                break
            
    def BrowseRegistrationFolder(self):
        dlg = QtGui.QFileDialog(self)
        dlg.setFileMode(QtGui.QFileDialog.Directory)
        dlg.setOption(QtGui.QFileDialog.ShowDirsOnly, True)
        if os.path.exists(self.env.getEnvValue("mapmashup.regfolder")):
            dlg.setDirectory(self.env.getEnvValue("mapmashup.regfolder"))     
            
        folderName = dlg.exec_()
        if folderName:
            for folderImage in dlg.selectedFiles():
                self.leRegistrationFolder.setText(folderImage)
                break
        
    def listRegistrations(self):
        
        dirReg = self.leRegistrationFolder.text() + "/*.wld"
        self.cboRegistrations.clear()
        for fileReg in glob.glob(dirReg):
            self.cboRegistrations.addItem(os.path.basename(fileReg)[:-4])
            
    def removeMap(self):
        if len(self.layers) > 0:
            layerID = self.layers[-1]
            try:
                QgsMapLayerRegistry.instance().removeMapLayer(layerID)
            except:
                pass
            self.layers = self.layers[:-1]
            
            tempPng = self.tempFiles[-1]
            tempWld = tempPng[:-4] + ".wld"
            try:
                os.remove(tempPng)
            except:
                #self.iface.messageBar().pushMessage("Warning", "Can't delete " + tmpPng, level=QgsMessageBar.WARNING)
                pass
            try:
                os.remove(tempWld)
            except:
                pass
            self.tempFiles = self.tempFiles[:-1]
            
    def removeMaps(self):
        for layerID in self.layers:
            try:
                QgsMapLayerRegistry.instance().removeMapLayer(layerID)
            except:
                pass
        self.layers = []
        
        for tempPng in self.tempFiles:
            tempWld = tempPng[:-4] + ".wld"
            try:
                os.remove(tempPng)
            except:
                #self.iface.messageBar().pushMessage("Warning", "Can't delete " + tmpPng, level=QgsMessageBar.WARNING)
                pass
            try:
                os.remove(tempWld)
            except:
                pass
        self.tempFiles = []
    
    def fromClipboard(self):
      
        try:
            img = QApplication.clipboard().image()
        except:
            img = None
            
        if img.isNull():
            self.iface.messageBar().pushMessage("Info", "No image in clipboard", level=QgsMessageBar.INFO)
            return
           
        self.loadImage(img)
        