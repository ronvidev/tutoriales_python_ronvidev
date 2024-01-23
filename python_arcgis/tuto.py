import arcpy

arcpy.env.workspace = r"C:\Users\ronal\Desktop\testa"

mxd = arcpy.mapping.MapDocument(r"F:\CarpetasW\Documentos\ArcGIS\test.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Southwestern United States")[0]


arcpy.mapping.ExportToPDF(mxd, r"F:\CarpetasW\Documentos\ArcGIS\a.pdf", resolution=300)

del mxd
