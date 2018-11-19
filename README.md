# pypika-gis

SpatialTypes functions for extend [PyPika](https://github.com/kayak/pypika) with GIS.

## Example

```python
from pypika import Query
from pypika_gis import spatialtypes as st

query = Query.from_('field').select('id', st.AsGeoJSON('geom'))
print(str(query))
# SELECT "id",ST_AsGeoJSON('geom') FROM "field"

query = Query.from_('crop').select('id').where(st.Intersects('geom', st.SRID(st.MakePoint(10, 5), 4326)))
print(str(query))
# SELECT "id" FROM "crop" WHERE ST_Intersects('geom',ST_SRID(ST_MakePoint(10,5),4326))
```

## Available functions

- Envelope(ST_Envelope)
- Extent(ST_Extent)
- GeomFromGeoJSON(ST_GeomFromGeoJSON)
- GeoHash(ST_GeoHash)
- Intersection(ST_Intersection)
- Intersects(ST_Intersects)
- IsEmpty(ST_IsEmpty)
- IsValid(ST_IsValid)
- MakePoint(ST_MakePoint)
- SetSRID(ST_SetSRID)
- Within(ST_Within)
- X(ST_X)
- Y(ST_Y)
- Z(ST_Z)

## Dependencies

- [PyPika](https://github.com/kayak/pypika)

## Setup

```bash
pip install pypika-gis
```

## Development

Full tests and coverage

```bash
pip install -r requirements-dev.txt
python -m pytest --cov
```

## Credits

pypika-gis is based on [PyPika](https://github.com/kayak/pypika). Check their page for further query buider instructions, examples and more details about PyPika core.
