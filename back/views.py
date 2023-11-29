import math
import typing

from flask.views import MethodView
from flask_smorest import Blueprint

from core import Arithmetics
from errors import ArithmeticOperatorFailed
from schemas import ArithmeticaSchema, ArithmeticaResponseSchema, OperatorsResponseSchema

blp = Blueprint(
    'Arithmetica', __name__, description='Operations on Arithmetica'
)


def create_exception_response(error_message):
    return {
        'status': 'FAILED',
        'result': math.nan,
        'errors': [error_message]
    }


@blp.route('/operations')
class OperationsAPI(MethodView):
    # @blp.arguments(ArithmeticaSchema)
    @blp.response(200, OperatorsResponseSchema)
    def get(self):
        return {
            'result': Arithmetics().get_operators()
        }


@blp.route('/calculate')
class ArithmeticaAPI(MethodView):
    @blp.arguments(ArithmeticaSchema)
    @blp.response(201, ArithmeticaResponseSchema)
    def post(self, data):
        operands: typing.List[str] = data.get('operands')
        operator = data.get('operator')

        calculation = Arithmetics(operands=operands)

        try:
            result = str(calculation.calculate(operator))
        except ArithmeticOperatorFailed as err:
            return create_exception_response(str(err))
        except ZeroDivisionError as err:
            return create_exception_response(str(err))
        except ValueError as err:
            return create_exception_response(str(err))
        return {
            'status': 'OK',
            'result': result,
            'errors': None
        }
