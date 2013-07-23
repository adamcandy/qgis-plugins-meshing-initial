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

# Form implementation generated from reading ui file 'ui_rasterisepolygons.ui'
#
# Created: Thu Aug 23 12:08:36 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RasterisePolygons(object):
    def setupUi(self, RasterisePolygons):
        RasterisePolygons.setObjectName("RasterisePolygons")
        RasterisePolygons.resize(532, 361)
        self.buttonBox = QtGui.QDialogButtonBox(RasterisePolygons)
        self.buttonBox.setGeometry(QtCore.QRect(170, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.singlePolygonLayerDropDown = QtGui.QComboBox(RasterisePolygons)
        self.singlePolygonLayerDropDown.setEnabled(False)
        self.singlePolygonLayerDropDown.setGeometry(QtCore.QRect(240, 70, 181, 27))
        self.singlePolygonLayerDropDown.setObjectName("singlePolygonLayerDropDown")
        self.polygonsChooseFromFileLineEdit = QtGui.QLineEdit(RasterisePolygons)
        self.polygonsChooseFromFileLineEdit.setEnabled(False)
        self.polygonsChooseFromFileLineEdit.setGeometry(QtCore.QRect(240, 100, 181, 27))
        self.polygonsChooseFromFileLineEdit.setObjectName("polygonsChooseFromFileLineEdit")
        self.polygonsChooseFromFilePushButton = QtGui.QPushButton(RasterisePolygons)
        self.polygonsChooseFromFilePushButton.setEnabled(False)
        self.polygonsChooseFromFilePushButton.setGeometry(QtCore.QRect(430, 100, 85, 27))
        self.polygonsChooseFromFilePushButton.setObjectName("polygonsChooseFromFilePushButton")
        self.backgroundLayerDropDown = QtGui.QComboBox(RasterisePolygons)
        self.backgroundLayerDropDown.setGeometry(QtCore.QRect(240, 180, 181, 27))
        self.backgroundLayerDropDown.setObjectName("backgroundLayerDropDown")
        self.backgroundLayerLineEdit = QtGui.QLineEdit(RasterisePolygons)
        self.backgroundLayerLineEdit.setEnabled(False)
        self.backgroundLayerLineEdit.setGeometry(QtCore.QRect(240, 210, 181, 27))
        self.backgroundLayerLineEdit.setObjectName("backgroundLayerLineEdit")
        self.backgroundLayerChooseFromFilePushButton = QtGui.QPushButton(RasterisePolygons)
        self.backgroundLayerChooseFromFilePushButton.setEnabled(False)
        self.backgroundLayerChooseFromFilePushButton.setGeometry(QtCore.QRect(430, 210, 85, 27))
        self.backgroundLayerChooseFromFilePushButton.setObjectName("backgroundLayerChooseFromFilePushButton")
        self.choosePolygonsGroupBox = QtGui.QGroupBox(RasterisePolygons)
        self.choosePolygonsGroupBox.setGeometry(QtCore.QRect(10, 20, 211, 111))
        self.choosePolygonsGroupBox.setObjectName("choosePolygonsGroupBox")
        self.layoutWidget = QtGui.QWidget(self.choosePolygonsGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 231, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allVisiblePolygonLayersRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.allVisiblePolygonLayersRadioButton.setChecked(True)
        self.allVisiblePolygonLayersRadioButton.setObjectName("allVisiblePolygonLayersRadioButton")
        self.verticalLayout.addWidget(self.allVisiblePolygonLayersRadioButton)
        self.singlePolygonLayerRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.singlePolygonLayerRadioButton.setObjectName("singlePolygonLayerRadioButton")
        self.verticalLayout.addWidget(self.singlePolygonLayerRadioButton)
        self.polygonsChooseFromFileRadioButton = QtGui.QRadioButton(self.layoutWidget)
        self.polygonsChooseFromFileRadioButton.setObjectName("polygonsChooseFromFileRadioButton")
        self.verticalLayout.addWidget(self.polygonsChooseFromFileRadioButton)
        self.chooseBackgroundGroupBox = QtGui.QGroupBox(RasterisePolygons)
        self.chooseBackgroundGroupBox.setGeometry(QtCore.QRect(10, 160, 191, 91))
        self.chooseBackgroundGroupBox.setTitle("")
        self.chooseBackgroundGroupBox.setObjectName("chooseBackgroundGroupBox")
        self.layoutWidget1 = QtGui.QWidget(self.chooseBackgroundGroupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 16, 181, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.backgroundLayerChooseFromLayerRadioButton = QtGui.QRadioButton(self.layoutWidget1)
        self.backgroundLayerChooseFromLayerRadioButton.setChecked(True)
        self.backgroundLayerChooseFromLayerRadioButton.setObjectName("backgroundLayerChooseFromLayerRadioButton")
        self.verticalLayout_2.addWidget(self.backgroundLayerChooseFromLayerRadioButton)
        self.backgroundLayerChooseFromFileRadioButton = QtGui.QRadioButton(self.layoutWidget1)
        self.backgroundLayerChooseFromFileRadioButton.setEnabled(True)
        self.backgroundLayerChooseFromFileRadioButton.setObjectName("backgroundLayerChooseFromFileRadioButton")
        self.verticalLayout_2.addWidget(self.backgroundLayerChooseFromFileRadioButton)
        self.line = QtGui.QFrame(RasterisePolygons)
        self.line.setGeometry(QtCore.QRect(10, 290, 501, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtGui.QLabel(RasterisePolygons)
        self.label.setGeometry(QtCore.QRect(10, 150, 399, 17))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.backgroundValueLineEdit = QtGui.QLineEdit(RasterisePolygons)
        self.backgroundValueLineEdit.setGeometry(QtCore.QRect(240, 250, 181, 27))
        self.backgroundValueLineEdit.setObjectName("backgroundValueLineEdit")
        self.label_2 = QtGui.QLabel(RasterisePolygons)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 177, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(RasterisePolygons)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), RasterisePolygons.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), RasterisePolygons.reject)
        QtCore.QMetaObject.connectSlotsByName(RasterisePolygons)

    def retranslateUi(self, RasterisePolygons):
        RasterisePolygons.setWindowTitle(QtGui.QApplication.translate("RasterisePolygons", "Rasterise Polygons", None, QtGui.QApplication.UnicodeUTF8))
        self.polygonsChooseFromFilePushButton.setText(QtGui.QApplication.translate("RasterisePolygons", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundLayerChooseFromFilePushButton.setText(QtGui.QApplication.translate("RasterisePolygons", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.choosePolygonsGroupBox.setTitle(QtGui.QApplication.translate("RasterisePolygons", "Choose Polygons", None, QtGui.QApplication.UnicodeUTF8))
        self.allVisiblePolygonLayersRadioButton.setText(QtGui.QApplication.translate("RasterisePolygons", "All Visible Polygon Layers", None, QtGui.QApplication.UnicodeUTF8))
        self.singlePolygonLayerRadioButton.setText(QtGui.QApplication.translate("RasterisePolygons", "Single Polygon Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.polygonsChooseFromFileRadioButton.setText(QtGui.QApplication.translate("RasterisePolygons", "Choose From File", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundLayerChooseFromLayerRadioButton.setText(QtGui.QApplication.translate("RasterisePolygons", "Choose From Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundLayerChooseFromFileRadioButton.setText(QtGui.QApplication.translate("RasterisePolygons", "Choose From File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RasterisePolygons", "Choose Background Layer for the Extent of New Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RasterisePolygons", "Value Outside of Polygons", None, QtGui.QApplication.UnicodeUTF8))

