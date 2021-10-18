#
# Spatialtypes module
#
from .dialects import MSSQLSpatial, PostgreSQLSpatial

postgis = PostgreSQLSpatial.SpatialMethods()

mssql = MSSQLSpatial.SpatialMethods()
