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
# Created: Fri Aug 31 11:19:24 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MeshNetCDF(object):
    def setupUi(self, MeshNetCDF):
        MeshNetCDF.setObjectName("MeshNetCDF")
        MeshNetCDF.resize(550, 640)
        self.buttonBox = QtGui.QDialogButtonBox(MeshNetCDF)
        self.buttonBox.setGeometry(QtCore.QRect(350, 590, 191, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtGui.QFrame(MeshNetCDF)
        self.frame.setGeometry(QtCore.QRect(10, 260, 531, 201))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grpNCDF = QtGui.QGroupBox(self.frame)
        self.grpNCDF.setEnabled(True)
        self.grpNCDF.setGeometry(QtCore.QRect(10, 10, 521, 191))
        self.grpNCDF.setToolTip("")
        self.grpNCDF.setWhatsThis("")
        self.grpNCDF.setAutoFillBackground(False)
        self.grpNCDF.setFlat(False)
        self.grpNCDF.setCheckable(True)
        self.grpNCDF.setChecked(True)
        self.grpNCDF.setObjectName("grpNCDF")
        self.singleNetCDFGroupBox = QtGui.QGroupBox(self.grpNCDF)
        self.singleNetCDFGroupBox.setEnabled(True)
        self.singleNetCDFGroupBox.setGeometry(QtCore.QRect(30, 50, 481, 81))
        self.singleNetCDFGroupBox.setTitle("")
        self.singleNetCDFGroupBox.setObjectName("singleNetCDFGroupBox")
        self.singleNetCDFChooseFilesPushButton = QtGui.QPushButton(self.singleNetCDFGroupBox)
        self.singleNetCDFChooseFilesPushButton.setEnabled(False)
        self.singleNetCDFChooseFilesPushButton.setGeometry(QtCore.QRect(390, 40, 85, 27))
        self.singleNetCDFChooseFilesPushButton.setObjectName("singleNetCDFChooseFilesPushButton")
        self.singleNetCDFChooseFilesLineEdit = QtGui.QLineEdit(self.singleNetCDFGroupBox)
        self.singleNetCDFChooseFilesLineEdit.setEnabled(False)
        self.singleNetCDFChooseFilesLineEdit.setGeometry(QtCore.QRect(180, 40, 201, 27))
        self.singleNetCDFChooseFilesLineEdit.setObjectName("singleNetCDFChooseFilesLineEdit")
        self.singleNetCDFLayersRadioButton = QtGui.QRadioButton(self.singleNetCDFGroupBox)
        self.singleNetCDFLayersRadioButton.setGeometry(QtCore.QRect(0, 10, 160, 22))
        self.singleNetCDFLayersRadioButton.setObjectName("singleNetCDFLayersRadioButton")
        self.singleNetCDFLayerDropDown = QtGui.QComboBox(self.singleNetCDFGroupBox)
        self.singleNetCDFLayerDropDown.setEnabled(False)
        self.singleNetCDFLayerDropDown.setGeometry(QtCore.QRect(180, 10, 201, 27))
        self.singleNetCDFLayerDropDown.setObjectName("singleNetCDFLayerDropDown")
        self.singleNetCDFChooseFilesRadioButton = QtGui.QRadioButton(self.singleNetCDFGroupBox)
        self.singleNetCDFChooseFilesRadioButton.setGeometry(QtCore.QRect(0, 40, 114, 22))
        self.singleNetCDFChooseFilesRadioButton.setObjectName("singleNetCDFChooseFilesRadioButton")
        self.singleNetCDFRadioButton = QtGui.QRadioButton(self.grpNCDF)
        self.singleNetCDFRadioButton.setGeometry(QtCore.QRect(10, 30, 183, 22))
        self.singleNetCDFRadioButton.setChecked(True)
        self.singleNetCDFRadioButton.setObjectName("singleNetCDFRadioButton")
        self.addLayerToCanvasCheckBox = QtGui.QCheckBox(self.grpNCDF)
        self.addLayerToCanvasCheckBox.setEnabled(False)
        self.addLayerToCanvasCheckBox.setGeometry(QtCore.QRect(30, 160, 126, 22))
        self.addLayerToCanvasCheckBox.setObjectName("addLayerToCanvasCheckBox")
        self.multipleNetCDFFilesRadioButton = QtGui.QRadioButton(self.grpNCDF)
        self.multipleNetCDFFilesRadioButton.setGeometry(QtCore.QRect(11, 130, 370, 22))
        self.multipleNetCDFFilesRadioButton.setChecked(False)
        self.multipleNetCDFFilesRadioButton.setObjectName("multipleNetCDFFilesRadioButton")
        self.frame_2 = QtGui.QFrame(MeshNetCDF)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 531, 241))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.grpDom = QtGui.QGroupBox(self.frame_2)
        self.grpDom.setGeometry(QtCore.QRect(10, 10, 521, 231))
        self.grpDom.setFlat(False)
        self.grpDom.setObjectName("grpDom")
        self.domainShapefileLayerDropDown = QtGui.QComboBox(self.grpDom)
        self.domainShapefileLayerDropDown.setGeometry(QtCore.QRect(210, 30, 201, 27))
        self.domainShapefileLayerDropDown.setObjectName("domainShapefileLayerDropDown")
        self.domainShapefileLayerRadioButton = QtGui.QRadioButton(self.grpDom)
        self.domainShapefileLayerRadioButton.setGeometry(QtCore.QRect(10, 30, 190, 22))
        self.domainShapefileLayerRadioButton.setChecked(True)
        self.domainShapefileLayerRadioButton.setObjectName("domainShapefileLayerRadioButton")
        self.grpDefID = QtGui.QGroupBox(self.grpDom)
        self.grpDefID.setEnabled(True)
        self.grpDefID.setGeometry(QtCore.QRect(30, 90, 391, 91))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.grpDefID.setFont(font)
        self.grpDefID.setAcceptDrops(False)
        self.grpDefID.setCheckable(True)
        self.grpDefID.setChecked(False)
        self.grpDefID.setObjectName("grpDefID")
        self.label_2 = QtGui.QLabel(self.grpDefID)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.label_2.setObjectName("label_2")
        self.IdDropdown = QtGui.QComboBox(self.grpDefID)
        self.IdDropdown.setGeometry(QtCore.QRect(180, 30, 201, 27))
        self.IdDropdown.setObjectName("IdDropdown")
        self.label_3 = QtGui.QLabel(self.grpDefID)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 71, 17))
        self.label_3.setObjectName("label_3")
        self.Default_Id = QtGui.QLineEdit(self.grpDefID)
        self.Default_Id.setGeometry(QtCore.QRect(180, 60, 201, 27))
        self.Default_Id.setObjectName("Default_Id")
        self.grpChooseGeo = QtGui.QGroupBox(self.grpDom)
        self.grpChooseGeo.setEnabled(True)
        self.grpChooseGeo.setGeometry(QtCore.QRect(10, 190, 501, 41))
        self.grpChooseGeo.setTitle("")
        self.grpChooseGeo.setObjectName("grpChooseGeo")
        self.chooseGeoFileRadioButton = QtGui.QRadioButton(self.grpChooseGeo)
        self.chooseGeoFileRadioButton.setGeometry(QtCore.QRect(0, 0, 177, 22))
        self.chooseGeoFileRadioButton.setChecked(False)
        self.chooseGeoFileRadioButton.setObjectName("chooseGeoFileRadioButton")
        self.chooseGeoFileLineEdit = QtGui.QLineEdit(self.grpChooseGeo)
        self.chooseGeoFileLineEdit.setEnabled(True)
        self.chooseGeoFileLineEdit.setGeometry(QtCore.QRect(200, 0, 201, 27))
        self.chooseGeoFileLineEdit.setObjectName("chooseGeoFileLineEdit")
        self.chooseGeoFilePushButton = QtGui.QPushButton(self.grpChooseGeo)
        self.chooseGeoFilePushButton.setEnabled(True)
        self.chooseGeoFilePushButton.setGeometry(QtCore.QRect(410, 0, 85, 27))
        self.chooseGeoFilePushButton.setObjectName("chooseGeoFilePushButton")
        self.Threshold = QtGui.QLineEdit(self.grpDom)
        self.Threshold.setEnabled(True)
        self.Threshold.setGeometry(QtCore.QRect(210, 60, 201, 27))
        self.Threshold.setObjectName("Threshold")
        self.define_th = QtGui.QCheckBox(self.grpDom)
        self.define_th.setEnabled(True)
        self.define_th.setGeometry(QtCore.QRect(30, 60, 141, 22))
        self.define_th.setObjectName("define_th")
        self.frame_5 = QtGui.QFrame(MeshNetCDF)
        self.frame_5.setGeometry(QtCore.QRect(10, 470, 531, 111))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.grpCSpace_2 = QtGui.QGroupBox(self.frame_5)
        self.grpCSpace_2.setGeometry(QtCore.QRect(10, 10, 511, 91))
        self.grpCSpace_2.setCheckable(True)
        self.grpCSpace_2.setObjectName("grpCSpace_2")
        self.sphereRadioButton = QtGui.QRadioButton(self.grpCSpace_2)
        self.sphereRadioButton.setGeometry(QtCore.QRect(300, 30, 93, 22))
        self.sphereRadioButton.setObjectName("sphereRadioButton")
        self.meshingAlgorithmDropDown = QtGui.QComboBox(self.grpCSpace_2)
        self.meshingAlgorithmDropDown.setGeometry(QtCore.QRect(210, 60, 201, 27))
        self.meshingAlgorithmDropDown.setObjectName("meshingAlgorithmDropDown")
        self.flatRadioButton = QtGui.QRadioButton(self.grpCSpace_2)
        self.flatRadioButton.setGeometry(QtCore.QRect(210, 30, 74, 22))
        self.flatRadioButton.setAcceptDrops(False)
        self.flatRadioButton.setChecked(True)
        self.flatRadioButton.setObjectName("flatRadioButton")
        self.label = QtGui.QLabel(self.grpCSpace_2)
        self.label.setGeometry(QtCore.QRect(40, 30, 120, 17))
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(self.grpCSpace_2)
        self.label_4.setGeometry(QtCore.QRect(40, 60, 69, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(MeshNetCDF)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), MeshNetCDF.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), MeshNetCDF.reject)
        QtCore.QObject.connect(self.singleNetCDFChooseFilesRadioButton, QtCore.SIGNAL("toggled(bool)"), self.singleNetCDFChooseFilesLineEdit.setEnabled)
        QtCore.QObject.connect(self.singleNetCDFLayersRadioButton, QtCore.SIGNAL("toggled(bool)"), self.singleNetCDFLayerDropDown.setEnabled)
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
        self.chooseGeoFileRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Choose Geo File", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseGeoFilePushButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.define_th.setText(QtGui.QApplication.translate("MeshNetCDF", "Define Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.grpCSpace_2.setTitle(QtGui.QApplication.translate("MeshNetCDF", "Generate Mesh", None, QtGui.QApplication.UnicodeUTF8))
        self.sphereRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Spherical", None, QtGui.QApplication.UnicodeUTF8))
        self.flatRadioButton.setText(QtGui.QApplication.translate("MeshNetCDF", "Planar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MeshNetCDF", "Projection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MeshNetCDF", "Algorithm", None, QtGui.QApplication.UnicodeUTF8))

