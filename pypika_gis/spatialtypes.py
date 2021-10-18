from .dialects import MSSQLSpatial, PostGIS

postgis = PostGIS.SpatialMethods()
mssql = MSSQLSpatial.SpatialMethods()
