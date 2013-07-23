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

# Form implementation generated from reading ui file 'rastercalcdialogbase.ui'
#
# Created: Fri Jul  6 09:54:39 2012
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RasterCalcDialog(object):
    def setupUi(self, RasterCalcDialog):
    
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
    
    
    
        RasterCalcDialog.setObjectName(_fromUtf8("RasterCalcDialog"))
        RasterCalcDialog.resize(741, 379)
        RasterCalcDialog.setSizeGripEnabled(False)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RasterCalcDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.rasterTree = QtGui.QTreeWidget(RasterCalcDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rasterTree.sizePolicy().hasHeightForWidth())
        self.rasterTree.setSizePolicy(sizePolicy)
        self.rasterTree.setMinimumSize(QtCore.QSize(180, 0))
        self.rasterTree.setObjectName(_fromUtf8("rasterTree"))
        self.horizontalLayout_2.addWidget(self.rasterTree)
        self.bandList = QtGui.QListWidget(RasterCalcDialog)
        self.bandList.setObjectName(_fromUtf8("bandList"))
        self.horizontalLayout_2.addWidget(self.bandList)
        self.frame = QtGui.QFrame(RasterCalcDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        
        self.btnRParen = QtGui.QPushButton(self.frame)
        self.btnRParen.setObjectName(_fromUtf8("btnRParen"))
        self.gridLayout_10.addWidget(self.btnRParen,1,0,1,1)
        

        self.btnLParen = QtGui.QPushButton(self.frame)
        self.btnLParen.setObjectName(_fromUtf8("btnLParen"))
        self.gridLayout_10.addWidget(self.btnLParen,1,1,1,1)
        self.btnBand = QtGui.QPushButton(self.frame)
        self.btnBand.setObjectName(_fromUtf8("btnBand"))
        self.gridLayout_10.addWidget(self.btnBand,0,3,1,1)
        self.btnClip = QtGui.QPushButton(self.frame)
        self.btnClip.setEnabled(False)
        self.btnClip.setObjectName(_fromUtf8("btnClip"))
        self.gridLayout_10.addWidget(self.btnClip,0,4,1,1)
        
        
        #check if needed
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        
        
        self.cmbPresets = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPresets.sizePolicy().hasHeightForWidth())
        self.cmbPresets.setSizePolicy(sizePolicy)
        self.cmbPresets.setObjectName(_fromUtf8("cmbPresets"))
        self.cmbPresets.addItem(_fromUtf8(""))
        self.cmbPresets.addItem(_fromUtf8(""))
        self.btnSin = QtGui.QPushButton(self.frame)
        self.btnSin.setObjectName(_fromUtf8("btnSin"))
        self.gridLayout_10.addWidget(self.btnSin, 1, 3, 1, 1)
        self.btnAsin = QtGui.QPushButton(self.frame)
        self.btnAsin.setObjectName(_fromUtf8("btnAsin"))
        self.gridLayout_10.addWidget(self.btnAsin, 1, 4, 1, 1)
        self.btnExp = QtGui.QPushButton(self.frame)
        self.btnExp.setObjectName(_fromUtf8("btnExp"))
        self.gridLayout_10.addWidget(self.btnExp, 2, 0, 1, 1)
        self.btnCos = QtGui.QPushButton(self.frame)
        self.btnCos.setObjectName(_fromUtf8("btnCos"))
        self.gridLayout_10.addWidget(self.btnCos, 2, 3, 1, 1)
        self.btnAcos = QtGui.QPushButton(self.frame)
        self.btnAcos.setObjectName(_fromUtf8("btnAcos"))
        self.gridLayout_10.addWidget(self.btnAcos, 2, 4, 1, 1)
        self.btnLn = QtGui.QPushButton(self.frame)
        self.btnLn.setObjectName(_fromUtf8("btnLn"))
        self.gridLayout_10.addWidget(self.btnLn, 2, 1, 1, 1)
        self.btnTan = QtGui.QPushButton(self.frame)
        self.btnTan.setObjectName(_fromUtf8("btnTan"))
        self.gridLayout_10.addWidget(self.btnTan, 3, 3, 1, 1)
        self.btnAtan = QtGui.QPushButton(self.frame)
        self.btnAtan.setObjectName(_fromUtf8("btnAtan"))
        self.gridLayout_10.addWidget(self.btnAtan, 3, 4, 1, 1)
        self.btnPower = QtGui.QPushButton(self.frame)
        self.btnPower.setObjectName(_fromUtf8("btnPower"))
        self.gridLayout_10.addWidget(self.btnPower, 5, 2, 1, 1)
        
        
        self.btnIntX = QtGui.QPushButton(self.frame)
        self.btnIntX.setObjectName(_fromUtf8("btnIntX"))
        self.gridLayout_10.addWidget(self.btnIntX, 4, 1, 1, 1)
        
        self.btnIntY = QtGui.QPushButton(self.frame)
        self.btnIntY.setObjectName(_fromUtf8("btnIntY"))
        self.gridLayout_10.addWidget(self.btnIntY, 4, 0, 1, 1)
        
        self.btnDvg = QtGui.QPushButton(self.frame)
        self.btnDvg.setObjectName(_fromUtf8("btnDvg"))
        self.gridLayout_10.addWidget(self.btnDvg, 4, 4, 1, 1)
        
        self.btnIntS = QtGui.QPushButton(self.frame)
        self.btnIntS.setObjectName(_fromUtf8("btnIntS"))
        self.gridLayout_10.addWidget(self.btnIntS, 3, 0, 1, 1)
        
        self.btnIntF = QtGui.QPushButton(self.frame)
        self.btnIntF.setObjectName(_fromUtf8("btnIntF"))
        self.gridLayout_10.addWidget(self.btnIntF, 3, 1, 1, 1)
        
        self.btnDdf = QtGui.QPushButton(self.frame)
        self.btnDdf.setObjectName(_fromUtf8("btnDdf"))
        self.gridLayout_10.addWidget(self.btnDdf, 4, 3, 1, 1)
        self.gridLayout_10.addWidget(self.cmbPresets, 0, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_10,5,0,1,1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 4, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnMul = QtGui.QPushButton(self.frame)
        self.btnMul.setObjectName(_fromUtf8("btnMul"))
        self.gridLayout_10.addWidget(self.btnMul,4,2,1,1)
        self.btnDiv = QtGui.QPushButton(self.frame)
        self.btnDiv.setObjectName(_fromUtf8("btnDiv"))
        self.gridLayout_10.addWidget(self.btnDiv,3,2,1,1)
        self.btnSub = QtGui.QPushButton(self.frame)
        self.btnSub.setObjectName(_fromUtf8("btnSub"))
        self.gridLayout_10.addWidget(self.btnSub,2,2,1,1)
        self.btnAdd = QtGui.QPushButton(self.frame)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.gridLayout_10.addWidget(self.btnAdd,1,2,1,1)
        self.horizontalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10 = QtGui.QVBoxLayout(RasterCalcDialog)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.btnddx = QtGui.QPushButton(self.frame)
        self.btnddx.setObjectName(_fromUtf8("btnddx"))
        self.gridLayout_10.addWidget(self.btnddx,5,1,1,1)
        
        self.btnDdy = QtGui.QPushButton(self.frame)
        self.btnDdy.setObjectName(_fromUtf8("btnDdy"))
        self.verticalLayout_10.addWidget(self.btnDdy)
        self.gridLayout_10.addLayout(self.verticalLayout_10, 5, 0, 1, 1)
        
        self.verticalLayout_11 = QtGui.QVBoxLayout(RasterCalcDialog)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.btnMmin = QtGui.QPushButton(self.frame)
        self.btnMmin.setObjectName(_fromUtf8("btnMmin"))
        self.gridLayout_10.addWidget(self.btnMmin,5,3,1,1)
        
        self.btnMmax = QtGui.QPushButton(self.frame)
        self.btnMmax.setObjectName(_fromUtf8("btnMmax"))
        self.gridLayout_10.addWidget(self.btnMmax,5,4,1,1)
				
        self.btnAbs = QtGui.QPushButton(self.frame)
        self.btnAbs.setObjectName(_fromUtf8("btnAbs"))
        self.gridLayout_10.addWidget(self.btnAbs,6,0,1,1)
					
        self.btnLt = QtGui.QPushButton(self.frame) 
        self.btnLt.setObjectName(_fromUtf8("btnLt"))
        self.gridLayout_10.addWidget(self.btnLt,6,1,1,1)
					
        self.btnGt = QtGui.QPushButton(self.frame) 
        self.btnGt.setObjectName(_fromUtf8("btnGt"))
        self.gridLayout_10.addWidget(self.btnGt,6,3,1,1)
				
        self.btnSqrt = QtGui.QPushButton(self.frame)
        self.btnSqrt.setObjectName(_fromUtf8("btnSqrt"))
        self.gridLayout_10.addWidget(self.btnSqrt,6,4,1,1)
				
        self.btnLog = QtGui.QPushButton(self.frame)
        self.btnLog.setObjectName(_fromUtf8("btnLog"))
        self.gridLayout_10.addWidget(self.btnLog,6,2,1,1)
					
        #self.gridLayout_3.addLayout(self.verticalLayout_11, 4, 1, 1, 1)
        
        
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.commandTextEdit = QtGui.QTextEdit(RasterCalcDialog)
        self.commandTextEdit.setObjectName(_fromUtf8("commandTextEdit"))
        self.horizontalLayout_3.addWidget(self.commandTextEdit)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.btnClearCommand = QtGui.QPushButton(RasterCalcDialog)
        self.btnClearCommand.setObjectName(_fromUtf8("btnClearCommand"))
        self.verticalLayout_4.addWidget(self.btnClearCommand)
        self.btnSaveExpression = QtGui.QPushButton(RasterCalcDialog)
        self.btnSaveExpression.setEnabled(False)
        self.btnSaveExpression.setObjectName(_fromUtf8("btnSaveExpression"))
        self.verticalLayout_4.addWidget(self.btnSaveExpression)
        self.btnLoadExpression = QtGui.QPushButton(RasterCalcDialog)
        self.btnLoadExpression.setObjectName(_fromUtf8("btnLoadExpression"))
        self.verticalLayout_4.addWidget(self.btnLoadExpression)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(RasterCalcDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.cmbPixelFormat = QtGui.QComboBox(RasterCalcDialog)
        self.cmbPixelFormat.setObjectName(_fromUtf8("cmbPixelFormat"))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.cmbPixelFormat.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cmbPixelFormat)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(RasterCalcDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.leFileName = QtGui.QLineEdit(RasterCalcDialog)
        self.leFileName.setObjectName(_fromUtf8("leFileName"))
        self.horizontalLayout.addWidget(self.leFileName)
        self.btnBrowse = QtGui.QPushButton(RasterCalcDialog)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.loadCheckBox = QtGui.QCheckBox(RasterCalcDialog)
        self.loadCheckBox.setObjectName(_fromUtf8("loadCheckBox"))
        self.verticalLayout_2.addWidget(self.loadCheckBox)
        self.buttonBox = QtGui.QDialogButtonBox(RasterCalcDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.retranslateUi(RasterCalcDialog)
        self.bandList.setCurrentRow(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RasterCalcDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RasterCalcDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RasterCalcDialog)

    def retranslateUi(self, RasterCalcDialog):
        RasterCalcDialog.setWindowTitle(QtGui.QApplication.translate("RasterCalcDialog", "RasterCalc", None, QtGui.QApplication.UnicodeUTF8))
        self.rasterTree.headerItem().setText(0, QtGui.QApplication.translate("RasterCalcDialog", "Available rasters", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRParen.setText(QtGui.QApplication.translate("RasterCalcDialog", "(", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRParen.setToolTip("Left Parenthesis")

        self.btnAbs.setText(QtGui.QApplication.translate("RasterCalcDialog", "abs", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAbs.setToolTip("Absolute Value")

        self.btnLog.setText(QtGui.QApplication.translate("RasterCalcDialog", "log", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLog.setToolTip("Logrithmic")

        self.btnLt.setText(QtGui.QApplication.translate("RasterCalcDialog", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLt.setToolTip("Less Than")

        self.btnGt.setText(QtGui.QApplication.translate("RasterCalcDialog", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGt.setToolTip("Greater Than")
        
        self.btnSqrt.setText(QtGui.QApplication.translate("RasterCalcDialog", "sqrt", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSqrt.setToolTip("Square Root")


        self.btnLParen.setText(QtGui.QApplication.translate("RasterCalcDialog", ")", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLParen.setToolTip("Right Parenthesis")
        self.btnddx.setText(QtGui.QApplication.translate("RasterCalcDialog", "ddx", None, QtGui.QApplication.UnicodeUTF8))
        self.btnddx.setToolTip("Derivitive with respect to x")
        self.btnDdy.setText(QtGui.QApplication.translate("RasterCalcDialog", "ddy", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDdy.setToolTip("Derivitive with respect to y")
        self.btnIntX.setText(QtGui.QApplication.translate("RasterCalcDialog", "intx", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIntX.setToolTip("Integrate with respect to x")
        self.btnIntY.setText(QtGui.QApplication.translate("RasterCalcDialog", "inty", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIntY.setToolTip("Integrate with respect to y")
        self.btnDvg.setText(QtGui.QApplication.translate("RasterCalcDialog", "dvg", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDvg.setToolTip("Divergence")
        self.btnIntS.setText(QtGui.QApplication.translate("RasterCalcDialog", "intS", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIntS.setToolTip("Surface Integral")
        self.btnIntF.setText(QtGui.QApplication.translate("RasterCalcDialog", "intF", None, QtGui.QApplication.UnicodeUTF8))
        self.btnIntF.setToolTip("Integrate Fields")
        self.btnDdf.setText(QtGui.QApplication.translate("RasterCalcDialog", "ddF", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDdf.setToolTip("Differentiate fields")
        self.btnMmin.setText(QtGui.QApplication.translate("RasterCalcDialog", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMmin.setToolTip("Minimum of upto 10 values")
        self.btnMmax.setText(QtGui.QApplication.translate("RasterCalcDialog", "max", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMmax.setToolTip("Maximum of upto 10 values")
        self.btnBand.setWhatsThis(QtGui.QApplication.translate("RasterCalcDialog", "Get band from raster", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBand.setText(QtGui.QApplication.translate("RasterCalcDialog", "@", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBand.setToolTip("Get band from raster layer")
        self.btnClip.setWhatsThis(QtGui.QApplication.translate("RasterCalcDialog", "Clip lower and upper values", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClip.setToolTip("Clip Lower and upper Values")
        self.btnClip.setText(QtGui.QApplication.translate("RasterCalcDialog", "clip", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPresets.setItemText(0, QtGui.QApplication.translate("RasterCalcDialog", "NDVI (TM/ETM+)", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPresets.setItemText(1, QtGui.QApplication.translate("RasterCalcDialog", "Difference", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSin.setText(QtGui.QApplication.translate("RasterCalcDialog", "sin", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSin.setToolTip("Sine")
        self.btnAsin.setText(QtGui.QApplication.translate("RasterCalcDialog", "asin", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAsin.setToolTip("Inverse Sine")
        self.btnExp.setText(QtGui.QApplication.translate("RasterCalcDialog", "exp", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExp.setToolTip("Exponantial")
        self.btnCos.setText(QtGui.QApplication.translate("RasterCalcDialog", "cos", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCos.setToolTip("Cosine")
        self.btnAcos.setText(QtGui.QApplication.translate("RasterCalcDialog", "acos", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAcos.setToolTip("Inverse Cosine")
        self.btnLn.setText(QtGui.QApplication.translate("RasterCalcDialog", "ln", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLn.setToolTip("Natural Logrithmic")
        self.btnTan.setText(QtGui.QApplication.translate("RasterCalcDialog", "tan", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTan.setToolTip("Tan")
        self.btnAtan.setText(QtGui.QApplication.translate("RasterCalcDialog", "atan", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAtan.setToolTip("Inverse tan")
        self.btnPower.setWhatsThis(QtGui.QApplication.translate("RasterCalcDialog", "Raise to power", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPower.setToolTip("Power")
        self.btnPower.setText(QtGui.QApplication.translate("RasterCalcDialog", "^", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMul.setWhatsThis(QtGui.QApplication.translate("RasterCalcDialog", "Multiply arguments", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMul.setToolTip("Multiply Arguments")
        self.btnMul.setText(QtGui.QApplication.translate("RasterCalcDialog", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDiv.setWhatsThis(QtGui.QApplication.translate("RasterCalcDialog", "Divide arguments", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDiv.setToolTip("Divide argumets")
        self.btnDiv.setText(QtGui.QApplication.translate("RasterCalcDialog", "/", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSub.setWhatsThis(QtGui.QApplication.translate("RasterCalcDialog", "Subtract argiments", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSub.setToolTip("Subtract arguments")
        self.btnSub.setText(QtGui.QApplication.translate("RasterCalcDialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setWhatsThis(QtGui.QApplication.translate("RasterCalcDialog", "Add arguments", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setToolTip("Add arguments")
        self.btnAdd.setText(QtGui.QApplication.translate("RasterCalcDialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClearCommand.setText(QtGui.QApplication.translate("RasterCalcDialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSaveExpression.setText(QtGui.QApplication.translate("RasterCalcDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoadExpression.setText(QtGui.QApplication.translate("RasterCalcDialog", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RasterCalcDialog", "Data type", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(0, QtGui.QApplication.translate("RasterCalcDialog", "Byte", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(1, QtGui.QApplication.translate("RasterCalcDialog", "UInt16", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(2, QtGui.QApplication.translate("RasterCalcDialog", "Int16", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(3, QtGui.QApplication.translate("RasterCalcDialog", "UInt32", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(4, QtGui.QApplication.translate("RasterCalcDialog", "Int32", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(5, QtGui.QApplication.translate("RasterCalcDialog", "Float32", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(6, QtGui.QApplication.translate("RasterCalcDialog", "Float64", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(7, QtGui.QApplication.translate("RasterCalcDialog", "CInt16", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(8, QtGui.QApplication.translate("RasterCalcDialog", "CInt32", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(9, QtGui.QApplication.translate("RasterCalcDialog", "CFloat32", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbPixelFormat.setItemText(10, QtGui.QApplication.translate("RasterCalcDialog", "CFloat64", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RasterCalcDialog", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBrowse.setText(QtGui.QApplication.translate("RasterCalcDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.loadCheckBox.setText(QtGui.QApplication.translate("RasterCalcDialog", "Add result to the map canvas", None, QtGui.QApplication.UnicodeUTF8))

