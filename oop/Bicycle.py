import time
import decimal


class Bicycle:

    def __init__(self):
        self.passengers = 0
        self.speed = decimal.Decimal(0.0)
        self.rate_of_acceleration = 1.0
        self.rate_of_deceleration = 2.5
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
        seconds_elapsed = seconds_elapsed if seconds_elapsed <= 9 else 9
        self.speed = decimal.Decimal(seconds_elapsed * 3.6).__round__(2)

    def begin_deceleration(self):
        self.acceleration_start_time = time.time()

    def end_deceleration(self):
        seconds_elapsed = time.time() - self.acceleration_start_time
        seconds_elapsed = seconds_elapsed if seconds_elapsed <= 9 else 9
        self.speed = self.speed - decimal.Decimal((self.rate_of_deceleration * seconds_elapsed) * 3.6).__round__(2)
        self.speed = self.speed if self.speed > 0 else 0 

    def decelerate(self):
        pass

    def turn(self, direction):
        pass

    def current_speed(self):
        return self.speed


bike = Bicycle()

bike.begin_acceleration()
time.sleep(9)
bike.end_acceleration()
print(f"Current speed: {bike.current_speed()} kmh")

bike.begin_deceleration()
time.sleep(2)
bike.end_deceleration()
print(f"Current speed: {bike.current_speed()} kmh")