import os
import arcpy

root = os.path.dirname(__file__)
arcpy.env.workspace = root

mxd = arcpy.mapping.MapDocument(os.path.join(root, 'doc.mxd'))
df = arcpy.mapping.ListDataFrames(mxd, "Central United States")[0]

arcpy.mapping.ExportToPDF(mxd, os.path.join(root, 'outputs/doc.pdf'), resolution=300)

del mxd