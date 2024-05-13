from instruments import Instrument1, Instrument2, Instrument3


# Класс для расчёта метрик по финансовым инструментам из файла
class MetricsCalculator:
    def __init__(self, filepath):
        self.filepath = filepath  # Путь к файлу с данными
        # Словарь, сопоставляющий имена инструментов с их объектами
        self.instruments = {
            'INSTRUMENT1': Instrument1('INSTRUMENT1'),
            'INSTRUMENT2': Instrument2('INSTRUMENT2'),
            'INSTRUMENT3': Instrument3('INSTRUMENT3')
        }

    # Метод для чтения данных из файла и добавления записей в соответствующие инструменты
    def process_file(self):
        with open(self.filepath, 'r') as file:  # Открытие файла для чтения
            for line in file:  # Чтение файла построчно
                name, date, price = line.strip().split(',')  # Разбор строки на компоненты
                if name in self.instruments:  # Проверка, существует ли такой инструмент
                    self.instruments[name].add_record(date, price)  # Добавление записи в инструмент

    # Метод для вычисления и возврата метрик всех инструментов
    def calculate_all_metrics(self):
        # Генерация словаря с результатами вычисления метрик для каждого инструмента
        return {name: instrument.calculate_metrics() for name, instrument in self.instruments.items()}
