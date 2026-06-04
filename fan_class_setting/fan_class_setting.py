class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, radius=5, color="blue", on=False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on

    def get_speed(self):
        return self.speed

    def get_radius(self):
        return self.radius

    def get_color(self):
        return self.color

    def get_on(self):
        return self.on

