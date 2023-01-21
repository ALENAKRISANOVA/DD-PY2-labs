# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Kettle:
    def __init__(self, capacity_volume: float, occupied_volume: float, material: str):
        """"
        Создание объекта "Чайник"
        :param capacity_volume: Объем стакана
        :param occupied_volume: Объем занимаемой жидкости
        :param material: Материал чайника
        Примеры:
        >>> kettle = Kettle(100, 0, 'steel')  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем чайника должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем чайника должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

        def is_empty_kettle(self) -> bool:
            """
            Функция которая проверяет является ли чайник пустым
            :return: Является ли чайник пустым
            Примеры:
            >>> kettle = Kettle(500, 0, 'steel')
            >>> kettle.is_empty_kettle()
            """
            ...
        def set_material(self, material):
            """
            Изменение материала чайника
            :param material: материал
            :return: новый материал
            Пример:
            >>> kettle = Kettle(100, 35, 'plastic')
            >>> kettle.set_material('steel')
            """
            ...
class Smart_lamp:
    def __init__(self, time: int, light: str):
        """
        Создание объекта умная лампа
        :param time: время в данный момент времени в часах
        :param light: теплый или холодный свет от лампы в зависимости от времени
        Пример:
        >>> smart_lamp = Smart_lamp(7, 'cold')
        """
        if not isinstance(time, int):
            raise ValueError
        if time < 0:
            raise ValueError('Время не может быть отрицательным')
        self.time = time
    def check_light(self, time):
        """
        Проверяет, каким светом сейчас светит лампа
        :param time: время
        :return: цветовая температура света
        Пример:
        >>> lamp = Smart_lamp(12, 'cold')
        >>> lamp.check_light(17)
        """
        if not isinstance(time, int):
            raise ValueError
        if time < 0:
            raise ValueError('Время не может быть отрицательным')
        self.time = time
        ...
    def change_light(self, light):
        """
        Меняет цветовую температуру света лампы
        :param light: новый свет от лампы
        :return: новый свет от лампы
        Пример:
        >>> lamp = Smart_lamp(19, 'warm')
        >>> lamp.change_light('cold')
        """
        if not isinstance(light, str):
            raise ValueError
        ...
class Pocket:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание объекта карман
        :param capacity_volume: Объем кармана
        :param occupied_volume: Занятый объем кармана
        Пример:
        >>> pocket = Pocket(100, 57)
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем кармана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем кармана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Занятый оъем должнен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Занятый объем не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def set_volume(self, volume):
        """
        Изменение объема кармана
        :param volume: Новый объем
        :return: Новый объем кармана
        Пример:
        >>> pocket = Pocket(100, 30)
        >>> pocket.set_volume(70)
        """
        if not isinstance(volume, (int, float)):
            raise ValueError
        ...

    def is_empty_pocket(self) -> bool:
        """
        Функция которая проверяет является ли карман пустым
        :return: Является ли карман пустым
        Примеры:
        >>> pocket = Pocket(100, 0)
        >>> pocket.is_empty_pocket()
        """
        ...





if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
