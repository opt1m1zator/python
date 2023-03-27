#5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).


class AppError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptWarehouseError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferWarehouseError(AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddWarehouseError = AcceptWarehouseError


class ValidateEquipmentError(AppError):
    pass


class Warehouse:
    def __init__(self):
        self.__Warehouse = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddWarehouseError(f"Вы пытаетесь добавить на склад не оргтехнику")

        self.__Warehouse.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferWarehouseError(f"Недопустимый тип")

        item: OfficeEquipment = self.__Warehouse[idx]

        if item.department:
            raise TransferWarehouseError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__Warehouse[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__Warehouse[key]

    def __iter__(self):
        return self.__Warehouse.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__Warehouse)} устройств"


class OfficeEquipment:
    __required_props = ("eq_type", "manufacturer", "model")

    def __init__(self, eq_type: str = None, manufacturer: str = "", model: str = ""):
        self.type = eq_type
        self.manufacturer = manufacturer
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.manufacturer} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Принтер', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Сканер', **kwargs)


class Mfp(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='МФУ', **kwargs)


if __name__ == '__main__':
    warehouse = Warehouse()
    warehouse.add(Printer.create(4, manufacturer="HP", model="p1102"))
    warehouse.add(Scanner.create(3, manufacturer="Canon", model="Lide-350"))
    warehouse.add(Scanner.create(2, manufacturer="Canon", model="Lide-300"))
    warehouse.add(Mfp.create(6, manufacturer="Brother", model="MFC-L2700DWR"))
    print(warehouse)

    for idx, itm in warehouse.filter_by(department=None, manufacturer="Canon", model="Lide-350"):
        print(f"Резервируем {itm} в 'Отдел 11'")
        warehouse.transfer(idx, 'Отдел 11')

    for idx, itm in warehouse.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print(warehouse)
    print("Списываем 1 устройство")
    del warehouse[0]
    print(warehouse)
