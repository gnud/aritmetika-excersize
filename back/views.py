import math
import typing

from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort, ErrorHandlerMixin
from marshmallow import ValidationError

from core import Arithmetics
from errors import ArithmeticOperatorFailed
from schemas import ArithmeticaSchema, ArithmeticaResponseSchema, OperatorsResponseSchema, ErrorSchema
import backend
import operations

blp = Blueprint(
    'Arithmetica', __name__, description='Operations on Arithmetica'
)


def create_exception_response(error_message, status='FAILED'):
    return {
        'status': status,
        'result': math.nan,
        'errors': [error_message]
    }


@blp.route('/operations')
class OperationsAPI(MethodView):
    @blp.response(200, OperatorsResponseSchema)
    def get(self):
        return {
            'result': Arithmetics().get_operators()
        }


@blp.route('/calculate')
class ArithmeticaAPI(ErrorHandlerMixin, MethodView):
    ERROR_SCHEMA = ErrorSchema

    @blp.arguments(ArithmeticaSchema)
    @blp.response(201, ArithmeticaResponseSchema)
    def post(self, data):
        operands: typing.List[str] = data.get('operands')
        operator = data.get('operator')

        calculation = Arithmetics(operands=operands)

        try:
            result = str(calculation.calculate(operator))
        except ArithmeticOperatorFailed as err:
            return abort(400, **create_exception_response(str(err)))
        except ZeroDivisionError as err:
            return abort(400, **create_exception_response(str(err)))
        except ValueError as err:
            return abort(400, **create_exception_response(str(err)))
        return {
            'status': 'OK',
            'result': result,
            'errors': None
        }


@blp.route('/v2/operations')
class OperationsAPI(MethodView):
    @blp.response(200, OperatorsResponseSchema)
    def get(self):
        operation_names = list(operations.operation_map.keys())

        return {
            'result': operation_names
        }


@blp.route('/v2/calculate')
class ArithmeticaAPI(ErrorHandlerMixin, MethodView):
    # ERROR_SCHEMA = ErrorSchema

    @blp.arguments(ArithmeticaSchema)
    @blp.response(201, ArithmeticaResponseSchema)
    def post(self, data):
        operation_type = data.get('operator')
        operands = data.get('operands', [])

        operation = operations.operation_map.get(operation_type)

        if not operation:
            return jsonify({'error': 'Invalid operation type'}), 400

        try:
            result = operation.execute(operands)
            return jsonify({'result': result})
        except ValidationError as e:
            return jsonify(create_exception_response(str(e), status='Unprocessable Entity')), 422
        except ValueError as e:
            return jsonify(create_exception_response(str(e), status='Unprocessable Entity')), 422
        except Exception as e:
            return jsonify(create_exception_response(str(e), status='Unprocessable Entity')), 422
