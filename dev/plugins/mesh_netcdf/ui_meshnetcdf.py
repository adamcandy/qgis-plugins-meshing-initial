# -*- coding: utf-8 -*-

##########################################################################
#  
#  QGIS-meshing plugins.
#  
#  Copyright (C) 2012-2013 Imperial College London and others.
#  
#  Please see the AUTHORS file in the main source directory for a
#  full list of copyright holders.
#  
#  Dr Adam S. Candy, adam.candy@imperial.ac.uk
#  Applied Modelling and Computation Group
#  Department of Earth Science and Engineering
#  Imperial College London
#  
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation,
#  version 2.1 of the License.
#  
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#  
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307
#  USA
#  
##########################################################################

# Form implementation generated from reading ui file 'ui_meshnetcdf.ui'
#
# Created: Mon Dec 10 16:39:54 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MeshNetCDF(object):
    def setupUi(self, MeshNetCDF):
        MeshNetCDF.setObjectName(_fromUtf8("MeshNetCDF"))
        MeshNetCDF.resize(550, 787)
        self.buttonBox = QtGui.QDialogButtonBox(MeshNetCDF)
        self.buttonBox.setGeometry(QtCore.QRect(350, 750, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.frame = QtGui.QFrame(MeshNetCDF)
        self.frame.setGeometry(QtCore.QRect(10, 330, 531, 201))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.grpNCDF = QtGui.QGroupBox(self.frame)
        self.grpNCDF.setEnabled(True)
        self.grpNCDF.setGeometry(QtCore.QRect(10, 10, 521, 191))
        self.grpNCDF.setToolTip(_fromUtf8(""))
        self.grpNCDF.setWhatsThis(_fromUtf8(""))
        self.grpNCDF.setAutoFillBackground(False)
        self.grpNCDF.setFlat(False)
        self.grpNCDF.setCheckable(True)
        self.grpNCDF.setChecked(True)
        self.grpNCDF.setObjectName(_fromUtf8("grpNCDF"))
        self.singleNetCDFGroupBox = QtGui.QGroupBox(self.grpNCDF)
        self.singleNetCDFGroupBox.setEnabled(True)
        self.singleNetCDFGroupBox.setGeometry(QtCore.QRect(30, 50, 481, 81))
        self.singleNetCDFGroupBox.setTitle(_fromUtf8(""))
        self.singleNetCDFGroupBox.setObjectName(_fromUtf8("singleNetCDFGroupBox"))
        self.singleNetCDFChooseFilesPushButton = QtGui.QPushButton(self.singleNetCDFGroupBox)
        self.singleNetCDFChooseFilesPushButton.setEnabled(False)
        self.singleNetCDFChooseFilesPushButton.setGeometry(QtCore.QRect(390, 40, 85, 27))
        self.singleNetCDFChooseFilesPushButton.setObjectName(_fromUtf8("singleNetCDFChooseFilesPushButton"))
        self.singleNetCDFChooseFilesLineEdit = QtGui.QLineEdit(self.singleNetCDFGroupBox)
        self.singleNetCDFChooseFilesLineEdit.setEnabled(False)
        self.singleNetCDFChooseFilesLineEdit.setGeometry(QtCore.QRect(180, 40, 201, 27))
        self.singleNetCDFChooseFilesLineEdit.setObjectName(_fromUtf8("singleNetCDFChooseFilesLineEdit"))
        self.singleNetCDFLayersRadioButton = QtGui.QRadioButton(self.singleNetCDFGroupBox)
        self.singleNetCDFLayersRadioButton.setGeometry(QtCore.QRect(0, 10, 160, 22))
        self.singleNetCDFLayersRadioButton.setObjectName(_fromUtf8("singleNetCDFLayersRadioButton"))
        self.singleNetCDFLayerDropDown = QtGui.QComboBox(self.singleNetCDFGroupBox)
        self.singleNetCDFLayerDropDown.setEnabled(False)
        self.singleNetCDFLayerDropDown.setGeometry(QtCore.QRect(180, 10, 201, 27))
        self.singleNetCDFLayerDropDown.setObjectName(_fromUtf8("singleNetCDFLayerDropDown"))
        self.singleNetCDFChooseFilesRadioButton = QtGui.QRadioButton(self.singleNetCDFGroupBox)
        self.singleNetCDFChooseFilesRadioButton.setGeometry(QtCore.QRect(0, 40, 114, 22))
        self.singleNetCDFChooseFilesRadioButton.setObjectName(_fromUtf8("singleNetCDFChooseFilesRadioButton"))
        self.singleNetCDFRadioButton = QtGui.QRadioButton(self.grpNCDF)
        self.singleNetCDFRadioButton.setGeometry(QtCore.QRect(10, 30, 183, 22))
        self.singleNetCDFRadioButton.setChecked(True)
        self.singleNetCDFRadioButton.setObjectName(_fromUtf8("singleNetCDFRadioButton"))
        self.addLayerToCanvasCheckBox = QtGui.QCheckBox(self.grpNCDF)
        self.addLayerToCanvasCheckBox.setEnabled(False)
        self.addLayerToCanvasCheckBox.setGeometry(QtCore.QRect(30, 160, 126, 22))
        self.addLayerToCanvasCheckBox.setObjectName(_fromUtf8("addLayerToCanvasCheckBox"))
        self.multipleNetCDFFilesRadioButton = QtGui.QRadioButton(self.grpNCDF)
        self.multipleNetCDFFilesRadioButton.setGeometry(QtCore.QRect(11, 130, 370, 22))
        self.multipleNetCDFFilesRadioButton.setChecked(False)
        self.multipleNetCDFFilesRadioButton.setObjectName(_fromUtf8("multipleNetCDFFilesRadioButton"))
        self.frame_2 = QtGui.QFrame(MeshNetCDF)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 531, 311))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.grpDom = QtGui.QGroupBox(self.frame_2)
        self.grpDom.setGeometry(QtCore.QRect(10, 10, 521, 271))
        self.grpDom.setFlat(False)
        self.grpDom.setObjectName(_fromUtf8("grpDom"))
        self.domainShapefileLayerDropDown = QtGui.QComboBox(self.grpDom)
        self.domainShapefileLayerDropDown.setGeometry(QtCore.QRect(210, 30, 201, 27))
        self.domainShapefileLayerDropDown.setObjectName(_fromUtf8("domainShapefileLayerDropDown"))
        self.domainShapefileLayerRadioButton = QtGui.QRadioButton(self.grpDom)
        self.domainShapefileLayerRadioButton.setGeometry(QtCore.QRect(10, 30, 190, 22))
        self.domainShapefileLayerRadioButton.setChecked(True)
        self.domainShapefileLayerRadioButton.setObjectName(_fromUtf8("domainShapefileLayerRadioButton"))
        self.grpDefID = QtGui.QGroupBox(self.grpDom)
        self.grpDefID.setEnabled(True)
        self.grpDefID.setGeometry(QtCore.QRect(30, 90, 391, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.grpDefID.setFont(font)
        self.grpDefID.setAcceptDrops(False)
        self.grpDefID.setCheckable(True)
        self.grpDefID.setChecked(False)
        self.grpDefID.setObjectName(_fromUtf8("grpDefID"))
        self.label_2 = QtGui.QLabel(self.grpDefID)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.IdDropdown = QtGui.QComboBox(self.grpDefID)
        self.IdDropdown.setGeometry(QtCore.QRect(180, 30, 201, 27))
        self.IdDropdown.setObjectName(_fromUtf8("IdDropdown"))
        self.label_3 = QtGui.QLabel(self.grpDefID)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 71, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Default_Id = QtGui.QLineEdit(self.grpDefID)
        self.Default_Id.setGeometry(QtCore.QRect(180, 60, 201, 27))
        self.Default_Id.setObjectName(_fromUtf8("Default_Id"))
        self.Threshold = QtGui.QLineEdit(self.grpDom)
        self.Threshold.setEnabled(True)
        self.Threshold.setGeometry(QtCore.QRect(210, 60, 201, 27))
        self.Threshold.setObjectName(_fromUtf8("Threshold"))
        self.define_th = QtGui.QCheckBox(self.grpDom)
        self.define_th.setEnabled(True)
        self.define_th.setGeometry(QtCore.QRect(30, 60, 141, 22))
        self.define_th.setObjectName(_fromUtf8("define_th"))
        self.lineGroupBox = QtGui.QGroupBox(self.grpDom)
        self.lineGroupBox.setGeometry(QtCore.QRect(20, 210, 391, 31))
        self.lineGroupBox.setTitle(_fromUtf8(""))
        self.lineGroupBox.setObjectName(_fromUtf8("lineGroupBox"))
        self.lineRadioButton = QtGui.QRadioButton(self.lineGroupBox)
        self.lineRadioButton.setGeometry(QtCore.QRect(190, 10, 71, 22))
        self.lineRadioButton.setChecked(True)
        self.lineRadioButton.setObjectName(_fromUtf8("lineRadioButton"))
        self.bSplineRadioButton = QtGui.QRadioButton(self.lineGroupBox)
        self.bSplineRadioButton.setGeometry(QtCore.QRect(280, 10, 91, 22))
        self.bSplineRadioButton.setObjectName(_fromUtf8("bSplineRadioButton"))
        self.label_5 = QtGui.QLabel(self.lineGroupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 67, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.compoundCheckBox = QtGui.QCheckBox(self.grpDom)
        self.compoundCheckBox.setGeometry(QtCore.QRect(30, 190, 171, 22))
        self.compoundCheckBox.setChecked(True)
        self.compoundCheckBox.setObjectName(_fromUtf8("compoundCheckBox"))
        self.grpChooseGeo = QtGui.QGroupBox(self.frame_2)
        self.grpChooseGeo.setEnabled(True)
        self.grpChooseGeo.setGeometry(QtCore.QRect(10, 270, 501, 41))
        self.grpChooseGeo.setTitle(_fromUtf8(""))
        self.grpChooseGeo.setObjectName(_fromUtf8("grpChooseGeo"))
        self.chooseGeoFileRadioButton = QtGui.QRadioButton(self.grpChooseGeo)
        self.chooseGeoFileRadioButton.setGeometry(QtCore.QRect(10, 0, 177, 22))
        self.chooseGeoFileRadioButton.setChecked(False)
        self.chooseGeoFileRadioButton.setObjectName(_fromUtf8("chooseGeoFileRadioButton"))
        self.chooseGeoFileLineEdit = QtGui.QLineEdit(self.grpChooseGeo)
        self.chooseGeoFileLineEdit.setEnabled(True)
        self.chooseGeoFileLineEdit.setGeometry(QtCore.QRect(200, 0, 201, 27))
        self.chooseGeoFileLineEdit.setObjectName(_fromUtf8("chooseGeoFileLineEdit"))
        self.chooseGeoFilePushButton = QtGui.QPushButton(self.grpChooseGeo)
        self.chooseGeoFilePushButton.setEnabled(True)
        self.chooseGeoFilePushButton.setGeometry(QtCore.QRect(410, 0, 85, 27))
        self.chooseGeoFilePushButton.setObjectName(_fromUtf8("chooseGeoFilePushButton"))
        self.frame_5 = QtGui.QFrame(MeshNetCDF)
        self.frame_5.setGeometry(QtCore.QRect(10, 540, 531, 201))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.grpCSpace_2 = QtGui.QGroupBox(self.frame_5)
        self.grpCSpace_2.setGeometry(QtCore.QRect(10, 10, 511, 181))
        self.grpCSpace_2.setCheckable(True)
        self.grpCSpace_2.setObjectName(_fromUtf8("grpCSpace_2"))
        self.sphereRadioButton = QtGui.QRadioButton(self.grpCSpace_2)
        self.sphereRadioButton.setGeometry(QtCore.QRect(250, 30, 131, 22))
        self.sphereRadioButton.setObjectName(_fromUtf8("sphereRadioButton"))
        self.meshingAlgorithmDropDown = QtGui.QComboBox(self.grpCSpace_2)
        self.meshingAlgorithmDropDown.setGeometry(QtCore.QRect(210, 60, 201, 27))
        self.meshingAlgorithmDropDown.setObjectName(_fromUtf8("meshingAlgorithmDropDown"))
        self.flatRadioButton = QtGui.QRadioButton(self.grpCSpace_2)
        self.flatRadioButton.setGeometry(QtCore.QRect(170, 30, 74, 22))
        self.flatRadioButton.setAcceptDrops(False)
        self.flatRadioButton.setChecked(True)
        self.flatRadioButton.setObjectName(_fromUtf8("flatRadioButton"))
        self.label = QtGui.QLabel(self.grpCSpace_2)
        self.label.setGeometry(QtCore.QRect(40, 30, 120, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.grpCSpace_2)
        self.label_4.setGeometry(QtCore.QRect(40, 60, 69, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.commandLineGroupBox = QtGui.QGroupBox(self.grpCSpace_2)
        self.commandLineGroupBox.setGeometry(QtCore.QRect(30, 80, 441, 101))
        self.commandLineGroupBox.setTitle(_fromUtf8(""))
        self.commandLineGroupBox.setCheckable(False)
        self.commandLineGroupBox.setObjectName(_fromUtf8("commandLineGroupBox"))
        self.commandEdit = QtGui.QToolButton(self.commandLineGroupBox)
        self.commandEdit.setGeometry(QtCore.QRect(390, 20, 24, 25))
        self.commandEdit.setCheckable(True)
        self.commandEdit.setObjectName(_fromUtf8("commandEdit"))
        self.commandTextEdit = QtGui.QTextEdit(self.commandLineGroupBox)
        self.commandTextEdit.setGeometry(QtCore.QRect(10, 20, 371, 78))
        self.commandTextEdit.setObjectName(_fromUtf8("commandTextEdit"))
        self.steriographicRadioButton = QtGui.QRadioButton(self.grpCSpace_2)
        self.steriographicRadioButton.setGeometry(QtCore.QRect(390, 30, 117, 22))
        self.steriographicRadioButton.setObjectName(_fromUtf8("steriographicRadioButton"))

        self.retranslateUi(MeshNetCDF)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MeshNetCDF.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MeshNetCDF.reject)
        QtCore.QObject.connect(self.singleNetCDFChooseFilesRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.singleNetCDFChooseFilesLineEdit.setEnabled)
        QtCore.QObject.connect(self.singleNetCDFLayersRadioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.singleNetCDFLayerDropDown.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MeshNetCDF)

    def retranslateUi(self, MeshNetCDF):
        MeshNetCDF.setWindowTitle(QtGui.QApplication.translate("MeshNetCDF", "Mesh NetCDF", None, QtGui.QApplication.UnicodeUTF8))
        self.grpNCDF.setTitle(QtGui.QApplication.translate("MeshNetCDF", "Use NetCDF Mesh Metric", None, QtGui.QApplication.UnicodeUTF8))
        self.singleNetCDFChooseFilesPushButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.singleNetCDFLayersRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Choose From Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.singleNetCDFChooseFilesRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Choose File", None, QtGui.QApplication.UnicodeUTF8))
        self.singleNetCDFRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Use Single NetCDF File", None, QtGui.QApplication.UnicodeUTF8))
        self.addLayerToCanvasCheckBox.setText(QtGui.QApplication.translate("MeshNetCDF", "Add to Canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.multipleNetCDFFilesRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Calculate Minumum Value of Visible NetCDF Files", None, QtGui.QApplication.UnicodeUTF8))
        self.grpDom.setTitle(QtGui.QApplication.translate("MeshNetCDF", "Domain", None, QtGui.QApplication.UnicodeUTF8))
        self.domainShapefileLayerRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Domain Shapefile Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.grpDefID.setTitle(QtGui.QApplication.translate("MeshNetCDF", "Define Boundary ID ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MeshNetCDF", "ID Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MeshNetCDF", "Default ID", None, QtGui.QApplication.UnicodeUTF8))
        self.define_th.setText(QtGui.QApplication.translate("MeshNetCDF", "Define Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.lineRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.bSplineRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "BSpline", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MeshNetCDF", "Line Type", None, QtGui.QApplication.UnicodeUTF8))
        self.compoundCheckBox.setToolTip(QtGui.QApplication.translate("MeshNetCDF", "WARNING: Using Compound Lines increses the meshing time#", None, QtGui.QApplication.UnicodeUTF8))
        self.compoundCheckBox.setText(QtGui.QApplication.translate("MeshNetCDF", "Use Compound Lines", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseGeoFileRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Choose Geo File", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseGeoFilePushButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.grpCSpace_2.setTitle(QtGui.QApplication.translate("MeshNetCDF", "Generate Mesh", None, QtGui.QApplication.UnicodeUTF8))
        self.sphereRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Lon-Lat Sphere", None, QtGui.QApplication.UnicodeUTF8))
        self.flatRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Planar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MeshNetCDF", "Projection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MeshNetCDF", "Algorithm", None, QtGui.QApplication.UnicodeUTF8))
        self.commandEdit.setText(QtGui.QApplication.translate("MeshNetCDF", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.steriographicRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Steriographic", None, QtGui.QApplication.UnicodeUTF8))

