# Импорт класса MetricsCalculator из модуля calculator
from calculator import MetricsCalculator


# Основная функция программы
def main():
    # Установка пути к файлу с данными в безопасном формате строки
    filepath = r'C:\Users\euene\PycharmProjects\financial_tools\data.txt'

    # Создание экземпляра калькулятора метрик с указанным путем файла
    calculator = MetricsCalculator(filepath)

    # Вызов метода для обработки данных из файла
    calculator.process_file()

    # Вычисление метрик для всех инструментов и сохранение результатов
    results = calculator.calculate_all_metrics()

    # Итерация по результатам и вывод метрик каждого инструмента
    for instrument, metrics in results.items():
        print(f"{instrument}: {metrics}")


# Проверка, запущен ли скрипт непосредственно, и не в режиме импорта
if __name__ == '__main__':
    main()
