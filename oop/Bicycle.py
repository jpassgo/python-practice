import time


class Bicycle:

    def __init__(self):
        self.passengers = 0
        self.speed = (0.0)
        self.rate_of_acceleration = 1.0
        self.interrupt = False

    def enter_vehicle(self):
        self.passengers += 1

    def exit_vehicle(self):
        self.passengers -= 1

    # Start the acceleration timer 
    def begin_acceleration(self):
        self.acceleration_start_time = time.time()

    # 1. End the acceleration timer.
    # 2. Calculate time elapsed since acceleration began.
    # 3. Multiply the time elapse by the rate of acceleration (1m per second) by 3.6 (conversion from meters per second to kilometers per hour).
    def end_acceleration(self):
        seconds_elapsed = time.time() - self.acceleration_start_time
        seconds_elapsed = seconds_elapsed if seconds_elapsed <= 6 else 6
        self.speed = seconds_elapsed * 3.6

    def decelerate(self):
        pass

    def turn(self, direction):
        pass

    def current_speed(self):
        return self.speed


bike = Bicycle()

bike.begin_acceleration()
time.sleep(7)
bike.end_acceleration()

print(f"Current speed: {bike.current_speed()} kmh")