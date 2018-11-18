from pypika.terms import (
    Function
)


class AsGeoJSON(Function):
    def __init__(self, term, alias=None):
        super(AsGeoJSON, self).__init__('ST_AsGeoJSON', term, alias=alias)


class Y(Function):
    def __init__(self, term, alias=None):
        super(Y, self).__init__('ST_Y', term, alias=alias)


class X(Function):
    def __init__(self, term, alias=None):
        super(Y, self).__init__('ST_Y', term, alias=alias)
