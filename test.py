import pytest
from instruments import Instrument1, Instrument2, Instrument3
import datetime


# Фикстура для подготовки объекта Instrument1 с тестовыми данными
@pytest.fixture
def setup_instrument1():
    instrument = Instrument1('INSTRUMENT1')
    instrument.add_record('01-Jan-2015', '100')  # Добавление записи
    instrument.add_record('02-Jan-2015', '200')  # Добавление еще одной записи
    return instrument  # Возврат сконфигурированного объекта для теста


# Фикстура для подготовки объекта Instrument2 с тестовыми данными за ноябрь 2014
@pytest.fixture
def setup_instrument2():
    instrument = Instrument2('INSTRUMENT2')
    instrument.add_record('01-Nov-2014', '300')  # Добавление записи за ноябрь
    instrument.add_record('02-Nov-2014', '400')  # Добавление следующей записи за ноябрь
    return instrument  # Возврат объекта для теста


# Фикстура для подготовки объекта Instrument3 с тестовыми данными, включая падение цен
@pytest.fixture
def setup_instrument3():
    instrument = Instrument3('INSTRUMENT3')
    instrument.add_record('01-Mar-2015', '500')  # Добавление записи
    instrument.add_record('02-Mar-2015', '400')  # Добавление записи с уменьшенной ценой
    instrument.add_record('03-Mar-2015', '300')  # Добавление записи с ещё более низкой ценой
    return instrument  # Возврат объекта для теста


# Тест для проверки расчета средней цены инструмента Instrument1
def test_average_price_instrument1(setup_instrument1):
    assert setup_instrument1.calculate_metrics() == 150  # Проверка правильности расчета


# Тест для проверки расчета средней цены за ноябрь 2014 года для Instrument2
def test_average_price_instrument2_november(setup_instrument2):
    assert setup_instrument2.calculate_metrics() == 350  # Проверка правильности расчета


# Тест для проверки дат уменьшения цен для Instrument3
def test_decreasing_days_instrument3(setup_instrument3):
    expected_dates = [datetime.datetime(2015, 3, 2, 0, 0), datetime.datetime(2015, 3, 3, 0, 0)]
    assert setup_instrument3.calculate_metrics() == expected_dates  # Проверка наличия правильных дат
