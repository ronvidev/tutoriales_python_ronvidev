import os
import arcpy

root = os.path.dirname(__file__)
mxd_path = os.path.join(root, 'doc.mxd')

mxd = arcpy.mapping.MapDocument(mxd_path)

arcpy.mapping.PrintMap(mxd, "HP Ink Tank 310 series")

del mxd
