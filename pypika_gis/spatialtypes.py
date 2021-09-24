#
# Spatialtypes module
#
from .dialects import (PostgreSQLSpatial,
                       MSSQLSpatial)

postgis = PostgreSQLSpatial.SpatialMethods()

mssql = MSSQLSpatial.SpatialMethods()
