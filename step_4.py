#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            manufacturer: str,
            model: str,
            color: str,
            purchase_price: float,
    ):
        self.type = eq_type
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.purchase_price = purchase_price
        self.printable = True if self.type in ("printer", "MFP") else False
        self.scannable = True if self.type in ("scanner", "MFP") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.purchase_price * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.manufacturer} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('Сканер', *args)


class Mfp(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('МФУ', *args)


if __name__ == '__main__':
    p1 = Printer("HP", "p1102", "grey", 4000)
    print(p1)
