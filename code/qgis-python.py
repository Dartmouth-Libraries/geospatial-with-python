# Replace with the path to your shapefile
#shapefile_path = "/path/to/your/shapefile.shp"
shapefile_path = "/Users/f002d69/Documents/data/vancouver/rapid-transit-lines/rapid-transit-lines.shp"
# Load the shapefile
layer = QgsVectorLayer(shapefile_path, "rapid-transit-lines", "ogr")
# Check if the layer was loaded successfully
if not layer.isValid():
    print("Layer failed to load!")
else:
    # Add the layer to the current project
    QgsProject.instance().addMapLayer(layer)
    print("Layer added successfully!")
    
def add_shapefile(path, name):
    # Load the shapefile
    layer = QgsVectorLayer(shapefile_path, name, "ogr")
    # Check if the layer was loaded successfully
    if not layer.isValid():
        print("Layer failed to load!")
    else:
        # Add the layer to the current project
        QgsProject.instance().addMapLayer(layer)
        print("Layer added successfully!")
        
the_path = "/Users/f002d69/Documents/data/vancouver/railway/railway.shp"
the_name = "railway"
add_shapefile(the_path, the_name)
