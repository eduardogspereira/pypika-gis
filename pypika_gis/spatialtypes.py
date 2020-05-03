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


def Buffer(term, length, *args):
    return Function("ST_Buffer", term, length, *args)


def Centroid(term, *args):
    return Function("ST_Centroid", term, *args)


def Contains(geomA, geomB, *args):
    return Function("ST_Contains", geomA, geomB, *args)


def Difference(geomA, geomB, *args):
    return Function("ST_Difference", geomA, geomB, *args)


def Disjoint(geomA, geomB, *args):
    return Function("ST_Disjoint", geomA, geomB, *args)


def Distance(geomA, geomB, *args):
    return Function("ST_Distance", geomA, geomB, *args)


def Envelope(term, *args):
    return Function("ST_Envelope", term, *args)


def Extent(term, *args):
    return Function("ST_Extent", term, *args)


def GeomFromGeoJSON(term, *args):
    return Function("ST_GeomFromGeoJSON", term, *args)


def GeogPoint(long, lat, *args):
    return Function("ST_GeogPoint", long, lat, *args)


def GeoHash(term, *args):
    return Function("ST_GeoHash", term, *args)


def Intersection(geomA, geomB, *args):
    return Function("ST_Intersection", geomA, geomB, *args)


def Intersects(geomA, geomB, *args):
    return Function("ST_Intersects", geomA, geomB, *args)


def IsEmpty(term, *args):
    return Function("ST_IsEmpty", term, *args)


def IsValid(term, *args):
    return Function("ST_IsValid", term, *args)


def MakePoint(long, lat, *args):
    return Function("ST_MakePoint", long, lat, *args)


def Point(long, lat, *args):
    return Function("ST_Point", long, lat, *args)


def SetSRID(geom, epsg, *args):
    return Function("ST_SetSRID", geom, epsg, *args)


def Within(geomA, geomB, *args):
    return Function("ST_Within", geomA, geomB, *args)


def X(term, *args):
    return Function("ST_X", term, *args)


def Y(term, *args):
    return Function("ST_Y", term, *args)


def Z(term, *args):
    return Function("ST_Z", term, *args)
