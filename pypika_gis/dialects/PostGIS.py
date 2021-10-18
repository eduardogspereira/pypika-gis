from pypika.terms import Function


class SpatialMethods(object):
    """
    Defines a PostGIS Spatial types/functions.
    """
    def Area(self, term, *args):
        return Function("ST_Area", term, *args)

    def AsBinary(self, term, *args):
        return Function("ST_AsBinary", term, *args)

    def AsGeoJSON(self, term, *args):
        return Function("ST_AsGeoJSON", term, *args)

    def AsMVT(self, term, *args):
        return Function("ST_AsMVT", term, *args)

    def AsText(self, term, *args):
        return Function("ST_AsText", term, *args)

    def Boundary(self, geom, *args):
        return Function("ST_Boundary", geom, *args)

    def Buffer(self, term, length, *args):
        return Function("ST_Buffer", term, length, *args)

    def Centroid(self, term, *args):
        return Function("ST_Centroid", term, *args)

    def ClosestPoint(self, geomA, geomB, *args):
        return Function("ST_ClosestPoint", geomA, geomB, *args)

    def Contains(self, geomA, geomB, *args):
        return Function("ST_Contains", geomA, geomB, *args)

    def ConvexHull(self, geomA, *args):
        return Function("ST_ConvexHull", geomA, *args)

    def CoveredBy(self, geomA, geomB, *args):
        return Function("ST_CoveredBy", geomA, geomB, *args)

    def Covers(self, geomA, geomB, *args):
        return Function("ST_Covers", geomA, geomB, *args)

    def Crosses(self, geomA, geomB, *args):
        return Function("ST_Crosses", geomA, geomB, *args)

    def CurveToLine(self, geom, tolerance, *args):
        return Function("ST_CurveToLine", geom, tolerance, *args)

    def DWithin(self, geomA, geomB, distance, use_spheroid=False):
        return Function("ST_DWithin", geomA, geomB, distance, use_spheroid)

    def Difference(self, geomA, geomB, *args):
        return Function("ST_Difference", geomA, geomB, *args)

    def Dimension(self, geom, *args):
        return Function("ST_Dimension", geom, *args)

    def Disjoint(self, geomA, geomB, *args):
        return Function("ST_Disjoint", geomA, geomB, *args)

    def Distance(self, geomA, geomB, *args):
        return Function("ST_Distance", geomA, geomB, *args)

    def EndPoint(self, geom, *args):
        return Function("ST_EndPoint", geom, *args)

    def Envelope(self, term, *args):
        return Function("ST_Envelope", term, *args)

    def Equals(self, geomA, geomB, *args):
        return Function("ST_Equals", geomA, geomB, *args)

    def Extent(self, term, *args):
        return Function("ST_Extent", term, *args)

    def ExteriorRing(self, geom, *args):
        return Function("ST_ExteriorRing", geom, *args)

    def GeoHash(self, term, *args):
        return Function("ST_GeoHash", term, *args)

    def GeogFromGeoJSON(self, term, *args):
        return Function("ST_GeogFromGeoJSON", term, *args)

    def GeogFromText(self, term, *args):
        return Function("ST_GeogFromText", term, *args)

    def GeogFromWKB(self, wkb, *args):
        return Function("ST_GeogFromWKB", wkb, *args)

    def GeogPoint(self, long, lat, *args):
        return Function("ST_GeogPoint", long, lat, *args)

    def GeogPointFromGeoHash(self, geohash, *args):
        return Function("ST_GeogPointFromGeoHash", geohash, *args)

    def GeomFromGeoJSON(self, term, *args):
        return Function("ST_GeomFromGeoJSON", term, *args)

    def GeometryN(self, geom, integer, *args):
        return Function("ST_GeometryN", geom, integer, *args)

    def GeometryType(self, geom, *args):
        return Function("ST_GeometryType", geom, *args)

    def InteriorRingN(self, geom, integer, *args):
        return Function("ST_InteriorRingN", geom, integer, *args)

    def Intersection(self, geomA, geomB, *args):
        return Function("ST_Intersection", geomA, geomB, *args)

    def Intersects(self, geomA, geomB, *args):
        return Function("ST_Intersects", geomA, geomB, *args)

    def IsClosed(self, geom, *args):
        return Function("ST_IsClosed", geom, *args)

    def IsCollection(self, term, *args):
        return Function("ST_IsCollection", term, *args)

    def IsEmpty(self, term, *args):
        return Function("ST_IsEmpty", term, *args)

    def IsRing(self, term, *args):
        return Function("ST_IsRing", term, *args)

    def IsSimple(self, term, *args):
        return Function("ST_IsSimple", term, *args)

    def IsValid(self, term, *args):
        return Function("ST_IsValid", term, *args)

    def Length(self, geom, *args):
        return Function("ST_Length", geom, *args)

    def MakeLine(self, *args):
        return Function("ST_MakeLine", *args)

    def MakePoint(self, long, lat, *args):
        return Function("ST_MakePoint", long, lat, *args)

    def MakePolygon(self, *args):
        return Function("ST_MakePolygon", *args)

    def NumPoints(self, geom, *args):
        return Function("ST_NumPoints", geom, *args)

    def Perimeter(self, geom, *args):
        return Function("ST_Perimeter", geom, *args)

    def Point(self, long, lat, *args):
        return Function("ST_Point", long, lat, *args)

    def PointN(self, geom, integer, *args):
        return Function("ST_PointN", geom, integer, *args)

    def PointOnSurface(self, geom, *args):
        return Function("ST_PointOnSurface", geom, *args)

    def Relate(self, geomA, geomB, *args):
        return Function("ST_Relate", geomA, geomB, *args)

    def SetSRID(self, geom, epsg, *args):
        return Function("ST_SetSRID", geom, epsg, *args)

    def StartPoint(self, geom, *args):
        return Function("ST_StartPoint", geom, *args)

    def Touches(self, geomA, geomB, *args):
        return Function("ST_Touches", geomA, geomB, *args)

    def Union(self, geomA, geomB, *args):
        return Function("ST_Union", geomA, geomB, *args)

    def Within(self, geomA, geomB, *args):
        return Function("ST_Within", geomA, geomB, *args)

    def X(self, term, *args):
        return Function("ST_X", term, *args)

    def Y(self, term, *args):
        return Function("ST_Y", term, *args)

    def Z(self, term, *args):
        return Function("ST_Z", term, *args)
