from pypika import Table

from pypika_gis.spatialtypes import postgis as st

table = Table('table')


def test_Area():
    query = st.Area(table.geom)
    assert (str(query)) == 'ST_Area("geom")'


def test_AsBinary():
    query = st.AsBinary(table.geom)
    assert (str(query)) == 'ST_AsBinary("geom")'


def test_AsGeoJSON():
    query = st.AsGeoJSON(table.geom)
    assert (str(query)) == 'ST_AsGeoJSON("geom")'


def test_AsMVT():
    query = st.AsMVT(table.geom)
    assert (str(query)) == 'ST_AsMVT("geom")'


def test_AsText():
    query = st.AsText(table.geom)
    assert (str(query)) == 'ST_AsText("geom")'


def test_Boundary():
    query = st.Boundary(table.geom)
    assert (str(query)) == 'ST_Boundary("geom")'


def test_Buffer():
    query = st.Buffer(table.geom, 100)
    assert (str(query)) == 'ST_Buffer("geom",100)'


def test_Centroid():
    query = st.Centroid(table.geom)
    assert (str(query)) == 'ST_Centroid("geom")'


def test_ClosestPoint():
    query = st.ClosestPoint(table.geomA, table.geomB)
    assert (str(query)) == 'ST_ClosestPoint("geomA","geomB")'


