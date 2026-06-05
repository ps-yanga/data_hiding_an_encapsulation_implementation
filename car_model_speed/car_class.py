from markdown_it.presets.commonmark import make


class Car:
    def __init__(self, year_model,make):
    self._year_model=year_model
    self._make=make
    self._speed=0

    def accelerate(self):
        self._speed+=5

    def brake(self):
        self._speed-=5

    def get_speed(self):
        return self._speed

    