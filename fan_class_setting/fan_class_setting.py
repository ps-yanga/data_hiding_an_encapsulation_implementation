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

    def set_speed(self, speed):
        self.speed = speed

    def set_radius(self, radius):
        self.radius = radius

    def set_color(self, color):
        self.color = color

    def set_on(self, on):
        self.on = on

    def __str__(self):
        status="on" if self.on else "off"
        return f"fan(speed={self.speed}, radius={self.radius}, color={self.color}, on={self.on})"