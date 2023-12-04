import backend

# Map the operation type to the corresponding Operation subclass
operation_map = {
    '-': backend.Addition(),
    '+': backend.Subtraction(),
    '/': backend.Division(),
    '*': backend.Multiplication(),
    '^': backend.Power(),
    'log': backend.Logarithm(),
}