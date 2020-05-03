from pypika.terms import Function


def Area(term, *args):
    return Function("ST_Area", term, *args)


def AsBinary(term, *args):
    return Function("ST_AsBinary", term, *args)


def AsGeoJSON(term, *args):
    return Function("ST_AsGeoJSON", term, *args)


def AsMVT(term, *args):
    return Function("ST_AsMVT", term, *args)


def AsText(term, *args):
    return Function("ST_AsText", term, *args)


def Boundary(geom, *args):
    return Function("ST_Boundary", geom, *args)


def Buffer(term, length, *args):
    return Function("ST_Buffer", term, length, *args)


def Centroid(term, *args):
    return Function("ST_Centroid", term, *args)


def Contains(geomA, geomB, *args):
    return Function("ST_Contains", geomA, geomB, *args)


def ClosestPoint(geomA, geomB, *args):
    return Function("ST_ClosestPoint", geomA, geomB, *args)


def CoveredBy(geomA, geomB, *args):
    return Function("ST_CoveredBy", geomA, geomB, *args)


def Covers(geomA, geomB, *args):
    return Function("ST_Covers", geomA, geomB, *args)


def Difference(geomA, geomB, *args):
    return Function("ST_Difference", geomA, geomB, *args)


def Dimension(geom, *args):
    return Function("ST_Dimension", geom, *args)


def Disjoint(geomA, geomB, *args):
    return Function("ST_Disjoint", geomA, geomB, *args)


def Distance(geomA, geomB, *args):
    return Function("ST_Distance", geomA, geomB, *args)


def DWithin(geomA, geomB, distance, use_spheroid=False):
    return Function("ST_DWithin", geomA, geomB, distance, use_spheroid)


def Equals(geomA, geomB, *args):
    return Function("ST_Equals", geomA, geomB, *args)


def Envelope(term, *args):
    return Function("ST_Envelope", term, *args)


def Extent(term, *args):
    return Function("ST_Extent", term, *args)


def GeoHash(term, *args):
    return Function("ST_GeoHash", term, *args)


def GeogFromGeoJSON(term, *args):
    return Function("ST_GeogFromGeoJSON", term, *args)


def GeogFromText(term, *args):
    return Function("ST_GeogFromText", term, *args)


def GeogFromWKB(wkb, *args):
    return Function("ST_GeogFromWKB", wkb, *args)


def GeogPoint(long, lat, *args):
    return Function("ST_GeogPoint", long, lat, *args)


def GeogPointFromGeoHash(geohash, *args):
    return Function("ST_GeogPointFromGeoHash", geohash, *args)


def GeomFromGeoJSON(term, *args):
    return Function("ST_GeomFromGeoJSON", term, *args)


def Length(geom, *args):
    return Function("ST_Length", geom, *args)


def Intersection(geomA, geomB, *args):
    return Function("ST_Intersection", geomA, geomB, *args)


def Intersects(geomA, geomB, *args):
    return Function("ST_Intersects", geomA, geomB, *args)


def IsCollection(term, *args):
    return Function("ST_IsCollection", term, *args)


def IsEmpty(term, *args):
    return Function("ST_IsEmpty", term, *args)


def IsValid(term, *args):
    return Function("ST_IsValid", term, *args)


def MakeLine(*args):
    return Function("ST_MakeLine", *args)


def MakePoint(long, lat, *args):
    return Function("ST_MakePoint", long, lat, *args)


def MakePolygon(*args):
    return Function("ST_MakePolygon", *args)


def NumPoints(geom, *args):
    return Function("ST_NumPoints", geom, *args)


def Perimeter(geom, *args):
    return Function("ST_Perimeter", geom, *args)


def Point(long, lat, *args):
    return Function("ST_Point", long, lat, *args)


def SetSRID(geom, epsg, *args):
    return Function("ST_SetSRID", geom, epsg, *args)


def Touches(geomA, geomB, *args):
    return Function("ST_Touches", geomA, geomB, *args)


def Union(geomA, geomB, *args):
    return Function("ST_Union", geomA, geomB, *args)


def Within(geomA, geomB, *args):
    return Function("ST_Within", geomA, geomB, *args)


def X(term, *args):
    return Function("ST_X", term, *args)


def Y(term, *args):
    return Function("ST_Y", term, *args)


def Z(term, *args):
    return Function("ST_Z", term, *args)
