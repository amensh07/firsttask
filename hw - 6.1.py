from time import sleep
import turtle


class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    def running(self, w, sec_red, sec_yellow, sec_green):
        """Метод рисует светофор. Каждый цвет в течение
        нескольких секунд.

        Ключевые аргументы:
        w -- длина стороны квадрата для формирования картинки
        sec_red/yellow/green -- столько секунд будет гореть
        каждый цвет

        """
        joe = turtle.Turtle()
        cycle = turtle.Turtle()
        joe.speed(100)
        for i in range(2):
            joe.pensize(5)
            joe.left(90)
            joe.fd(w + 10)
            joe.left(90)
            joe.fd(w + 10)
        for i in range(3):
            cycle.speed(100)
            cycle.color(self.__colors[i % 3], self.__colors[i % 3])
            cycle.up()
            cycle.bk(w / 2 + 5)
            cycle.right(90)
            cycle.bk(5)
            cycle.left(90)
            cycle.down()
            cycle.begin_fill()
            cycle.fillcolor(self.__colors[i % 3])
            cycle.circle(w / 2, 360)
            cycle.end_fill()
            if i == 0:
                sleep(sec_red)
            elif i == 1:
                sleep(sec_yellow)
            else:
                sleep(sec_green)
            cycle.reset()


TrafficLight = TrafficLight()
TrafficLight.running(300, 4, 5, 2)
turtle.done()
