from pypika import Table

from pypika_gis.spatialtypes import mssql as st

table = Table('table')


def test_Area():
    query = st.Area(table.geom)
    assert (str(query)) == "geom.STArea()"


def test_AsBinary():
    query = st.AsBinary(table.geom)
    assert (str(query)) == "geom.STAsBinary()"


def test_AsText():
    query = st.AsText(table.geom)
    assert (str(query)) == "geom.STAsText()"


def test_Boundary():
    query = st.Boundary(table.geom)
    assert (str(query)) == "geom.STBoundary()"


def test_Buffer():
    query = st.Buffer(table.geom, 100)
    assert (str(query)) == "geom.STBuffer(100)"


def test_Centroid():
    query = st.Centroid(table.geom)
    assert (str(query)) == "geom.STCentroid()"


def test_Contains():
    query = st.Contains(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STContains("geomB")'


def test_ConvexHull():
    query = st.ConvexHull(table.geom)
    assert (str(query)) == "geom.STConvexHull()"


def test_Crosses():
    query = st.Crosses(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STCrosses("geomB")'


def test_CurveN():
    query = st.CurveN(table.geom, 10)
    assert (str(query)) == "geom.STCurveN(10)"


def test_CurveToLine():
    query = st.CurveToLine(table.geom)
    assert (str(query)) == "geom.STCurveToLine()"


def test_Difference():
    query = st.Difference(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STDifference("geomB")'


def test_Dimension():
    query = st.Dimension(table.geom)
    assert (str(query)) == "geom.STDimension()"


def test_Disjoint():
    query = st.Disjoint(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STDisjoint("geomB")'


def test_Distance():
    query = st.Distance(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STDistance("geomB")'


def test_EndPoint():
    query = st.EndPoint(table.geom)
    assert (str(query)) == "geom.STEndpoint()"


def test_Envelope():
    query = st.Envelope(table.geom)
    assert (str(query)) == "geom.STEnvelope()"


def test_Equals():
    query = st.Equals(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STEquals("geomB")'


def test_ExteriorRing():
    query = st.ExteriorRing(table.geom)
    assert (str(query)) == "geom.STExteriorRing()"


def test_GeomFromText():
    query = st.GeomFromText("Polygon((0 0, 0 2, 2 2, 2 0, 0 0))", 1234)
    assert (
        str(query)
    ) == "geometry::STGeomFromText('Polygon((0 0, 0 2, 2 2, 2 0, 0 0))',1234)"


def test_GeomFromWKB():
    query = st.GeomFromWKB("{}", 1234)
    assert (str(query)) == "geometry::STGeomFromWKB('{}',1234)"


def test_GeometryN():
    query = st.GeometryN(table.geom, 10)
    assert (str(query)) == "geom.STGeometryN(10)"


def test_GeometryType():
    query = st.GeometryType(table.geom)
    assert (str(query)) == "geom.STGeometryType()"


def test_InteriorRingN():
    query = st.InteriorRingN(table.geom, 10)
    assert (str(query)) == "geom.STInteriorRingN(10)"


def test_Intersection():
    query = st.Intersection(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STIntersection("geomB")'


def test_Intersects():
    query = st.Intersects(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STIntersects("geomB")'


def test_IsClosed():
    query = st.IsClosed(table.geom)
    assert (str(query)) == "geom.STIsClosed()"


def test_IsEmpty():
    query = st.IsEmpty(table.geom)
    assert (str(query)) == "geom.STIsEmpty()"


def test_IsRing():
    query = st.IsRing(table.geom)
    assert (str(query)) == "geom.STIsRing()"


def test_IsSimple():
    query = st.IsSimple(table.geom)
    assert (str(query)) == "geom.STIsSimple()"


def test_IsValid():
    query = st.IsValid(table.geom)
    assert (str(query)) == "geom.STIsValid()"


def test_Length():
    query = st.Length(table.geom)
    assert (str(query)) == "geom.STLength()"


def test_NumCurves():
    query = st.NumCurves(table.geom)
    assert (str(query)) == "geom.STNumCurves()"


def test_NumGeometries():
    query = st.NumGeometries(table.geom)
    assert (str(query)) == "geom.STNumGeometries()"


def test_NumInteriorRing():
    query = st.NumInteriorRing(table.geom)
    assert (str(query)) == "geom.STNumInteriorRing()"


def test_NumPoints():
    query = st.NumPoints(table.geom)
    assert (str(query)) == "geom.STNumPoints()"


def test_Overlaps():
    query = st.Overlaps(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STOverlaps("geomB")'


def test_Point():
    query = st.Point(10, 20, 1234)
    assert (str(query)) == "geography::Point(10,20,1234)"


def test_PointN():
    query = st.PointN(table.geom, 10)
    assert (str(query)) == "geom.STPointN(10)"


def test_PointOnSurface():
    query = st.PointOnSurface(table.geom)
    assert (str(query)) == "geom.STPointOnSurface()"


def test_Relate():
    query = st.Relate(table.geomA, table.geomB, 'FF*FF****')
    assert (str(query)) == 'geomA.STRelate("geomB",\'FF*FF****\')'


def test_StartPoint():
    query = st.StartPoint(table.geom)
    assert (str(query)) == "geom.STStartPoint()"


def test_SymDifference():
    query = st.SymDifference(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STSymDifference("geomB")'


def test_Touches():
    query = st.Touches(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STTouches("geomB")'


def test_Union():
    query = st.Union(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STUnion("geomB")'


def test_Within():
    query = st.Within(table.geomA, table.geomB)
    assert (str(query)) == 'geomA.STWithin("geomB")'


def test_X():
    query = st.X(table.geom)
    assert (str(query)) == '"geom.STX"'


def test_Y():
    query = st.Y(table.geom)
    assert (str(query)) == '"geom.STY"'
