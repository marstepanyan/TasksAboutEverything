# Command Interface

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete Command Classes

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Receiver

class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


# Invoker

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


# Client code

# Receiver
living_room_light = Light()

# Concrete Command objects
light_on_command = LightOnCommand(living_room_light)
light_off_command = LightOffCommand(living_room_light)

# Invoker
remote_control = RemoteControl()

# Turn ON the light
remote_control.set_command(light_on_command)
remote_control.press_button()

# Turn OFF the light
remote_control.set_command(light_off_command)
remote_control.press_button()
