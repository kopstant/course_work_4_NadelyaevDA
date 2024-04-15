from abc import ABC, abstractmethod
import requests
import json
from datetime import datetime


class AbstractService(ABC):
    """
    Абстрактный класс для работы с API сервиса вакансий.
    В этом классе можно определять общие методы и свойства для работы с API сервисов с вакансиями
    """
    def __init__(self, api_url):

        self.api_url = api_url

    def connect_to_api(self):
        """Метод для подключения к API"""
        pass

    def get_vacancies(self):
        """ метод для получения данных о вакансиях"""
        pass


class HHruVacancyService(AbstractService):
    """
    Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru
    В этом классе необходимо определить методы для подключения к API hh.ru и получения данных о вакансиях.
    Также изменены методы обработки данных, чтобы они соотвествовали структуре данных hh.ru
    """
    def __init__(self):
        super().__init__("https://api.hh.ru")

    def get_vacancies(self):
        response = requests
