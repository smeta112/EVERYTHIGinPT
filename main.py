class Car:
    def __init__(self, color, speed, mark): #(указывает св-ва)
        self.color = color
        self.speed = speed
        self.mark = mark

    def Drive(self, pllace):
        print("Машина марки {self.mark}, цвета{self.color}, едет в {place}"+f"со скоростью{self.speed}")