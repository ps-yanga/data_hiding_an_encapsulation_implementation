class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self._speed = speed
        self._radius = radius
        self._color = color
        self._on = on

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value in [self.SLOW, self.MEDIUM, self.FAST]:
            self._speed = value
        else:
            print(f"Invalid speed: {value}")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value>0:
            self._radius = value
        else:
            print(f"Invalid radius: {value}")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, value):
        if isinstance(value, bool):
            self._on = value
        else:
            print(f"Invalid on: {value}")

    def __str__(self):
        status="on" if self.on else "off"
        return f"fan(speed={self._speed}, radius={self._radius}, color={self._color}, on={status})"