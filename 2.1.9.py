class NonPositiveError(ArithmeticError):
    pass


class PositiveList(list):
    def append(self, x):
        x = int(x)
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError


pos_list = PositiveList([])
pos_list.append("1")

