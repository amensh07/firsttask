class Road:

    def first(self, _length, _width):
        self._length = _length
        self._width = _width

    def _area(self):
        result = self._length * self._width * 25 * 5
        print(f'Масса асфальта,необходимая для покрытия всего дорожного полотна = {result}')


road = Road()
road.first(10, 15)
road._area()
