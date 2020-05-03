# pypika-gis

SpatialTypes functions for extend [PyPika](https://github.com/kayak/pypika) with GIS.

## Install

```bash
pip install pypika-gis
```

## Example

```python
from pypika import Query
from pypika_gis import spatialtypes as st

query = Query.from_('field').select('id', st.AsGeoJSON('geom'))
print(str(query))
# SELECT "id",ST_AsGeoJSON('geom') FROM "field"

query = Query.from_('crop').select('id').where(st.Intersects('geom', st.SetSRID(st.MakePoint(10, 5), 4326)))
print(str(query))
# SELECT "id" FROM "crop" WHERE ST_Intersects('geom',ST_SRID(ST_MakePoint(10,5),4326))
```

## Available functions

- Area(ST_Area)
- AsBinary(ST_AsBinary)
- AsGeoJSON(ST_AsGeoJSON)
- AsMVT(ST_AsMVT)
- AsText(ST_AsText)
- Boundary(ST_Boundary)
- Buffer(ST_Buffer)
- Centroid(ST_Centroid)
- ClosestPoint(ST_ClosestPoint)
- Contains(ST_Contains)
- CoveredBy(ST_CoveredBy)
- Covers(ST_Covers)
- Difference(ST_Difference)
- Dimension(ST_Dimension)
- Disjoint(ST_Disjoint)
- Distance(ST_Distance)
- DWithin(ST_DWithin)
- Equals(ST_Equals)
- Envelope(ST_Envelope)
- Extent(ST_Extent)
- GeoHash(ST_GeoHash)
- GeogFromGeoJSON(ST_GeogFromGeoJSON)
- GeogFromText(ST_GeogFromText)
- GeogFromWKB(ST_GeogFromWKB)
- GeogPoint(ST_GeogPoint)
- GeogPointFromGeoHash(ST_GeogPointFromGeoHash)
- GeomFromGeoJSON(ST_GeomFromGeoJSON)
- Intersections(ST_Intersection)
- Intersects(ST_Intersects)
- IsCollection(ST_IsCollection)
- IsEmpty(ST_IsEmpty)
- IsValid(ST_IsValid)
- Length(ST_Length)
- MakeLine(ST_MakeLine)
- MakePoint(ST_MakePoint)
- MakePolygon(ST_MakePolygon)
- NumPoints(ST_NumPoints)
- Perimeter(ST_Perimeter)
- Point(ST_Point)
- SetSRID(ST_SetSRID)
- Touches(ST_Touches)
- Union(ST_Union)
- Within(ST_Within)
- X(ST_X)
- Y(ST_Y)
- Z(ST_Z)

## Development

### Dependencies

- [Python](https://www.python.org/downloads/)
- [poetry](https://poetry.eustace.io/)

### Setup

```bash
poetry install
```

### Tests

Full tests and coverage

```bash
poetry run pytest
```

### Publish

```bash
poetry build
poetry publish
```

## Credits

pypika-gis is based on [PyPika](https://github.com/kayak/pypika). Check their page for further query buider instructions, examples and more details about PyPika core.
