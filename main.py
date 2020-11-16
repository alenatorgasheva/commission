class Value:
    def __init__(self, value=0):
        self.value = value

    @staticmethod
    def _prepare_value(value, commission):
        return (1 - commission) * value

    def __get__(self, obj, obj_type):
        return int(self.value)

    def __set__(self, obj, value):
        self.value = self._prepare_value(value, obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
