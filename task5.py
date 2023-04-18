import time
class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        self.__color = 'Красный'
        print(f'Светофор переключился на цвет: {self.__color}')
        time.sleep(1)

        self.__color = 'Желтый'
        print(f'Светофор переключился на цвет: {self.__color}')
        time.sleep(0.5)

        self.__color = 'Зеленый'
        print(f'Светофор переключился на цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'Желтый'
        print(f'Светофор переключился на цвет: {self.__color}') # Добавим блок, чтобы показать 2-ух секундную работу зелёного сигнала
        time.sleep(0.5)

tl = TrafficLight()
tl.running()