import math
import operator as op
import typing
from functools import reduce

from errors import ArithmeticOperatorFailed


class Arithmetics:
    def get_operators(self) -> typing.List[str]:
        return list(self.operators_map.keys())

    @property
    def operators_map(self) -> dict[str, typing.Callable]:
        return {
            '+': self.do_addition,
            '-': self.do_subtraction,
            '/': self.do_division,
            '*': self.do_multiplication,
            '^': self.do_power,
            'log': self.do_log,
        }

    def __init__(self, **kwargs):
        self.operands = kwargs.get('operands')

    # region Operators
    def do_addition(self):
        return reduce(op.__add__, self.operands)

    def do_subtraction(self):
        return reduce(op.__sub__, self.operands)

    def do_division(self):
        return reduce(op.__truediv__, self.operands)

    def do_multiplication(self):
        return reduce(op.__mul__, self.operands)

    def do_power(self):
        return reduce(op.__pow__, self.operands)

    def do_log(self):
        return reduce(math.log, self.operands)

    # endregion

    def calculate(self, operator) -> float:
        _callable: typing.Callable = self.operators_map.get(operator)

        if not _callable:
            raise ArithmeticOperatorFailed(f'Operator \'{operator}\' is not usable.')
        return _callable()


