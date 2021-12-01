
class IncorrectDataRecivedError(Exception):

    def __str__(self):
        return 'Принято неккоректное сообщение  от удаленного компьютера.'


class NonDictInputError(Exception):

    def __str__(self):
        return 'Аргумент функции должен быть словарём.'


class ReqFieldMissingError(Exception):

    def __init__(self, missing_field):
        self.missing_field = missing_field

    def __str__(self):
        return f'В принятом словаре отсутствует обязательное поле {self.missing_field}.'
