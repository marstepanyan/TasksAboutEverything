class Observer:
    def update(self, subject):
        pass


class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class TemperatureDisplay(Observer):
    def update(self, subject):
        print(f"Temperature Display: {subject.temperature}°C")


class Fan(Observer):
    def update(self, subject):
        if subject.temperature > 25:
            print("Fan: Turning on the fan.")
        else:
            print("Fan: Turning off the fan.")


def main():
    weather_station = WeatherStation()

    temp_display = TemperatureDisplay()
    fan = Fan()

    weather_station.add_observer(temp_display)
    weather_station.add_observer(fan)

    weather_station.set_temperature(20)
    weather_station.set_temperature(30)

    weather_station.remove_observer(fan)

    weather_station.set_temperature(15)


if __name__ == "__main__":
    main()
