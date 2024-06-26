from abc import ABC, abstractmethod
from typing import Any

from pytemplate.domain.models import City, Dish, Restaurant


class RestaurantService(ABC):

    @abstractmethod
    def allocate_city(self, data: dict[str, Any]) -> City:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def make_dish(self, data: dict[str, Any]) -> Dish:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
        raise NotImplementedError("This method should be overridden by subclasses")

    @abstractmethod
    def create(self, data: dict[str, Any]) -> Restaurant:
        raise NotImplementedError("This method should be overridden by subclasses")
