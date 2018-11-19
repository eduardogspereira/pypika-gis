import spatialtypes as st


def test_Area():
    query = st.Area("geom")
    assert(str(query)) == "ST_Area('geom')"


def test_AsBinary():
    query = st.AsBinary("geom")
    assert(str(query)) == "ST_AsBinary('geom')"


def test_AsGeoJSON():
    query = st.AsGeoJSON("geom")
    assert(str(query)) == "ST_AsGeoJSON('geom')"


def test_AsMVT():
    query = st.AsMVT("geom")
    assert(str(query)) == "ST_AsMVT('geom')"


def test_AsText():
    query = st.AsText("geom")
    assert(str(query)) == "ST_AsText('geom')"


def test_Buffer():
    query = st.Buffer("geom", 100)
    assert(str(query)) == "ST_Buffer('geom',100)"


def test_Centroid():
    query = st.Centroid("geom")
    assert(str(query)) == "ST_Centroid('geom')"


def test_Contains():
    query = st.Contains("geomA", "geomB")
    assert(str(query)) == "ST_Contains('geomA','geomB')"


def test_Difference():
    query = st.Difference("geomA", "geomB")
    assert(str(query)) == "ST_Difference('geomA','geomB')"


def test_Disjoint():
    query = st.Disjoint("geomA", "geomB")
    assert(str(query)) == "ST_Disjoint('geomA','geomB')"


def test_Distance():
    query = st.Distance("geomA", "geomB")
    assert(str(query)) == "ST_Distance('geomA','geomB')"


def test_Envelope():
    query = st.Envelope("geom")
    assert(str(query)) == "ST_Envelope('geom')"


def test_Extent():
    query = st.Extent("geom")
    assert(str(query)) == "ST_Extent('geom')"


def test_GeomFromGeoJSON():
    query = st.GeomFromGeoJSON({"geometry": {}})
    assert(str(query)) == "ST_GeomFromGeoJSON({'geometry': {}})"


def test_GeoHash():
    query = st.GeoHash("geom")
    assert(str(query)) == "ST_GeoHash('geom')"


def test_Intersection():
    query = st.Intersection("geomA", "geomB")
    assert(str(query)) == "ST_Intersection('geomA','geomB')"


def test_Intersects():
    query = st.Intersects("geomA", "geomB")
    assert(str(query)) == "ST_Intersects('geomA','geomB')"


def test_IsEmpty():
    query = st.IsEmpty("geom")
    assert(str(query)) == "ST_IsEmpty('geom')"


def test_IsValid():
    query = st.IsValid("geom")
    assert(str(query)) == "ST_IsValid('geom')"


def test_MakePoint():
    query = st.MakePoint(10, 20)
    assert(str(query)) == "ST_MakePoint(10,20)"


def test_Point():
    query = st.Point(10, 20)
    assert(str(query)) == "ST_Point(10,20)"


def test_SetSRID():
    query = st.SetSRID("geom", 4326)
    assert(str(query)) == "ST_SetSRID('geom',4326)"


def test_Within():
    query = st.Within("geomA", "geomB")
    assert(str(query)) == "ST_Within('geomA','geomB')"


def test_X():
    query = st.X("geom")
    assert(str(query)) == "ST_X('geom')"


def test_Y():
    query = st.Y("geom")
    assert(str(query)) == "ST_Y('geom')"


def test_Z():
    query = st.Z("geom")
    assert(str(query)) == "ST_Z('geom')"
