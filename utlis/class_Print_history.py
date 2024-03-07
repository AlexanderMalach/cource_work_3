import datetime
import f


class Print_history:
    """ Принимает json объект и его индекс, вытаскивает словарь"""

    def __init__(self, dict_json_all, number_operation=0):
        self.number_operation = number_operation
        self.dict_json_all = dict_json_all
        self.dict_json = list(self.dict_json_all)[self.number_operation]

    def date_print(self):
        """ Запрашивает у словаря строку по ключу 'date',
        форматирует строку и возвращет дату в формате '%d.%m.%Y'"""

        self.date_slice = (self.dict_json).get('date')
        if f.check_error(self.date_slice):
            self.date_print_datetime = datetime.datetime.strptime(self.date_slice[:10], "%Y-%m-%d")
            self.date_print_point = self.date_print_datetime.strftime("%d.%m.%Y")
            return self.date_print_point

    def print_line(self, line_title):
        """ Запрашивает у словаря по ключу строку и возвращает её значение"""

        self.line_title = line_title
        self.line_output = self.dict_json.get(self.line_title)
        if f.check_error(self.line_output):
            return self.line_output

    def account_code(self, from_and_to):
        """ Зашифровка карт  в формате  XXXX XX** **** XXXX
        счета в формате  **XXXX"""

        self.from_and_to = from_and_to
        self.payment = (self.dict_json).get(self.from_and_to)
        if f.check_error(self.payment):
            if "Счет" in self.payment:
                return f'Счет **{self.payment[-4:]}'
            else:
                return f'{self.payment[-16:-12]} {self.payment[-12:-10]}** **** {self.payment[-4:]}'

    def currency(self):
        """ Выводит занчение словаря operationAmount возварщает значенеи amount и name"""
        self.operation_amount = self.dict_json.get("operationAmount")
        if f.check_error(self.operation_amount):
            self.currency = self.operation_amount.get("currency")
            if f.check_error(self.currency):
                return self.operation_amount.get("amount") + ' ' + self.currency.get("name")
