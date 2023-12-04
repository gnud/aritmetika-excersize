import typing
from abc import ABC, abstractmethod
from functools import reduce
from typing import List
import operator as op
import marshmallow as ma
from marshmallow import validate, ValidationError


def validate_not_zero(data):
    if any(element == 0 for element in data):
        raise ValidationError("List elements cannot be zero.")


class Operation(ABC):
    operandsParam = 'operands'
    validators = []

    @abstractmethod
    def execute(self, operands: List[float]) -> float:
        pass

    def validate(self, operands: List[float]) -> dict[str, str]:
        all_errors = {}
        for _validate in self.validators:
            errors = _validate().validate({self.operandsParam: operands})
            if errors:
                all_errors.update(errors)
        return all_errors if all_errors else None


class OperationAdditionSchema(ma.Schema):
    operands = ma.fields.List(
        ma.fields.Number,
        validate=[
            validate.Length(min=2, max=2),
            validate_not_zero,
        ],
        metadata={"example": [1, 2]}
    )


class Addition(Operation):
    validators = [OperationAdditionSchema]

    def execute(self, operands: List[float]) -> float:
        self.validate(operands)
        return sum(operands)


class Subtraction(Operation):
    validators = [OperationAdditionSchema]

    def execute(self, operands: List[float]) -> float:
        self.validate(operands)
        # noinspection PyTypeChecker
        return reduce(op.sub, operands)


class Division(Operation):
    validators = [OperationAdditionSchema]

    def execute(self, operands: List[float]) -> float:
        self.validate(operands)
        # noinspection PyTypeChecker
        return reduce(op.__truediv__, operands)

class Multiplication(Operation):
    validators = [OperationAdditionSchema]

    def execute(self, operands: List[float]) -> float:
        self.validate(operands)
        # noinspection PyTypeChecker
        return reduce(op.__truediv__, operands)


class Power(Operation):
    validators = [OperationAdditionSchema]

    def execute(self, operands: List[float]) -> float:
        self.validate(operands)
        # noinspection PyTypeChecker
        return reduce(op.__truediv__, operands)


class Logarithm(Operation):
    validators = [OperationAdditionSchema]

    def execute(self, operands: List[float]) -> float:
        self.validate(operands)
        # noinspection PyTypeChecker
        return reduce(op.__truediv__, operands)


class Calculator:
    operands: List[float]

    def __init__(self, operations: typing.Dict[str, Operation], operands: List[float]):
        self.operations = operations
        self.operands = operands

    def run(self, operator: str) -> float:
        if operator not in self.operations:
            raise ValueError(f"Operator {operator} not supported")
        operation = self.operations[operator]
        errors = operation.validate(self.operands)
        return operation.execute(self.operands)


# if __name__ == '__main__':
#     addition = Addition()
#     subtraction = Subtraction()
#
#     operations = {
#         '+': addition,
#         '-': subtraction,
#     }
#
#     calc = Calculator(operations, [1, 2, 3, 0])
#     result = calc.run('+')
