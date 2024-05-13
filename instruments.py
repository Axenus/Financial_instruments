import datetime


# Базовый класс для финансовых инструментов
class FinancialInstrument:
    def __init__(self, name):
        self.name = name  # Имя финансового инструмента
        self.prices = []  # Список для хранения цен и дат

    # Метод для добавления записи о цене в определенную дату
    def add_record(self, date, price):
        # Добавление кортежа (дата, цена), где дата преобразуется из строки
        self.prices.append((datetime.datetime.strptime(date, '%d-%b-%Y'), float(price)))

    # Заглушка метода для расчета метрик, должна быть переопределена в подклассах
    def calculate_metrics(self):
        raise NotImplementedError("This method should be overridden by subclasses")


# Класс для финансового инструмента типа 1
class Instrument1(FinancialInstrument):
    # Расчет средней цены всех записей
    def calculate_metrics(self):
        return sum(price for _, price in self.prices) / len(self.prices) if self.prices else None


# Класс для финансового инструмента типа 2
class Instrument2(FinancialInstrument):
    # Расчет средней цены за ноябрь 2014 года
    def calculate_metrics(self):
        nov_prices = [price for date, price in self.prices if date.month == 11 and date.year == 2014]
        return sum(nov_prices) / len(nov_prices) if nov_prices else None


# Класс для финансового инструмента типа 3
class Instrument3(FinancialInstrument):
    # Определение дней, когда цена уменьшалась по сравнению с предыдущим днем
    def calculate_metrics(self):
        decreasing_days = []
        for i in range(1, len(self.prices)):
            if self.prices[i][1] < self.prices[i - 1][1]:
                decreasing_days.append(self.prices[i][0])
        return decreasing_days
