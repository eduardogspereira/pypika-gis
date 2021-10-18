from pypika import Field
from pypika.terms import Function


class SpatialMethods(object):
    """
    Defines an MS-SQL (a.k.a. SQL Server) Spatial types/functions
    """
    def Area(self, geom, *args):
        return Function(f"{geom.get_sql()}.STArea", *args)

    def AsBinary(self, geom, *args):
        return Function(f"{geom.get_sql()}.STAsBinary", *args)

    def AsText(self, geom, *args):
        return Function(f"{geom.get_sql()}.STAsText", *args)

    def Boundary(self, geom, *args):
        return Function(f"{geom.get_sql()}.STBoundary", *args)

    def Buffer(self, geom, length, *args):
        return Function(f"{geom.get_sql()}.STBuffer", length, *args)

    def Centroid(self, geom, *args):
        return Function(f"{geom.get_sql()}.STCentroid", *args)

    def Contains(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STContains", geomB, *args)

    def ConvexHull(self, geom, *args):
        return Function(f"{geom.get_sql()}.STConvexHull", *args)

    def Crosses(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STCrosses", geomB, *args)

    def CurveN(self, term, curve_index, *args):
        return Function(f"{term.get_sql()}.STCurveN", curve_index, *args)

    def CurveToLine(self, term, *args):
        return Function(f"{term.get_sql()}.STCurveToLine", *args)

    def Difference(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STDifference", geomB, *args)

    def Dimension(self, geom, *args):
        return Function(f"{geom.get_sql()}.STDimension", *args)

    def Disjoint(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STDisjoint", geomB, *args)

    def Distance(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STDistance", geomB, *args)

    def EndPoint(self, geom, *args):
        return Function(f"{geom.get_sql()}.STEndpoint", *args)

    def Envelope(self, geom, *args):
        return Function(f"{geom.get_sql()}.STEnvelope", *args)

    def Equals(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STEquals", geomB, *args)

    def ExteriorRing(self, geom, *args):
        return Function(f"{geom.get_sql()}.STExteriorRing", *args)

    def GeomFromText(self, text, srid, *args):
        return Function("geometry::STGeomFromText", text, srid, *args)

    def GeomFromWKB(self, wkb, srid, *args):
        return Function("geometry::STGeomFromWKB", wkb, srid, *args)

    def GeometryN(self, geom, value, *args):
        return Function(f"{geom.get_sql()}.STGeometryN", value, *args)

    def GeometryType(self, geom, *args):
        return Function(f"{geom.get_sql()}.STGeometryType", *args)

    def InteriorRingN(self, geom, value, *args):
        return Function(f"{geom.get_sql()}.STInteriorRingN", value, *args)

    def Intersection(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STIntersection", geomB, *args)

    def Intersects(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STIntersects", geomB, *args)

    def IsClosed(self, geom, *args):
        return Function(f"{geom.get_sql()}.STIsClosed", *args)

    def IsEmpty(self, geom, *args):
        return Function(f"{geom.get_sql()}.STIsEmpty", *args)

    def IsRing(self, geom, *args):
        return Function(f"{geom.get_sql()}.STIsRing", *args)

    def IsSimple(self, geom, *args):
        return Function(f"{geom.get_sql()}.STIsSimple", *args)

    def IsValid(self, geom, *args):
        return Function(f"{geom.get_sql()}.STIsValid", *args)

    def Length(self, geom, *args):
        return Function(f"{geom.get_sql()}.STLength", *args)

    def NumCurves(self, geom, *args):
        return Function(f"{geom.get_sql()}.STNumCurves", *args)

    def NumGeometries(self, geom, *args):
        return Function(f"{geom.get_sql()}.STNumGeometries", *args)

    def NumInteriorRing(self, geom, *args):
        return Function(f"{geom.get_sql()}.STNumInteriorRing", *args)

    def NumPoints(self, geom, *args):
        return Function(f"{geom.get_sql()}.STNumPoints", *args)

    def Overlaps(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STOverlaps", geomB, *args)

    def Point(self, x, y, srid):
        return Function(f"geography::Point", x, y, srid)

    def PointN(self, geom, expression, *args):
        return Function(f"{geom.get_sql()}.STPointN", expression, *args)

    def PointOnSurface(self, geom, *args):
        return Function(f"{geom.get_sql()}.STPointOnSurface", *args)

    def Relate(self, geomA, geomB, pattern, *args):
        return Function(f"{geomA.get_sql()}.STRelate", geomB, pattern, *args)

    def Srid(self, geom, alias='srid'):
        if isinstance(geom, Field):
            return Field(geom.name + '.STSrid', table=geom.table, alias=alias)
        else:
            raise ValueError('Input geom must be Field.')

    def StartPoint(self, geom, *args):
        return Function(f"{geom.get_sql()}.STStartPoint", *args)

    def SymDifference(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STSymDifference", geomB, *args)

    def Touches(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STTouches", geomB, *args)

    def Union(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STUnion", geomB, *args)

    def Within(self, geomA, geomB, *args):
        return Function(f"{geomA.get_sql()}.STWithin", geomB, *args)

    def X(self, geom, alias='x'):
        if isinstance(geom, Field):
            return Field(geom.name + '.STX', table=geom.table, alias=alias)
        else:
            raise ValueError('Input geom must be Field.')

    def Y(self, geom, alias='y'):
        if isinstance(geom, Field):
            return Field(geom.name + '.STY', table=geom.table, alias=alias)
        else:
            raise ValueError('Input geom must be Field.')
