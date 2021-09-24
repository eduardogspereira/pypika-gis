#
# Dialects module
#
from pypika.terms import Function


class SpatialMethods(object):
    """
    Defines an MS-SQL (a.k.a. SQL Server) Spatial types/functions
    """

    def Area(self, term, *args):
        return Function("STArea", term, *args)

    def AsBinary(self, term, *args):
        return Function("STAsBinary", term, *args)

    def AsGeoJSON(self, term, *args):
        raise NotImplementedError('MSSQL has no STAsGeoJSON method')

    def AsMVT(self, term, *args):
        raise NotImplementedError('MSSQL has no STAsMVT method')

    def AsText(self, term, *args):
        return Function("STAsText", term, *args)

    def Boundary(self, term, *args):
        return Function("STBoundary", term, *args)

    def Buffer(self, term, length, *args):
        return Function("STBuffer", term, length, *args)

    def Centroid(self, term, *args):
        return Function("STCentroid", term, *args)
    
    def Contains(self, geomA, geomB, *args):
        return Function("STContains", geomA, geomB, *args)

    def ConvexHull(self, term, *args):
        return Function("STConvexHull", term, *args)
    
    def Crosses(self, geom, *args):
        return Function("STCrosses", geom, *args)

    def CurveN(self, curve_index, *args):
        return Function("STCurveN", curve_index, *args)
    
    def CurveToLine(self, term, *args):
        return Function("STCurveToLine", term, *args)

    def Difference(self, geom, *args):
        return Function("STDifference", geom, *args)

    def Dimension(self, term, *args):
        return Function("STDimension", term, *args)

    def Disjoint(self, geom, *args):
        return Function("STDisjoint", geom, *args)

    def Distance(self, geom, *args):
        return Function("STDistance", geom, *args)

    def EndPoint(self, term, *args):
        return Function("STEndpoint", term, *args)

    def Envelope(self, term, *args):
        return Function("STEnvelope", term, *args)

    def Equals(self, geom, *args):
        return Function("STEquals", geom, *args)

    def ExteriorRing(self, term, *args):
        return Function("STExteriorRing", term, *args)

    def GeogFromGeoJSON(self, term, *args):
        return Function("STGeogFromGeoJSON", term, *args)

    def GeogFromText(self, term, *args):
        return Function("STGeogFromText", term, *args)

    def GeogFromWKB(self, wkb, *args):
        return Function("STGeogFromWKB", wkb, *args)

    def GeogPoint(self, long, lat, *args):
        return Function("STGeogPoint", long, lat, *args)

    def GeogPointFromGeoHash(self, geohash, *args):
        return Function("STGeogPointFromGeoHash", geohash, *args)

    def GeomFromGeoJSON(self, term, *args):
        return Function("STGeomFromGeoJSON", term, *args)

    def Length(self, geom, *args):
        return Function("STLength", geom, *args)

    def Intersection(self, geomA, geomB, *args):
        return Function("STIntersection", geomA, geomB, *args)

    def Intersects(self, geomA, geomB, *args):
        return Function("STIntersects", geomA, geomB, *args)

    def IsCollection(self, term, *args):
        return Function("STIsCollection", term, *args)

    def IsEmpty(self, term, *args):
        return Function("STIsEmpty", term, *args)

    def IsValid(self, term, *args):
        return Function("STIsValid", term, *args)

    def MakeLine(self, *args):
        return Function("STMakeLine", *args)

    def MakePoint(self, long, lat, *args):
        return Function("STMakePoint", long, lat, *args)

    def MakePolygon(self, *args):
        return Function("STMakePolygon", *args)

    def NumPoints(self, geom, *args):
        return Function("STNumPoints", geom, *args)

    def Perimeter(self, geom, *args):
        return Function("STPerimeter", geom, *args)

    def Point(self, long, lat, *args):
        return Function("STPoint", long, lat, *args)

    def SetSRID(self, geom, epsg, *args):
        return Function("STSetSRID", geom, epsg, *args)

    def Touches(self, geomA, geomB, *args):
        return Function("STTouches", geomA, geomB, *args)

    def Union(self, geomA, geomB, *args):
        return Function("STUnion", geomA, geomB, *args)

    def Within(self, geomA, geomB, *args):
        return Function("STWithin", geomA, geomB, *args)

    def X(self, term, *args):
        return Function("STX", term, *args)

    def Y(self, term, *args):
        return Function("STY", term, *args)

    def Z(self, term, *args):
        return Function("STZ", term, *args)
