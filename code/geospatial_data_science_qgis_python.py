# QGIS Python script - run at the Python Console, or the Python script window
# 
# 
# import the processing library
import processing
from qgis.core import QgsField

# use QGIS processing.run to run native tool 'fixgeometries' and 'buffer'
processing.run("native:fixgeometries", 
{'INPUT':'/Users/netid/Downloads/censustowns_geomfix.shp',
'METHOD':0,'OUTPUT':'/Users/netid/Downloads/censustowns_geomfix_temp.shp'})

# Create a buffer of 1 mile using points1.shp as input
processing.run("native:buffer",
               {'INPUT':'/Users/netid/Downloads/eee_towns_intersect.shp',
               'DISTANCE':6336, 'SEGMENTS':5,'MITER_JOIN':True, 
               'END_CAP_STYLE':0, 'OUTPUT':'/Users/netid/Downloads/eee_buffer_temp.shp'})
