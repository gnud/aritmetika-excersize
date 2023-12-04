import marshmallow as ma
from marshmallow import validate

from core import Arithmetics


class ArithmeticaSchema(ma.Schema):
    operands = ma.fields.List(
        ma.fields.Number,
        validate=validate.Length(min=2, max=2),
        metadata={"example": [1, 2]}
    )
    operator = ma.fields.String(
        validate=validate.OneOf(list(iter(Arithmetics().get_operators()))),
        metadata={"example": '-'}
    )


class ArithmeticaResponseSchema(ma.Schema):
    code = ma.fields.Number(required=False)
    status = ma.fields.String(required=False)
    result = ma.fields.String(required=False)
    errors = ma.fields.List(ma.fields.String(), required=False)


class OperatorsResponseSchema(ma.Schema):
    result = ma.fields.List(ma.fields.String(), required=False)


class ErrorSchema(ma.Schema):
    code = ma.fields.Number(required=False)
    status = ma.fields.Integer(required=True, description='HTTP status code of the error.')
    error = ma.fields.String(required=True, description='HTTP error message.')
    message = ma.fields.String(required=True, description='Error message.')


