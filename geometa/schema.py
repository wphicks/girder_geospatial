from marshmallow import Schema, fields
import pyproj


class WrongGeospatialMetadata(Exception):
    pass


class Crs(fields.Field):
    def _deserialize(self, value, attr, obj):
        try:
            pyproj.Proj(init=value, errcheck=True)
            return value
        except RuntimeError:
            raise WrongGeospatialMetadata('crs is not a valid proj4 string.')


class NativeBounds(fields.Field):
    # TODO: Validate native bounds
    def _deserialize(self, value, attr, obj):
        return value


class Bounds(fields.Field):
    # TODO: Validate native bounds
    def _deserialize(self, value, attr, obj):
        return value


class BaseSchema(Schema):
    crs = Crs(required=True)
    nativeBounds = NativeBounds(required=True)
    bounds = Bounds(required=True)
    type_ = fields.String(required=True)
    date = fields.Date(default='')
    # TODO: Validate altitude fields
    altitudeEllipsoid = fields.String()
    nativeAltitude = fields.List(fields.Float)
    altitude = fields.List(fields.Float)