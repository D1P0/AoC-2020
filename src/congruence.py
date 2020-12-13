from typing import List, Optional


class CongruentExpression:
    def __init__(self, res: int, mod: int, x: int = 1) -> None:
        self.x: int = x
        self.res: int = res
        self.mod: int = mod

    def subtract(self, expression: 'CongruentExpression', multiply: int) -> 'CongruentExpression':
        assert self.mod == expression.mod

        x: int = self.x - multiply * expression.x
        res: int = self.res - multiply * expression.res
        return CongruentExpression(res, self.mod, x)

    def simplify(self) -> 'CongruentExpression':
        self.x = self.x % self.mod
        self.res = self.res % self.mod
        return self

    def __str__(self):
        return "{}x = {} (mod {})".format(self.x, self.res, self.mod)

    def __repr__(self):
        return str(self)


class CongruentSystem:
    def __init__(self):
        self.expressions: List[CongruentExpression] = []

    def add(self, expression: CongruentExpression) -> None:
        self.expressions.append(expression)

    def solve(self):
        result: CongruentExpression = self.expressions[0]
        for i in range(1, len(self.expressions)):
            result = solve_expressions(result, self.expressions[i]).simplify()
        return result


def solve_expressions(exp_a: CongruentExpression, exp_b: CongruentExpression) -> Optional[CongruentExpression]:
    tmp_a: CongruentExpression = CongruentExpression(0, exp_b.mod, exp_a.x * exp_b.mod)
    tmp_b: CongruentExpression = CongruentExpression(exp_b.res - exp_a.res, exp_b.mod, exp_b.x * exp_a.mod)

    while tmp_a.x != 1 and tmp_b.x != 0:
        tmp_a, tmp_b = tmp_b, tmp_a.subtract(tmp_b, tmp_a.x // tmp_b.x)
    if tmp_b.x == 0:
        if tmp_b.res % tmp_b.mod != 0:
            return None
        if tmp_a.mod % tmp_a.x == 0:
            return CongruentExpression(exp_a.mod * (tmp_a.res // tmp_a.x) + exp_a.res, exp_a.mod * (tmp_a.mod // tmp_a.x))
        return CongruentExpression(exp_a.mod * (tmp_a.res // tmp_a.x) + exp_a.res, exp_a.mod * exp_b.mod)

    return CongruentExpression(tmp_a.res * exp_a.mod + exp_a.res, exp_a.mod * exp_b.mod)
