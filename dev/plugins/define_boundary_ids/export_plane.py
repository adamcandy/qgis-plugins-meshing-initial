from PyQt4.QtCore import * 

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

from PyQt4.QtGui import *
from qgis.core import *
import math

def same_point(x1,y1,x2,y2):
  dist = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
  return (dist<=0.000001)



def export(shpFile ,filePath):

	# The function exports the shp file to a .geo. If there isn't any .shp file created, the user will be promped an error.

	geoFile =  open(filePath + ".geo","w")
	shapes =  shpFile.shapes()
	records = shpFile.records()
	pId = 1
	lId = 1
	zCoord = 0
	meshSize = 0.5
	phLine = []
	geoFile.write("zCoord = %f;\n" %zCoord)
	geoFile.write("meshSize = %f;\n" %meshSize)

	# First of all, we'll remove the duplicates

	for i in range(len(shapes)):
		for j in range(len(shapes[i].points)-1):
			while j < len(shapes[i].points)-1 and same_point(shapes[i].points[j][0], shapes[i].points[j][1], shapes[i].points[j+1][0], shapes[i].points[j+1][1]):
				trash = shapes[i].points.pop(j+1)
		trash = shapes[i].points.pop()
	i = 0
	while i < len(shapes):
		if(len(shapes[i].points) == 0):
			trash = shapes.pop(i)
			trash = records.pop(i)
		else:
			i+=1 

	# This for-loop extracts all the points, one by one, and writes them as it goes along

	for i in range(len(shapes)):
		shape = shapes[i]
		for coord in shape.points:
			geoFile.write("Point(%d) = {%f, %f, zCoord};\n" %(pId, coord[0], coord[1]))
			pId+=1
	pId = 1
	lId = 1
	# This for-loop writes the lines of the file. Each geometric shape (boundary and island) will get an extra edge to close its poligon.
	i = 0
	lLoopId = 1

	planeSurface= "Plane Surface(1)={1"
	while i < len(shapes):
		init = pId
		polyId = records[i][1]
		lLoop = "Line Loop(" + str(lLoopId) + ") = {"
		while(i<len(shapes) and polyId == records[i][1]):
			shape = shapes[i]

			for j in range(len(shape.points)):
				if j==len(shape.points)-1 and (i==len(shapes)-1 or polyId!=records[i+1][1]):
					geoFile.write("Line(%d) = {%d, %d};\n" %(lId ,pId, init))
					lLoop += str(lId) + "};\n"
					phLine.append((int(records[i][0]),lId))
				else:
					geoFile.write("Line(%d) = {%d, %d};\n" %(lId, pId, pId+1))
					lLoop += str(lId) + ", "
					phLine.append((int(records[i][0]),lId))
				lId+=1
				pId+=1
			i+=1

		geoFile.write(lLoop)
		if lLoopId>1:
			planeSurface += ", " + str(lLoopId)
		lLoopId+=1
	planeSurface += "};\n"
	# The boundary can be splitted into many different shapes. That's why, the first line loop will contain only the boundary, regardless of how many shape it may encapsulate.
	# Puts ths ids in the file as physical lines.
	# How it works: Takes the first element's id, passes it into the file as the id of a physical line and loops through the entire array, searching for lines with the same id. The lines that are found are added to that specific physical line and are deleted from the phLine array. All this stops when phLine will be empty.
	pids = ""
	while len(phLine) > 0:  
		finalId = phLine[0][0] 
		ok = False
		geoFile.write("Physical Line(%d) = {" %finalId)
		i = 0 
		while i < len(phLine):
			if phLine[i][0] == finalId:
				if ok:
					pids+=", "
					geoFile.write(", ")
				ok = True
				pids+=str(phLine[i][1])
				geoFile.write(str(phLine[i][1]))
				phLine.remove(phLine[i])
				continue
			i+=1   
		geoFile.write("};\n")
	
	
	geoFile.write("Physical Surface(1)={1};\n")
	geoFile.write(planeSurface)

	# Additional lines which help the meshing algorithm:
	
	geoFile.write("Printf(\"Assigning characteristic mesh sizes...\");\n")
	geoFile.write("Field[1] = Attractor;\n")
	geoFile.write("Field[1].EdgesList = {%s};\n" %pids) 
	geoFile.write("Field[1].NNodesByEdge = 50;\n")
	geoFile.write("Field[2] = Threshold;\n")
	geoFile.write("Field[2].DistMax = 50000;\n")
	geoFile.write("Field[2].DistMin = 500;\n")
	geoFile.write("Field[2].IField = 1;\n")
	geoFile.write("Field[2].LcMin = 5000;\n")
	geoFile.write("Field[2].LcMax = 50000;\n")
	geoFile.write("Background Field = 2;\n")
	geoFile.write("// Dont extent the elements sizes from the boundary inside the domain\n")
	geoFile.write("Mesh.CharacteristicLengthExtendFromBoundary = 0;\n")
	geoFile.write("//Set some options for better png output\n")
	geoFile.write("General.Color.Background = {255,255,255};\n")
	geoFile.write("General.Color.BackgroundGradient = {255,255,255};\n")
	geoFile.write("General.Color.Foreground = Black;\n")
	geoFile.write("Mesh.Color.Lines = {0,0,0}; \n")
	geoFile.close()
