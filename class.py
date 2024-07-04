class House:
    def __init__(self, name, number_of_flour):
        self.name = name
        self.number_of_flour = number_of_flour

    def go_to(self, new_flour):
        if 1 <= new_flour <= self.number_of_flour:
            for floor in range(1, new_flour + 1):
                print(f"прибытие на {floor} этаж")
            else:
                print("такого этажа не существует")


my_house = House('ЖК Эльбрус', 30)
my_house.go_to(15)
