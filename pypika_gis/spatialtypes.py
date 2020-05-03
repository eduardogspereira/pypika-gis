from pypika.terms import Function


def Area(term):
    return Function("ST_Area", term)


def AsBinary(term):
    return Function("ST_AsBinary", term)


def AsGeoJSON(term):
    return Function("ST_AsGeoJSON", term)


def AsMVT(term):
    return Function("ST_AsMVT", term)


def AsText(term):
    return Function("ST_AsText", term)


def Buffer(term, length):
    return Function("ST_Buffer", term, length)


def Centroid(term):
    return Function("ST_Centroid", term)


def Contains(geomA, geomB):
    return Function("ST_Contains", geomA, geomB)


def Difference(geomA, geomB):
    return Function("ST_Difference", geomA, geomB)


def Disjoint(geomA, geomB):
    return Function("ST_Disjoint", geomA, geomB)


def Distance(geomA, geomB):
    return Function("ST_Distance", geomA, geomB)


def Envelope(term):
    return Function("ST_Envelope", term)


def Extent(term):
    return Function("ST_Extent", term)


def GeomFromGeoJSON(term):
    return Function("ST_GeomFromGeoJSON", term)


def GeogPoint(long, lat):
    return Function("ST_GeogPoint", long, lat)


def GeoHash(term):
    return Function("ST_GeoHash", term)


def Intersection(geomA, geomB):
    return Function("ST_Intersection", geomA, geomB)


def Intersects(geomA, geomB):
    return Function("ST_Intersects", geomA, geomB)


def IsEmpty(term):
    return Function("ST_IsEmpty", term)


def IsValid(term):
    return Function("ST_IsValid", term)


def MakePoint(long, lat):
    return Function("ST_MakePoint", long, lat)


def Point(long, lat):
    return Function("ST_Point", long, lat)


def SetSRID(geom, epsg):
    return Function("ST_SetSRID", geom, epsg)


def Within(geomA, geomB):
    return Function("ST_Within", geomA, geomB)


def X(term):
    return Function("ST_X", term)


def Y(term):
    return Function("ST_Y", term)


def Z(term):
    return Function("ST_Z", term)