def test_Contains():
    query = st.Contains(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Contains("geomA","geomB")'


def test_ConvexHull():
    query = st.ConvexHull(table.geom)
    assert (str(query)) == 'ST_ConvexHull("geom")'


def test_CoveredBy():
    query = st.CoveredBy(table.geomA, table.geomB)
    assert (str(query)) == 'ST_CoveredBy("geomA","geomB")'


def test_Covers():
    query = st.Covers(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Covers("geomA","geomB")'


def test_Crosses():
    query = st.Crosses(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Crosses("geomA","geomB")'


def test_CurveToLine():
    query = st.CurveToLine(table.geom, 10)
    assert (str(query)) == 'ST_CurveToLine("geom",10)'


def test_DWithin():
    query = st.DWithin(table.geomA, table.geomB, 10)
    assert (str(query)) == 'ST_DWithin("geomA","geomB",10,false)'


def test_Difference():
    query = st.Difference(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Difference("geomA","geomB")'


def test_Dimension():
    query = st.Dimension(table.geom)
    assert (str(query)) == 'ST_Dimension("geom")'


def test_Disjoint():
    query = st.Disjoint(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Disjoint("geomA","geomB")'


def test_Distance():
    query = st.Distance(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Distance("geomA","geomB")'


def test_EndPoint():
    query = st.EndPoint(table.geom)
    assert (str(query)) == 'ST_EndPoint("geom")'


def test_Envelope():
    query = st.Envelope(table.geom)
    assert (str(query)) == 'ST_Envelope("geom")'


def test_Equals():
    query = st.Equals(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Equals("geomA","geomB")'


def test_Extent():
    query = st.Extent(table.geom)
    assert (str(query)) == 'ST_Extent("geom")'


def test_ExteriorRing():
    query = st.ExteriorRing(table.geom)
    assert (str(query)) == 'ST_ExteriorRing("geom")'


def test_GeoHash():
    query = st.GeoHash(table.geom)
    assert (str(query)) == 'ST_GeoHash("geom")'


def test_GeogFromGeoJSON():
    query = st.GeogFromGeoJSON("{}")
    assert (str(query)) == "ST_GeogFromGeoJSON('{}')"


def test_GeogFromText():
    query = st.GeogFromText("Polygon((0 0, 0 2, 2 2, 2 0, 0 0))")
    assert (
        str(query)) == "ST_GeogFromText('Polygon((0 0, 0 2, 2 2, 2 0, 0 0))')"


def test_GeogFromWKB():
    query = st.GeogFromWKB("{}")
    assert (str(query)) == "ST_GeogFromWKB('{}')"


def test_GeogPoint():
    query = st.GeogPoint(10, 10)
    assert (str(query)) == "ST_GeogPoint(10,10)"


def test_GeogPointFromGeoHash():
    query = st.GeogPointFromGeoHash("6GZ765HX0128")
    assert (str(query)) == "ST_GeogPointFromGeoHash('6GZ765HX0128')"


def test_GeomFromGeoJSON():
    query = st.GeomFromGeoJSON({"geometry": {}})
    assert (str(query)) == "ST_GeomFromGeoJSON({'geometry': {}})"


def test_GeometryN():
    query = st.GeometryN(table.geom, 1)
    assert (str(query)) == 'ST_GeometryN("geom",1)'


def test_GeometryType():
    query = st.GeometryType(table.geom, 1)
    assert (str(query)) == 'ST_GeometryType("geom",1)'


def test_InteriorRingN():
    query = st.InteriorRingN(table.geom, 0)
    assert (str(query)) == 'ST_InteriorRingN("geom",0)'


def test_Intersection():
    query = st.Intersection(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Intersection("geomA","geomB")'


def test_Intersects():
    query = st.Intersects(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Intersects("geomA","geomB")'


def test_IsClosed():
    query = st.IsClosed(table.geom)
    assert (str(query)) == 'ST_IsClosed("geom")'


def test_IsCollection():
    query = st.IsCollection(table.geom)
    assert (str(query)) == 'ST_IsCollection("geom")'


def test_IsEmpty():
    query = st.IsEmpty(table.geom)
    assert (str(query)) == 'ST_IsEmpty("geom")'


def test_IsRing():
    query = st.IsRing(table.geom)
    assert (str(query)) == 'ST_IsRing("geom")'


def test_IsSimple():
    query = st.IsSimple(table.geom)
    assert (str(query)) == 'ST_IsSimple("geom")'


def test_IsValid():
    query = st.IsValid(table.geom)
    assert (str(query)) == 'ST_IsValid("geom")'


def test_Length():
    query = st.Length(table.geom)
    assert (str(query)) == 'ST_Length("geom")'


def test_MakeLine():
    query = st.MakeLine(st.MakePoint(10, 10), table.geom)
    assert (str(query)) == 'ST_MakeLine(ST_MakePoint(10,10),"geom")'


def test_MakePoint():
    query = st.MakePoint(10, 20)
    assert (str(query)) == "ST_MakePoint(10,20)"


def test_MakePolygon():
    query = st.MakePolygon(
        "LINESTRING(75.15 29.53 1,77 29 1,77.6 29.5 1, 75.15 29.53 1)")
    assert (
        (str(query)) ==
        "ST_MakePolygon('LINESTRING(75.15 29.53 1,77 29 1,77.6 29.5 1, 75.15 29.53 1)')"
    )


def test_NumPoints():
    query = st.NumPoints(table.geom)
    assert (str(query)) == 'ST_NumPoints("geom")'


def test_Perimeter():
    query = st.Perimeter(table.geom)
    assert (str(query)) == 'ST_Perimeter("geom")'


def test_Point():
    query = st.Point(10, 20)
    assert (str(query)) == "ST_Point(10,20)"


def test_PointN():
    query = st.PointN(table.geom, 2)
    assert (str(query)) == 'ST_PointN("geom",2)'


def test_PointOnSurface():
    query = st.PointOnSurface(table.geom)
    assert (str(query)) == 'ST_PointOnSurface("geom")'


def test_Relate():
    query = st.Relate(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Relate("geomA","geomB")'


def test_SetSRID():
    query = st.SetSRID(table.geom, 4326)
    assert (str(query)) == 'ST_SetSRID("geom",4326)'


def test_StartPoint():
    query = st.StartPoint(table.geom)
    assert (str(query)) == 'ST_StartPoint("geom")'


def test_Touches():
    query = st.Touches(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Touches("geomA","geomB")'


def test_Union():
    query = st.Union(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Union("geomA","geomB")'


def test_Within():
    query = st.Within(table.geomA, table.geomB)
    assert (str(query)) == 'ST_Within("geomA","geomB")'


def test_X():
    query = st.X(table.geom)
    assert (str(query)) == 'ST_X("geom")'


def test_Y():
    query = st.Y(table.geom)
    assert (str(query)) == 'ST_Y("geom")'


def test_Z():
    query = st.Z(table.geom)
    assert (str(query)) == 'ST_Z("geom")'
