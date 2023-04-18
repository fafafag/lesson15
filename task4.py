class Car:
    def __init__(self, color, brand, body_type, speed, transmission):
        self.color = color
        self.brand = brand
        self.body_type = body_type
        self.speed = speed
        self.transmission = transmission

    def start(self):
        print(f'The {self.color} {self.brand} {self.body_type} starts moving')

    def stop(self):
        print(f'The {self.color} {self.brand} {self.body_type} stops')

    def turn(self, direction):
        print(f'The {self.color} {self.brand} {self.body_type} turns {direction}')

    def speed_up(self, speed):
        if self.body_type == 'truck' and self.speed + speed > 60:
            print('Speed limit exceeded! Maximum allowed speed is 60 km/h')
        elif self.body_type == 'car' and self.speed + speed > 80:
            print('Speed limit exceeded! Maximum allowed speed is 80 km/h')
        else:
            self.speed += speed
            print(f'The {self.color} {self.brand} {self.body_type} speeds up to {self.speed} km/h')

    def speed_down(self, speed):
        self.speed -= speed
        print(f'The {self.color} {self.brand} {self.body_type} slows down to {self.speed} km/h')

    def beep(self):
        print(f'The {self.color} {self.brand} {self.body_type} beeps')

car1 = Car('red', 'Toyota', 'sedan', 60, 'automatic')
car2 = Car('blue', 'Lada', 'sedan', 40, 'manual')
truck1 = Car('yellow', 'Volvo', 'truck', 80, 'manual')
truck2 = Car('green', 'MAN', 'truck', 70, 'automatic')

car1.start()
car1.speed_up(20)
car1.turn('left')
car1.speed_down(10)
car1.beep()
car1.stop()

car2.start()
car2.speed_up(30)
car2.turn('right')
car2.speed_down(15)
car2.beep()
car2.stop()

truck1.start()
truck1.speed_up(30)
truck1.turn('right')
truck1.speed_down(20)
truck1.beep()
truck1.stop()

truck2.start()
truck2.speed_up(25)
truck2.turn('left')
truck2.speed_down(10)
truck2.beep()
truck2.stop()