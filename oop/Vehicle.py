from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Vehicle(ABC):

    @abstractmethod
    def enter_vehicle(self) -> None:
        pass

    @abstractmethod
    def exit_vehicle(self) -> None:
        pass

    @abstractmethod
    def begin_acceleration(self) -> None:
        pass

    @abstractmethod
    def decelerate(self) -> None:
        pass

    @abstractmethod
    def turn(self, direction) -> None:
        pass

    @abstractmethod
    def current_speed(self) -> None:
        pass
