from typing import Any

import pytest

from pytemplate.domain.models import City, Dish, Restaurant
from src.pytemplate.service.restaurant import RestaurantService


def test_allocate_city_not_implemented():

    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            return super().allocate_city(data)

        def make_dish(self, data: dict[str, Any]) -> Dish:
            pass

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            pass

        def create(self, data: dict[str, Any]) -> Restaurant:
            pass

    service = ConcreteRestaurantService()

    with pytest.raises(NotImplementedError):
        service.allocate_city({"city_name": "TestCity"})


def test_make_dish_not_implemented():
    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            pass

        def make_dish(self, data: dict[str, Any]) -> Dish:
            return super().make_dish(data)

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            pass

        def create(self, data: dict[str, Any]) -> Restaurant:
            pass

    service = ConcreteRestaurantService()

    with pytest.raises(NotImplementedError):
        service.make_dish({"dish_name": "TestDish"})


def test_make_restaurant_not_implemented():

    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            pass

        def make_dish(self, data: dict[str, Any]) -> Dish:
            pass

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            return super().make_restaurant(city, dishes)

        def create(self, data: dict[str, Any]) -> Restaurant:
            pass

    service = ConcreteRestaurantService()
    city = City(name="Beijing", country="China", population=21540000)
    dishes = [Dish(name="Kung Pao Chicken", price=12.5), Dish(name="Sweet and Sour Pork", price=10.0)]
    with pytest.raises(NotImplementedError):
        service.make_restaurant(city, dishes)


def test_create_not_implemented():

    class ConcreteRestaurantService(RestaurantService):
        def allocate_city(self, data: dict[str, Any]) -> City:
            pass

        def make_dish(self, data: dict[str, Any]) -> Dish:
            pass

        def make_restaurant(self, city: City, dishes: list[Dish]) -> Restaurant:
            pass

        def create(self, data: dict[str, Any]) -> Restaurant:
            return super().create(data)

    service = ConcreteRestaurantService()
    with pytest.raises(NotImplementedError):
        service.create({"city_name": "TestCity", "num_dishes": 3})
