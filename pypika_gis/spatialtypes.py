from pypika.terms import (
    AggregateFunction,
    Function
)


class Area(Function):
    def __init__(self, term, alias=None):
        super(Area, self).__init__('ST_Area', term, alias=alias)


class AsBinary(Function):
    def __init__(self, term, alias=None):
        super(AsBinary, self).__init__('ST_AsBinary', term, alias=alias)


class AsGeoJSON(Function):
    def __init__(self, term, alias=None):
        super(AsGeoJSON, self).__init__('ST_AsGeoJSON', term, alias=alias)


class AsMVT(Function):
    def __init__(self, term, alias=None):
        super(AsMVT, self).__init__('ST_AsMVT', term, alias=alias)


class AsText(Function):
    def __init__(self, term, alias=None):
        super(AsText, self).__init__('ST_AsText', term, alias=alias)


class Buffer(Function):
    def __init__(self, term, length, alias=None):
        super(Buffer, self).__init__('ST_Buffer', term, length, alias=alias)


class Centroid(Function):
    def __init__(self, term, alias=None):
        super(Centroid, self).__init__('ST_Centroid', term, alias=alias)


class Contains(Function):
    def __init__(self, geometryA, geometryB, alias=None):
        super(Contains, self).__init__(
            'ST_Contains', geometryA, geometryB, alias=alias)


class Difference(Function):
    def __init__(self, geometryA, geometryB, alias=None):
        super(Difference, self).__init__(
            'ST_Difference', geometryA, geometryB, alias=alias)


class Disjoint(Function):
    def __init__(self, geometryA, geometryB, alias=None):
        super(Disjoint, self).__init__(
            'ST_Disjoint', geometryA, geometryB, alias=alias)


class Distance(Function):
    def __init__(self, geometryA, geometryB, alias=None):
        super(Distance, self).__init__(
            'ST_Distance', geometryA, geometryB, alias=alias)


class Envelope(Function):
    def __init__(self, term, alias=None):
        super(Envelope, self).__init__('ST_Envelope', term, alias=alias)


class Extent(AggregateFunction):
    def __init__(self, term, alias=None):
        super(Extent, self).__init__('ST_Extent', term, alias=alias)


class GeomFromGeoJSON(Function):
    def __init__(self, geometry, alias=None):
        super(GeomFromGeoJSON, self).__init__(
            'ST_GeomFromGeoJSON', geometry, alias=alias)


class GeoHash(Function):
    def __init__(self, geometry, alias=None):
        super(GeoHash, self).__init__('ST_GeoHash', geometry, alias=alias)


class Intersection(Function):
    def __init__(self, geometryA, geometryB, alias=None):
        super(Intersection, self).__init__(
            'ST_Intersection', geometryA, geometryB, alias=alias)


class Intersects(Function):
    def __init__(self, geometryA, geometryB, alias=None):
        super(Intersects, self).__init__(
            'ST_Intersects', geometryA, geometryB, alias=alias)


class IsEmpty(Function):
    def __init__(self, term, alias=None):
        super(IsEmpty, self).__init__('ST_IsEmpty', term, alias=alias)


class IsValid(Function):
    def __init__(self, term, alias=None):
        super(IsValid, self).__init__('ST_IsValid', term, alias=alias)


class MakePoint(Function):
    def __init__(self, lng, lat, alias=None):
        super(MakePoint, self).__init__('ST_MakePoint', lng, lat, alias=alias)


class Point(Function):
    def __init__(self, lng, lat, alias=None):
        super(Point, self).__init__('ST_Point', lng, lat, alias=alias)


class Within(Function):
    def __init__(self, geometryA, geometryB, alias=None):
        super(Within, self).__init__(
            'ST_Within', geometryA, geometryB, alias=alias)


class X(Function):
    def __init__(self, term, alias=None):
        super(X, self).__init__('ST_X', term, alias=alias)


class Y(Function):
    def __init__(self, term, alias=None):
        super(Y, self).__init__('ST_Y', term, alias=alias)


class Z(Function):
    def __init__(self, term, alias=None):
        super(Z, self).__init__('ST_Z', term, alias=alias)


class SRID(Function):
    def __init__(self, geometry, epsg, alias=None):
        super(SRID, self).__init__(
            'ST_SRID', geometry, epsg, alias=alias)
